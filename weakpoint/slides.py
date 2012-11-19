
import re


class Slide(object):
    def __init__(self, **arg):
        self.no = arg['no']
        self.content = arg['content']
        self.x = arg['x']
        self.rotate = arg['rotate']

class Navi(object):
    def __init__(self, **arg):
        self.title = arg['title']
        self.no = arg['no']


class Slides(object):

    def  __init__(self, content):
        slides = re.compile(r'<hr>').split(content)
        self.slides = []
        self.navi = []
        rotate = 0
        for i in range(len(slides)):
            content = slides[i]

            # choose the first <h1> to be title and add it to navi
            titles = re.compile(r'<h1>.*?<\/h1>').findall(content)
            if titles:
                titlestring = titles[0].replace('<h1>', '')
                titlestring = titlestring.replace('</h1>', '')
                self.navi.append(Navi(title=titlestring, no=i+2))
                rotate += 90

            self.slides.append(Slide(no=i+2, content=content, x=i*1200, rotate=rotate))
            
        

        
            
            
