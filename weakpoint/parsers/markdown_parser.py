import markdown as m

try:
    import pygments
    have_pygments = True
except ImportError:
    have_pygments = False

class Parser():
    def parse(self, src):
        plugins = ['extra']
        pyg = 'codehilite(css_class=highlight,force_linenos=False)'
        if have_pygments:
            plugins.append(pyg)
        return m.markdown(src, plugins)
