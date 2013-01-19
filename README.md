
# WeakPoint (Version 0.2.3)


WeakPoint is a static slideshow generator.



* Use **Markdown** to write your slides
* Display your slides in Web browser
* NOT a powerful slideshow authering tool
* NOT WYSIWYG


## DEMO


[WeakPoint: Weak is more powerful](http://blog.chengyichao.info/weakpoint/#/step-1)



## Install

The recommended way to install WeakPoint is to use pip:


    $ pip install weakpoint


Create a template:
    
    
    $ weakpoint init ~/my-file

The default theme is "light" and you can specify it with "-t" option:

    $ weakpoint init ~/my-file -t dark


Generate the slideshow:


    $ weakpoint gen


## Dependencies


* [Jinja2](http://jinja.pocoo.org/)
* [misaka](http://misaka.61924.nl/)
* [Python-Markdown](http://packages.python.org/Markdown/)
* [PyYAML](http://pyyaml.org/)
* [impress.js](http://bartaz.github.com/impress.js)
* [jmpress.js](https://github.com/shama/jmpress.js/)



## Contributors


Michael Tiller
