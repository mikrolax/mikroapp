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

import sys 
import time 
from PySide import QtCore,QtGui,QtWebKit 

import webapp 
  
class WebThread(QtCore.QThread): 
  def __init__(self,app,host='localhost',port=8000): 
    super(WebThread, self).__init__()     
    if isinstance(app, webapp.Webapp) or issubclass(app,webapp.Webapp):
      self.app=app
    
  def run(self):     
    self.app.start() 
          
  
class Window(QtWebKit.QWebView): 
  def __init__(self,app,host='localhost',port=8000,title=''): 
    super(Window, self).__init__()   
    self.host=host
    self.port=port
    self.title=title
    self.thread=WebThread(app,host=self.host,port=self.port) 
    self.thread.start() 
    time.sleep(2)   
    self.init_ui() 
      
  def init_ui(self): 
    self.setWindowTitle(self.title)  
    url="http://%s:%s" %(self.host,self.port) 
    print  'load %s' %url     
    self.settings().setAttribute(QtWebKit.QWebSettings.LocalContentCanAccessRemoteUrls, True)  
    self.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True) 
    self.settings().setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True) 
    self.load(QtCore.QUrl(url)) 
    self.show()      
      

def run(app,host='localhost',port=8000,title=''):
  qt_app = QtGui.QApplication(sys.argv) 
  win=Window(app,host=host,port=port,title=title) 
  win.show() 
  sys.exit(qt_app.exec_()) 
  
  
'''   
if __name__ == '__main__':
  webapp=webapp.Webapp()
  run(webapp)
'''  