from jinja2 import Template
import os


def render(name, **kwargs):
    file_path = os.path.join('Html-pages', name)
    with open(file_path, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)
