from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(name, **kwargs):
    env = Environment()
    env.loader = FileSystemLoader('Html-pages')
    tmpl = env.get_template(name)
    return tmpl.render(**kwargs)
