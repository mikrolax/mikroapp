#!/usr/bin/env python
from distutils.core import setup
import mikroapp

setup(name='mikroapp',
      version=mikroapp.__version__,
      description=mikroapp.__description__,
      long_description=mikroapp.__long_description__,  
      author=mikroapp.__author__,
      author_email=mikroapp.__author_email__,
      license=mikroapp.__license__,
      url=mikroapp.__url__,
      packages=['mikroapp','mikroapp.external'],
      package_data={'mikroapp': ['static/*.js','static/*.css']},

     )
     
