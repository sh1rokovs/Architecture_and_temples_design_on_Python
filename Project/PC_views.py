from framework.template import render


def index_view(request):
    print(request)
    query = request.get('query', None)
    return '200 OK', render('index.html', query=query)


def services_views(request):
    return '200 OK', 'Services'


def contacts_view(request):
    print(request)
    if request['method'] == 'POST':
        data = request['data']
        name = data['name']
        email = data['email']
        tel = data['tel']
        organize = data['organize']
        print(f'Новое сообщение от {name} из организации {organize}, его номер телефона:{tel} и email:{email}')
        return '200 OK', render('contacts.html')
    elif request['method'] == 'GET':
        print(request['data'])
        return '200 OK', render('contacts.html')
    else:
        return '200 OK', render('contacts.html')
