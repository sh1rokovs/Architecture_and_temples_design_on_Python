from framework.core import MockApplication
from framework.template import render
import FC_views as fc
import PC_views as pc
from models import SiteWIthServices
from login import Logger

site = SiteWIthServices()
logs = Logger('main.py')

routes = {
    '/': pc.index_view,
    '/services/': pc.services_views,
    '/create-services/': pc.create_service_view,
    '/create-category/': pc.create_category_view,
    '/contacts/': pc.contacts_view,
    '/team/': pc.team_view,
}

front = [fc.query_controller]

application = MockApplication(routes, front)


@application.add_route('/copy-course/')
def copy_course(request):
    request_params = request['request_params']
    name = request_params['name']
    old_service = site.get_service(name)
    if old_service:
        new_name = f'copy_{name}'
        new_service = old_service.copy()
        new_service.name = new_name
        site.services.append(new_service)

    return '200 OK', render('services.html', query=site.services)


@application.add_route('/category-list/')
def category_list(request):
    logs.logs('Список категорий')
    return '200 OK', render('service_category.html', query=site.categories)
