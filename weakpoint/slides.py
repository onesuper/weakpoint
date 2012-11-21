
import re


class Slide(object):
    def __init__(self, **arg):
        self.no = arg['no']
        self.content = arg['content']
        self.chapter = arg['chapter'] 
        self.section = arg['section']


class Navi(object):
    def __init__(self, **arg):
        self.title = arg['title']
        self.no = arg['no']


class Slides(object):

    '''
    The slides no begins from 2!!!
    '''

    def  __init__(self, content):
        slides = re.compile(r'<hr>').split(content)
        self.slides = []  # a linear structure
        self.navi = [] # for navi bar

        chapter = -1
        section = -1   
        for i in range(len(slides)):

            # entering a new section
            section += 1

            content = slides[i]
            
            # choose the first <h1> to be title and add it to navi
            # and set it into 
            titles = re.compile(r'<h1>.*?<\/h1>').findall(content)
            if titles:
                # entering a new chapter
                chapter += 1
                section = 0

                titlestring = titles[0].replace('<h1>', '')
                titlestring = titlestring.replace('</h1>', '')
                self.navi.append(Navi(title=titlestring, no=i+2))

            # add silde
            self.slides.append(Slide(no=i+2, content=content,
                                     section=section, chapter=chapter))
                 
