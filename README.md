# WeakPoint [DEMO]: Create Slideshows in a Weaker Way

touch the [demo](http://blog.chengyichao.info/weakpoint/)

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
* The content and view are sperated! If you can write, then you can make slideshow
* A new way to share slideshows, like websites

## Three Setups and You Have a Slideshow
 
###  1.Config your slideshow in '_config.yaml'

<pre>
filename: weakpoint.md
theme: clean
google-font:
   font1: Eater
   font2:
meta:
  title: WeakPoint
  subtitle: Weak is more powerful
  author: onesuper
  email: onesuperclark
</pre>

### 2. write your own Mardown file 

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

### 3. deploy it by typing 'python bootstrap.py'

<pre>
> python bootstrap.py
</pre>

## Libraries

1. [PyYAML](http://pyyaml.org/)
2. [Markdown in Python](http://freewisdom.org/projects/python-markdown/)
