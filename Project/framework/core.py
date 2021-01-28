class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        print("it's works")
        path = environ['PATH_INFO']
        if not '/' in path[-1:]:
            path += '/'
        if path in self.routes:
            view = self.routes[path]
            request = {}
            for front in self.fronts:
                front(request)
            code, body = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [body.encode('utf-8')]
        else:
            start_response('404 Not Found', [('Content-Type', 'text/html')])
            return [b'404 Not Found']
