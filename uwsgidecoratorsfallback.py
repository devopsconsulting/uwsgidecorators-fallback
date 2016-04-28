class BaseDecorator(object):
    @property
    def spool(self):
        return self

    def __init__(self, f):
        self.f = f
    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

class BaseDecoratorWithArguments(object):

    def __init__(self, *args, **kwargs):
        # If there are decorator arguments, only the decorator arguments are passed to the constructor.
        # Not the to-be-decorated function.
        self.args = args
        self.kwargs = kwargs

    def __call__(self, f, *args, **kwargs):
        # If there are decorator arguments, __call__() is only called once, as part of the decoration process.
        # You can only give it a single argument, which is the function object.
        def wrapped_func(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapped_func

try:
    from uwsgidecorators import *
except ImportError:
    class lock(BaseDecorator):
        pass

    class spool(BaseDecorator):
        pass

    class cron(BaseDecoratorWithArguments):
        pass

    class timer(BaseDecoratorWithArguments):
        pass
