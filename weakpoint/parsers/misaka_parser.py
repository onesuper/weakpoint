import misaka

class Render(misaka.HtmlRenderer):
    pass

class Parser():

    def parse(self, markdown):
        html = misaka.Markdown(Render())
        return html.render(markdown) 
