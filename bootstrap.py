# author: onesuper
# under MIT license

import yaml
import markdown
import re
import time
import codecs

# ===========import the configs========
f = open('config.yaml')
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
latex_enable = config['slide']['latex']
mode = config['slide']['mode']

# =======read the markdown file and convert it to html ========
fmd = codecs.open(filename, mode="r", encoding="utf8")
text = fmd.read()
html = markdown.markdown(text)


# ==================html starts===============
content = '''
<!doctype html>  
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>''' 
content += title
content += '''</title>
    <link rel="stylesheet" href="core/weakpoint.css">
    <script src="third/jquery.js" type="text/javascript"></script>
    <script src="third/jquery.bxSlider.min.js" type="text/javascript"></script>
    <script type="text/javascript">
  $(document).ready(function(){
    bxslide = $('#slider1').bxSlider({
        infiniteLoop: false,
        controls: false,
        mode : "'''
# -------------------------mode-------------------
content += mode + '",'
content += '''
        });
});
    </script>'''

# ====================latex======================
if latex_enable:
    content += '''
     <script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [ ['$','$'], ["\\(","\\)"] ],processEscapes: true}});</script>
    <script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']}});</script>
    <script type="text/x-mathjax-config">MathJax.Hub.Queue(function() {var all = MathJax.Hub.getAllJax(), i;for(i=0; i < all.length; i += 1) {all[i].SourceElement().parentNode.className += ' has-jax';}});</script>
    <script type="text/javascript"src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>'''
# ends

# ===================google fonts==================
if googlefonts:
    content += '''
    <link href='http://fonts.googleapis.com/css?family='''
    content += googlefonts
    content += '''' rel='stylesheet' type='text/css'>'''


# ===================theme=====================
if theme:
    content +='''    
    <link rel="stylesheet" href="theme/'''
    content += theme
    content += '''.css">
  </head>
  <body>'''


# =======================navi====================
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
    <div id="wrapper">
    <div id="slider1">
    <div class="paper"><div class="paper-container">
	    <div class="title">''' 

# =====================front page===========================

# ------------------------------------- title-----------------------------------------
content += title
content += '''</div>
	    <div class="subtitle">'''
    
# ------------------------------------- subtile--------------------------------------
content += subtitle
content += '''</div>
        <div class="meta">
	         <div class="author">''' 
    
# -------------------------------------author---------------------------------------
content += author

# -------------------------------------email-----------------------------------------
if email:
    content += '''</div>
	          <div class="email">'''
    content += email
    
# -------------------------------------organization---------------------------------
if organization:
    content += '''</div>
              <div class="organization">'''
    content += organization
    
# -------------------------------------time-----------------------------------------
content += '''</div>
              <div class="date">'''
content += time.strftime("%Y-%m-%d", time.localtime())
content += '''</div>
              <div class="theme">'''
     
# -------------------------------------theme----------------------------------------
content += theme
content += ''' theme</div></div>
    </div></div>'''

# ==================trick here=================
html = html.replace('<h2>', '<hr />\n<h2>')
html = html.replace('<h1>', '<hr />\n<h1>')
p = re.compile(r'<hr />')
slides = p.split(html)
slides.remove('')

# ===================slides====================
for one in slides:
    content += '''






    
    
    <div class="paper"><div class="paper-container">
    <!-- =========================SLIDE==========================-->
    '''
    content += one
    content += '''
    <!-- ====================================================== -->
    </div></div>'''

    
# ===================end page & js===================
content += '''
    <div class="paper"><div class="paper-container">
      <div class="thanks">Thanks!</div></div>
    </div>
    </div>
    </div>
    <script type="text/javascript" src="core/weakpoint.js"></script>
    <script type="text/javascript">var weakpoint = new weakPoint(); weakpoint.init();</script>'''

    

    
# ====================ribbon====================
if ribbon_enable:
    content += '''
    <a href="https://github.com/onesuper/weakpoint"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_white_ffffff.png" alt="Fork me on GitHub"></a>'''

    
# ==================html ends=====================
content += '''
    </body>
</html>'''


# =================write file=====================
fslide = codecs.open('index.html', mode="w", encoding="utf8")
fslide.write(content)
fslide.close()
