


from argparse import ArgumentParser
from pkg_resources import resource_filename, load_entry_point


from weakpoint import __version__
from weakpoint.fs import Directory, File 
from weakpoint.utils import normpath
from weakpoint.config import Config
from weakpoint.parsers import markdown
from weakpoint.renderers import Renderer
from weakpoint.exceptions import OptionException, RendererException
from weakpoint.slides import Slides


from copy import deepcopy

import sys


class WeakPoint(object):
    # in case read key error, we make some 
    # default choices
    default_config = {
        'markup': 'markdown,'
    }

    def __init__(self, args = None):
        self.opts = self._get_opts(args)
        self.opts['func']()

    '''
    assume the src is on current dir
    generate index.html in the src
    '''
    def generate(self):
        self.src = Directory('.')   
        
        # load the config file before generate 
        self._load_config()
        
        # markdown => html 
        html = self._parse()

        # html => slides + navi
        htmldump = Slides(html) 
        slides = htmldump.slides
        navi = htmldump.navi
        
        # variables + slides (render)
        variables = {}
        variables.update(self.config)
        variables['slides'] = slides
        variables['navi'] = navi
        rendered = self._render(variables)

        # create index.html using rendered content
        out = File('index.html')
        if out.exists:
            out.rm()
        File('index.html', rendered).mk() 
        
         

    def init(self):
        self.dest = Directory(self.opts['dest'])
        self.src = Directory(self._get_theme(self.opts['theme']))

        if not self.src.exists:
            raise OptionException('Theme not found.')

        # copy the ./theme/{theme} to the dest
        self.src.cp(self.dest.path)



    def _render(self, variables):

        try:
            return Renderer(self.src.path).render("layout.html", variables)
        except RendererException, e:
            print e
            sys.exit(1)
        

    def _parse(self):

        path = File(normpath(self.src.path, 'slides.md'))
        if not path.exists:
            print "slides.md is required, abort"
            sys.exit(1)
        if self.config['markup'] == 'markdown':
            return markdown.Parser().parse(path.content)
            
        else:
            print 'no such markup: {0}'.format(config['markup'])
            sys.exit(1)


    def _load_config(self):
        self.config = deepcopy(self.default_config)

        f = File(normpath(self.src.path, 'config.yaml'))
        if f.exists:
            self.config.update(Config(f.content))
        else:
            print "missing config.yaml, abort"
            sys.exit(1)


    def _get_theme(self, theme):
        # the theme is intalled at weakpoint/themes/{theme}
        return resource_filename(__name__, 'themes/{0}'.format(theme))


    def _get_opts(self, args):
        opts = {}
        parser = ArgumentParser()
        subparser = parser.add_subparsers()

        # version
        parser.add_argument('-V', '--version', action = 'version',
                            version = '{0}'.format(__version__),
                            help = 'Show %(prog)s\'s version.')
        

        # gen
        gen = subparser.add_parser('gen')
        gen.set_defaults(func = self.generate)
        
        
        # init
        init = subparser.add_parser('init')
        init.set_defaults(func = self.init)
        init.add_argument('dest', metavar = 'destination',
                          help = 'The location %(prog)s initializes.')
        init.add_argument('-t', '--theme', default = 'light',
                          help = 'Sets the theme of slideshow.')



        # process the opts
        for option, value in vars(parser.parse_args(args)).iteritems():
            if value is not None:
                if isinstance(option, str):
                    option = option.decode('utf-8')
                if isinstance(value, str):
                    value = value.decode('utf-8')
                opts[option] = value
        
        return opts
        
