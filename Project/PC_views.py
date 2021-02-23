from framework.template import render
from framework.cbv import CreateView, ListView
from login import debug, Logger
from models import SiteWIthServices, EmailNotifier


email_notifier = EmailNotifier()
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
        if category_id:
            category = site.find_category_by_id(int(category_id))
            services = site.create_service('record', name, category)
            services.observers.append(email_notifier)
            site.services.append(services)
        categories = site.categories
        return '200 OK', render('create_service.html', categories=categories)
    else:
        categories = site.categories
        return '200 OK', render('create_service.html', categories=categories)


class CategoryCreateView(CreateView):
    template_name = 'create_category.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = site.categories
        return context

    def create_obj(self, data: dict):
        name = data['name']
        category_id = data.get('category_id')
        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))
        new_category = site.create_category(name, category)
        site.categories.append(new_category)


class CategoryListView(ListView):
    queryset = site.categories
    template_name = 'service_category.html'


class CustomerListView(ListView):
    queryset = site.customer
    template_name = 'customers.html'


class CustomerCreateView(CreateView):
    template_name = 'create_customer.html'

    def create_obj(self, data: dict):
        name = data['name']
        new_obj = site.create_user('student', name)
        site.customer.append(new_obj)


class AddCustomerByServiceCreateView(CreateView):
    template_name = 'add_customer.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['services'] = site.services
        context['customer'] = site.customer
        return context

    def create_obj(self, data: dict):
        service_name = data['service_name']
        service = site.get_service(service_name)
        customer_name = data['customer_name']
        customer = site.get_customer(customer_name)
        service.add_customer(customer)


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
