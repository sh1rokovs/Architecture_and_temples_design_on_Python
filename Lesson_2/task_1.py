# Post запрос
def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    print('method', method)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello from wsgi']
