# WeakPoint: Create Slideshows in a Weaker Way

touch the [demo](http://blog.chengyichao.info/weakpoint/)


--------------------
version 1.2

* popup on the front page
* gravatar 

---------------
version 1.1

Social information(twiter/email/github)

---------------
version 1.0

* implements the slide effect
* cancel the the actions inside one slide
* cancel the mouse event
* redesign the layouts 

------------
version 0.11

Support LaTeX using MathJax

---------------

version 0.1(demo)

* internal movements
* navigation

--------------------



## It is Not

A powerful WYSIWG slideshow editor  


## Features


* Create a slideshow in Markdown
* Display it in web browser
* Themed by CSS
* Hosted on Github Pages


## Advantages

* Markdown is Awesome, so it's awesome, too
* As compatible as web page
* The content and view are sperated!
* If you can write, then you can make slideshow
* A new way to share slideshows, like websites

## Get Started

### 1. Clone the repository


<pre>
$ git clone https://github.com/onesuper/weakpoint TESTNAME
$ cd TESTNAME
$ git remote set-url origin git@github.com: USERNAME/TESTNAME.git
$ git push origin master
 </pre>
 
 
###  2.Config your slideshow in 'config.yaml'

<pre>
filename: weakpoint.md
theme: clean
googlefonts:Eater|Smart
meta:
  title: WeakPoint
  subtitle: Weak is more powerful
  author: onesuper
  email: onesuperclark
  ...
</pre>

### 3. write your own Mardown file 

<pre>
## It is a headline
* first
* second
* third
----
## Yet another headline
It is a lovely day.


Isn't it?
----
</pre>

### 3. bootstrap it by typing 'python bootstrap.py'

<pre>
$ python bootstrap.py
</pre>

### 4. deploy your slideshow to Github Page

<pre>
$ cd TESTNAME
$ git checkout -- orphan gh-pages
$ git add .
$ git commit -m 'First page commit for my slides'
$ git push origin gh-pages
</pre>

## Libraries

1. [PyYAML](http://pyyaml.org/)
2. [Markdown in Python](http://freewisdom.org/projects/python-markdown/)
3. [bxslider](http://bxslider.com)
