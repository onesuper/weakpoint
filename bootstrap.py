

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
    <link rel="stylesheet" href="theme/'''

content += theme

content += '''">
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
	<div class="author">''' 

content += author

content += '''</div>
	<div class="email">'''
content += email

content += '''</div>
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
