'''
Weak is more powerful
'''
from setuptools import find_packages, setup
from weakpoint import __version__



setup(
    name = 'weakpoint',
    version = str(__version__),
    author = 'onesuper',
    author_email = 'onesuperclark@gmail.com',
    url = 'http://blog.chengyichao.info/weakpoint',
    description = 'slideshow generator',
    long_description = __doc__,
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    entry_points = {
        'console_scripts': 'weakpoint = weakpoint.main:main'
    },
    install_requires = [
        'Jinja2',
        'misaka',
        'PyYAML',
    ],
    platforms = 'any',
    zip_safe = False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ]
)
