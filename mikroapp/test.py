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

import unittest
import subprocess


'''tst_webapp1=None
tst_webapp2=None
tst_master_webapp=None
tst_applist=None
'''
tstnav='''
      <div class="navbar">
        <div class="navbar-inner">
          <a class="brand" href="/">Home</a>
          <ul class="nav">
            <li><a href="/test1/">App1</a></li>
            <li><a href="/test2/">App2</a></li>
          </ul>
        </div>
      </div>''' 
      
def setUpModule():
  global tst_webapp1
  global tst_webapp2
  global tst_master_webapp
  global tst_applist
  import webapp
  tst_webapp1=webapp.Webapp()
  tst_webapp2=webapp.Webapp()
  tst_applist=[('/test1/',tst_webapp1._app),('/test2/',tst_webapp2._app)]
  tst_master_webapp=webapp.MasterWebapp(tst_applist)
  
  tst_webapp1._model._nav=tstnav
  tst_webapp1._model._content=''' I'm test 1 app!'''
  tst_webapp2._model._nav=tstnav
  tst_webapp2._model._content=''' I'm test 2 app!'''
  tst_master_webapp._model._nav=tstnav
  tst_master_webapp._model._content=''' I'm The master app! <br> Check <a href="/test1/">Test 1 app</a> and <a href="/test1/">Test 2 app</a>'''

def tearDownModule():
  pass  


class DesktopTest(unittest.TestCase):
  #def test_module_desktop_mono_app(self):
  #  import desktop
  #  desktop.run(tst_webapp1)
  
  def test_module_desktop_multi_app(self):
    import desktop
    desktop.run(tst_master_webapp)   

class MikroAppTest(unittest.TestCase):
  """ Base class for mikroapp testing """    
  def test_module_webapp_class_webapp(self):
    tst_webapp1.start()

  def test_module_webapp_class_masterwebapp(self):
    tst_master_webapp.start()

def suite():
  suite = unittest.TestLoader().loadTestsFromTestCase(MikroAppTest)
  suite2=unittest.TestLoader().loadTestsFromTestCase(DesktopTest)
  suite.addTest(suite2)
  return suite
 
def run():
  test_suite=suite()
  unittest.TextTestRunner(verbosity = 2).run(test_suite)
  

if __name__ == '__main__':
  run()
