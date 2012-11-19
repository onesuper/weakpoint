
from os import makedirs, remove, walk
from os import path as op
import shutil
import codecs

from weakpoint.utils import abspath



class Directory(object):
    def __init__(self, path):
        self.path = abspath(path)


    def cp(self, dest):
        dest = Directory(dest)
        
        if dest.exists:
            dest.rm()

        shutil.copytree(self.path, dest.path)

    def mk(self):
        if not self.exists:
            makedirs(self.path)

    def rm(self):
        if self.exists:
            shutil.rmtree(self.path)


    # protect the template files and dirs
    def empty(self):
        if self.exists:
            for root, dirs, files in walk(self.path):
                for d in dirs[:]:
                    if not d.startswith(('.', '_')):
                        Directory(abspath(root, d)).rm()
                    
                    dirs.remove(d)
                
                for f in files:
                    if not f.startswith(('.', '_')):
                        File(abspath(root, f)).rm()


    @property
    def exists(self):
        return op.exists(self.path) and op.isdir(self.path)



class File(object):
    def __init__(self, path, content=None):
        self.path = abspath(path)
        self.root = Directory(op.dirname(self.path))
        self.name, self.extension = op.splitext(op.basename(self.path))
        self.content = content


    def cp(self, dest):
        dest = File(dest)
        if self.path != dest.path:
            if not dest.root.exists:
                dest.root.mk()
            shutil.copyfile(self.path, dest.path)
    
    '''
    create the file with content
    '''
    def mk(self):
        if not self.exists:
            if not self.root.exists:
                self.root.mk()

            with codecs.open(self.path, mode='w', encoding='utf-8') as f:
                if self.content is None:
                    self.content = ''    
                f.write(self.content)


    def rm(self):
        if self.exists:
            remove(self.path)





    @property
    def exists(self):
        return op.exists(self.path) and op.isfile(self.path)


    
    
    @property
    def content(self):
        if self._content is None and self.exists:
            with codecs.open(self.path, mode='r', encoding='utf-8') as f:
                self._content = f.read()
        
        return self._content


    @content.setter
    def content(self, content):
        self._content = content

    def __str__(self):
        return unicode(self).encode('utf-8')
    
    def __unicode__(self):
        return self.path
