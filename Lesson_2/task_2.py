def parse_input_data(data):
    result = {}
    if data:
        params = data.split('&')
        for item in params:
            k, v = item.split('=')
            result[k] = v
    return result


def application(environ, start_response):
    query_string = environ['QUERY_STRING']
    method = environ['REQUEST_METHOD']
    print('method', method)
    print(query_string)
    request_params = parse_input_data(query_string)
    print(request_params)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello from wsgi']
