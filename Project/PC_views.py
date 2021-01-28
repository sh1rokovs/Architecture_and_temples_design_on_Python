from framework.template import render


def index_view(request):
    print(request)
    query = request.get('query', None)
    return '200 OK', render('index.html', query=query)


def services_views(request):
    return '200 OK', 'Services'
