# Page controller
def index_view(request):
    print(request)
    return '200 OK', [b'Index']


def abc_view(request):
    print(request)
    return '200 OK', [b'ABC']


def not_found_404_view(request):
    print(request)
    return '404 OK', [b'404 NOT FOUND']


routes = {
    '/', index_view,
    '/abc/', abc_view,
}


class Application:
    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if path == '/':
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [b'Index']
        elif path == '/abc/':
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [b'ABC']
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b'404 NOT FOUND']


application = Application(routes)
