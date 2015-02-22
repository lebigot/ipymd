# -*- coding: utf-8 -*-

"""Utils"""

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------

import os
import os.path as op

from .six import exec_


#------------------------------------------------------------------------------
# Utils
#------------------------------------------------------------------------------

def _script_dir():
    return op.dirname(op.realpath(__file__))


def _test_file_path(filename):
    """Return the full path to an example filename in the 'examples'
    directory."""
    return op.realpath(op.join(_script_dir(), '../examples', filename))


def _exec_test_file(filename):
    """Return the 'output' object defined in a Python file."""
    path = _test_file_path(filename)
    with open(path, 'r') as f:
        contents = f.read()
    ns = {}
    exec_(contents, ns)
    return ns.get('output', None)
