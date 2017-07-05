"""
uWSGI API - Python decorators - with fallback for running outside uwsgi

Uwsgi offers a nice pyhton api in the form of decorators.
It's a shame that you can nolonger run your code outside of uwsgi.
This package implements fallbacks for the uwsgi decorators, that either do
nothing, or run the asynchronous stuff synchronously.

Beats import errors right?

this module provides fallbacks for the following uwsgi decorators::

    spool
    lock
    cron
    timer

usage, just import the decorators from uwsgidecoratorsfallback instead of
uwsgidecorators and your code will nolonger import error outside of uwsgi::

    from uwsgidecoratorsfallback import spool, lock, cron, timer

After that just use as intended, outside of uwsgi you get alternatives that
either do nothing or run the function synchronously.
"""
from setuptools import setup, find_packages


__version__ = "0.0.2"


setup(
    # package name in pypi
    name='uwsgidecorators-fallback',
    # extract version from module.
    version=__version__,
    description="uWSGI API - Python decorators - with fallback for running outside uwsgi",
    long_description=__doc__,
    classifiers=[],
    keywords='uwsgi',
    author='Lars van de Kerkhof',
    author_email='lars@permanentmarkers.nl',
    url='https://github.com/devopsconsulting/uwsgidecorators-fallback',
    license='GPL',
    # include all packages in the egg, except the test package.
    py_modules=['uwsgidecoratorsfallback'],
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=[
        'setuptools',
    ],
)
