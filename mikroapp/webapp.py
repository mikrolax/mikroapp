#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__='sebastien stang'
__author_email__='seb@mikrolax.me'
__license__="""Copyright (C) 2013 Sebastien Stang
 
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
 
""" simple webapp based on bottle.py  """

from string import Template
import os.path
import sys
from external.bottle import Bottle,route,static_file,error,request,response #,view?
 
def _we_are_frozen(): 
    return hasattr(sys, "frozen") 
def _module_path(): 
    if _we_are_frozen(): 
        return os.path.dirname(unicode(sys.executable, sys.getfilesystemencoding( ))) 
    return os.path.dirname(unicode(__file__, sys.getfilesystemencoding( ))) 
    
   
class _Model(object):
  def __init__(self):
    print 'init model'
    #use standard python $ ? or bottle {{ script }}! 
    self._content='''<h1>Hello!</h1><hr>'''
    
    self._footer='''
        <footer>
          <div class="container">
            <hr>
            <center> &copy 2013  | made with love by <a href="http://mikrolax.me"> mikrolax.me </a>  </center>                                                 
          </div>
      </footer>
    '''
    self._head='''
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="home simple app">
        <meta name="author" content="mikrolax">

        <link href="_static/style.min.css" rel="stylesheet">
    '''
  
    self._nav='''
      <div class="navbar">
        <div class="navbar-inner">
          <a class="brand" href="/">Home</a>
          <ul class="nav">
         <!--   <li><a href="/some_app/">some_app</a></li>
            <li><a href="/app2/">app2</a></li>  -->
          </ul>
        </div>
      </div>''' 
  
    self._script=''' 
            <script src="_static/script.min.js"></script>
            '''
  
    self._layout='''<!DOCTYPE html>
          <html>
          <head>
            $head
          </head>
          
          <body>
          
            <div class="container">
            $nav
            <div id="content">  $content </div>
            </div>
            
            $footer
            $script
            
          </body>
          </html>'''

    
  def _getLayout(self):
    print 'get layout'
    d=dict(head=self._head,nav=self._nav,content=self._content,footer=self._footer,script=self._script)
    return Template(self._layout).substitute(d)
    

class Webapp(object):
  def __init__(self,host='localhost',port=8000):
    print 'init Webapp'
    self._host = host
    self._port = port
    self._model= _Model()
    self._app  = Bottle()
    self._route()
    self._root=_module_path() # add static_path?
    
  #def setRoot(self,path):
  #  self.root=path
  
  def _route(self):
    self._app.route('/', method="GET", callback=self._index)
    self._app.route('/_static/<filepath:path>', callback=self._serve_static)

  def start(self):
    print 'start %s' %self._app
    self._app.run(host=self._host, port=self._port,debug=True)   
 
  def _index(self):
    print 'Webapp:_index %s for bottle %s' %(self._model._content,self._app)
    return self._model._getLayout()
  
  def _serve_static(self,filepath):
    print 'Webapp:_serve_static %s' %filepath
    return static_file(filepath, root=os.path.join(os.path.abspath(self._root),'static')) #should be able to serve anywhere...
   
  @error(404) # ??
  def error404(error):
    return 'Nothing here, sorry' 


class MasterWebapp(Webapp):
  #applist =[(bottle_app1,mount_point1),(bottle_app2,mount_point2)]
  def __init__(self,applist): 
    super(MasterWebapp, self).__init__() 
    self.load(applist)
    
  def load(self,applist):
    for app in applist:
      mountpoint,subapp=app
      self._app.mount(prefix=mountpoint,app=subapp)
      self._model._content='''Master Webapp!'''      
      self._model._nav='''
      <div class="navbar">
        <div class="navbar-inner">
          <a class="brand" href="#">Mikrotools</a>
          <ul class="nav">
            <li><a href="/minify/">webminify</a></li>
            <li><a href="/rss/">ezRSS</a></li>
          </ul>
        </div>
      </div>'''

