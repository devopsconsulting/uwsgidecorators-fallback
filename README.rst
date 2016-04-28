uWSGI API - Python decorators - with fallback for running outside uwsgi
=======================================================================

Uwsgi offers a nice pyhton api in the form of decorators.
It's a shame that you can nolonger run your code outside of uwsgi.
This package implements fallbacks for the uwsgi decorators, that run the
asynchronous stuff synchronously.

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
