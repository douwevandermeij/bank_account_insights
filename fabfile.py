import sys

from django.conf import settings
from django.template.loader import render_to_string
from fabric.operations import local


def create_func(name):
    def f():
        settings.configure(TEMPLATE_DIRS=('.'))
        fh = open("geldzaken/settings.py", 'wb')
        fh.write(render_to_string("geldzaken/settings.py.dev", {
            'name': name
        }))
        fh.close()

    f.__name__ = name
    f.func_name = name
    return f


for layer in ["prd", "dev", "acc", "tst", "stg"]:
    setattr(sys.modules[__name__], layer, create_func(layer))

