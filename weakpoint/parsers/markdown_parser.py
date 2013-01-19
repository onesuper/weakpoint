import markdown as m


# If you have pygments installed, WeakPoint will highlight
# the code automatically. Actually, I was considering to make
# pygements as a dependency of WeakPoint and let user config 
# whether to highlight the code in config.xml

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
