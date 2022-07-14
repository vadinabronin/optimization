import os
from .func import function


__version__ = '1.0.0'
__licence__ = 'vadim_abronin'
__author__ = 'vadim_abronin'

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

__all__ = ['function']
