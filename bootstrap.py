

import yaml
f = open('_config.yaml')
config = yaml.load(f)
f.close()
filename = config['filename']
theme = config['theme']
title = config['meta']['title']
subtitle = config['meta']['subtitle']
author = config['meta']['author']
email = config['meta']['email']
font_1 = config['google-font']['font1']
font_2 = config['google-font']['font2']

import time

fslide = open('index.html', 'w')
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

if font_1:
    content += '''
    <link href='http://fonts.googleapis.com/css?family='''
    content += font_1
    content += '''' rel='stylesheet' type='text/css'>
'''

if font_2:
    content += '''
    <link href='http://fonts.googleapis.com/css?family='''
    content += font_2
    content += '''' rel='stylesheet' type='text/css'>
'''

content +='''    
    <link rel="stylesheet" href="theme/'''

content += theme

content += '''.css">
  </head>
  <body>
    <div class="container">
    <section>
    
	<div class="title">''' 

content += title

content += '''</div>
	<div class="subtitle">'''
content += subtitle

content += '''</div>
    <div class="meta">
	<div class="author">''' 
content += author

content += '''</div>
    <div class="date">'''
content += time.strftime("%Y-%m-%d", time.localtime())

content += '''</div>
	<div class="email">'''
content += email

content += '''</div>
     <div class="theme">Powered by '''
content += theme


content += ''' theme</div></div>
    </section>
'''

# Markdown Starts

import markdown

fmd = open(filename)
text = fmd.read()
html = markdown.markdown(text)

import re
p = re.compile(r'<hr />')
slices = p.split(html)
for one in slices:
    content += '''
    <section>'''
    content += one
    content += '''
    </section>'''

# Markdown Ends


content += '''
    </div>
    <script src="core/weakpoint.js"></script>
  </body>
</html>
'''

fslide.write(content)
fslide.close()
