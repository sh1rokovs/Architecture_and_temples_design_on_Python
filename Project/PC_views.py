from framework.template import render
from login import debug, Logger
from models import SiteWIthServices


site = SiteWIthServices()
logs = Logger('main.py')


def index_view(request):
    logs.logs('Список услуг')
    return '200 OK', render('index.html', query=site.services)


def services_views(request):
    return '200 OK', render('services.html')


@debug
def create_service_view(request):
    if request['method'] == 'POST':
        data = request['data']
        name = data['name']
        category_id = data.get('category_id')
        print(category_id)
        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))
            course = site.create_service('record', name, category)
            site.services.append(course)
        return '200 OK', render('create_services.html')
    else:
        categories = site.categories
        return '200 OK', render('create_services.html', categories=categories)


def create_category_view(request):
    if request['method'] == 'POST':
        data = request['data']
        name = data['name']
        category_id = data.get('category_id')
        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))
        new_category = site.create_category(name, category)
        site.categories.append(new_category)
        return '200 OK', render('create_category.html')
    else:
        categories = site.categories
        return '200 OK', render('create_category.html', categories=categories)


def team_view(request):
    return '200 OK', render('team.html')


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
