def application(environ, start_response):
    path = environ['PATH_INFO']
    if path == "/":
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Index']
    elif path == "/abc/":
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'ABC']
    else:
        start_response('404 OK', [('Content-Type', 'text/html')])
        return [b'404 NOT FOUND']
