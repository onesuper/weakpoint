
# What It Is?
----


## It is...

a static slideshow generator


* use **Markdown** to write your slides
* display your slides in Web browser


----

## It Is Not...

* a powerful slideshow creator
* WYSIWYG

----



# Quickstart
----

## Install

The recommended way to install WeakPoint is to use pip:


    $ pip install weakpoint



----



## Create a template
    
    
    $ weakpoint init ~/my-file

The default theme is "light" and you can specify it
with "-t" option:

    $ weakpoint init ~/my-file -t dark

----

##  Write & config your slides



* Open `~/my-file/slides.md` and write your slides in Markdown 
* Edit `~/my-file/config.yaml` to config your slides



----


## Generate the slideshow


    $ weakpoint gen


That's all! Now your slideshow is in `~/my-file/index.html`.


You can release it like static web pages.


----

# Misc

----

## Dependencies

The technologies behind WeakPoint:

* [Jinja2](http://jinja.pocoo.org/)
* [misaka](http://misaka.61924.nl/)
* [PyYAML](http://pyyaml.org/)
* [impress.js](http://bartaz.github.com/impress.js)

----

## How to Make a Theme


WeakPoint uses [Jinja2](http://jinja.pocoo.org/) as a templete engine.


You can get the content of slides by writing:


    {% for slide in slides %}
        <div class="content">{{ slide.content }}</div>
    {% endfor %}


----

# Thanks

