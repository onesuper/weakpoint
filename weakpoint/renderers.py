


from jinja2 import Environment, FileSystemLoader, PrefixLoader
from jinja2.exceptions import TemplateNotFound

from weakpoint.exceptions import RendererException

import os

class Renderer(object):


    def __init__(self, path):
        self.environment = Environment(loader=FileSystemLoader(path + os.sep + "_templates"))

    def render(self, template, vars_ = {}):
        try:
            template = self.environment.get_template(template)
        except TemplateNotFound:
            raise RendererException('Template not found')
        
        return template.render(**vars_)



