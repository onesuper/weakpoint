


import misaka as m



class Render(m.HtmlRenderer):
    pass

class Parser():

    def parse(self, markdown):
        html = m.Markdown(Render())
        return html.render(markdown) 


