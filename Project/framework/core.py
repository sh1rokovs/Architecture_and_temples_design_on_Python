class Application:

    def parse_input_data(self, data: str):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    def parse_wsgi_input_data(self, data: bytes):
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    def get_wsgi_input_data(self, env):
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        print("it's works")
        path = environ['PATH_INFO']
        if not '/' in path[-1:]:
            path += '/'

        method = environ['REQUEST_METHOD']
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        query_string = environ['QUERY_STRING']
        request_params = self.parse_input_data(query_string)
        if path in self.routes:
            view = self.routes[path]

            request = {}
            request['method'] = method
            request['data'] = data
            request['request_params'] = request_params

            for front in self.fronts:
                front(request)
            code, body = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [body.encode('utf-8')]
        else:
            start_response('404 Not Found', [('Content-Type', 'text/html')])
            return [b'404 Not Found']
