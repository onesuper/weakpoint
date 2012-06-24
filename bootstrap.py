# create a slide show quickly

import yaml
import markdown
import re
import time
import codecs

# import the configs
f = open('_config.yaml')
config = yaml.load(f)
f.close()
filename = config['filename']
theme = config['theme']
title = config['meta']['title']
subtitle = config['meta']['subtitle']
author = config['meta']['author']
email = config['meta']['email']
organization = config['meta']['organization']
googlefonts = config['googlefonts']
navi_enable = config['slide']['navi']
ribbon_enable = config['slide']['ribbon']

# read the markdown file and convert it to html
fmd = codecs.open(filename, mode="r", encoding="utf8")
text = fmd.read()
html = markdown.markdown(text)



content = '''
<!doctype html>  
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>''' 
content += title

content += '''</title>
    <link rel="stylesheet" href="core/weakpoint.css">
'''
# set up fonts

if googlefonts:
    content += '''
    <link href='http://fonts.googleapis.com/css?family='''
    content += googlefonts
    content += '''' rel='stylesheet' type='text/css'>
'''


# set up theme

content +='''    
    <link rel="stylesheet" href="theme/'''

content += theme

content += '''.css">
  </head>
  <body>'''


# navi bar

if navi_enable:
    content += '''
    <div class="navi">'''
    # get the headlines ready 
    headlines = re.compile(r'<h1>.+</h1>').findall(html)
    if headlines: 
        for i in range(len(headlines)):
            headlines[i] = headlines[i][4:-5]
        for h in headlines:
            content += ("<span>" + h + "</span>")
    content += '''
    </div>'''

content += '''
    <div class="container">
    <section>
	<div class="title">''' 

# set up the first slide with meta infomations
 
content += title

content += '''</div>
	<div class="subtitle">'''
content += subtitle

content += '''</div>
    <div class="meta">
	<div class="author">''' 
content += author


if email:
    content += '''</div>
	<div class="email">'''
    content += email

if organization:
    content += '''</div>
    <div class="organization">'''
    content += organization
    
content += '''</div>
    <div class="date">'''
content += time.strftime("%Y-%m-%d", time.localtime())


content += '''</div>
     <div class="theme">'''
content += theme


content += ''' theme</div></div>
    </section>
'''

# Markdown Starts

# a little trick here

html = html.replace('<h2>', '<hr />\n<h2>')
html = html.replace('<h1>', '<hr />\n<h1>')
p = re.compile(r'<hr />')
slides = p.split(html)
slides.remove('')
for one in slides:
    content += '''
    <section>'''
    content += one
    content += '''
    </section>'''

# Markdown Ends


content += '''
    <section>
      <div class="thanks">Thanks!</div>
    </section>
    </div>
    <script src="core/weakpoint.js"></script>
    <script>weakpoint.init()</script>
    '''

if ribbon_enable:
    content += '''
    <a href="https://github.com/onesuper/weakpoint"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png" alt="Fork me on GitHub"></a>'''

    content += '''
    </body>
</html>'''


fslide = codecs.open('index.html', mode="w", encoding="utf8")
fslide.write(content)
fslide.close()
