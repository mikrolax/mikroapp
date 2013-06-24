## mikroapp

Quickly build webapp based on bottle.py 

- includes bootstrap & JQuery
- mono or multi-app
- "desktop" app using Webkit


Example:
	  
	  import mikroapp.webapp
	  
	  #create 2 bottle app
	  tst_webapp1=webapp.Webapp()
	  tst_webapp2=webapp.Webapp()
	  
	  #create master app 
	  tst_applist=[('/test1/',tst_webapp1._app),('/test2/',tst_webapp2._app)] 	# list of (mountpoint, bootle app)
	  tst_master_webapp=webapp.MasterWebapp(tst_applist)
	  
	  #fill nav & content
	  tst_webapp1._model._nav=tstnav
	  tst_webapp1._model._content=''' I'm test 1 app!'''
	  tst_webapp2._model._nav=tstnav
	  tst_webapp2._model._content=''' I'm test 2 app!'''
	  tst_master_webapp._model._nav='''
	      <div class="navbar">
		<div class="navbar-inner">
		  <a class="brand" href="/">Home</a>
		  <ul class="nav">
		    <li><a href="/test1/">App1</a></li>
		    <li><a href="/test2/">App2</a></li>
		  </ul>
		</div>
	      </div>''' 

	  tst_master_webapp._model._content=''' I'm The master app! <br> Check <a href="/test1/">Test 1 app</a> and <a href="/test1/">Test 2 app</a>'''
	  
	  #run as webapp (bottle internal wsgi server)
	  tst_master_webapp.start()
	  
	  
	  #or run a desktop app (using webkit, require pyside)
          import mikroapp.desktop
          desktop.run(tst_master_webapp)   


TODO:

* authentification app
* doc

