import markdown as m

try:
    import pygments
    have_pygments = True
except ImportError:
    have_pygments = False

class Parser():
    def parse(self, src):
        plugins = ['def_list', 'footnotes']
        if have_pygments:
            plugins.append('codehilite(css_class=highlight)')
        return m.markdown(src, plugins)
