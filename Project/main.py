from framework.core import Application
import FC_views as fc
import PC_views as pc

routes = {
    '/': pc.index_view,
    '/services/': pc.services_views,
}

front = [fc.query_controller]

application = Application(routes, front)
