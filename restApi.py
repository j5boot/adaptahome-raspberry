#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import json
from gpioes import Gpioes

controladora = Gpioes()

urls = (
	'/setValue/', 		'SetValue',
	'/getValue/', 		'GetValue'
)

print "datos cargados"

app = web.application(urls, globals())



class SetValue :
	def OPTIONS (self) :
		web.header('Access-Control-Allow-Origin','*')
		web.header('Access-Control-Allow-Credentials','true')
		web.header('Access-Control-Allow-Headers','Origin, X-Requested-With, Content-Type, Accept')
		web.header("Access-Control-Allow-Methods","GET,POST,OPTIONS,PUT,DELETE")
	def POST (self) :
		web.header("Content-Type","application/json; charset=utf-8")
		web.header('Access-Control-Allow-Origin',      '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		web.header('Access-Control-Allow-Headers', 
			'Origin, X-Requested-With, Content-Type, Accept')
		web.header("Access-Control-Allow-Methods","GET,POST,OPTIONS,PUT,DELETE")
		jobj = json.loads(web.data())
		dicc = controladora.setValue(jobj)
		print dicc
		return json.dumps(dicc)

class GetValue :
	def GET (self) :
		web.header("Content-Type","application/json; charset=utf-8")
		web.header('Access-Control-Allow-Origin',      '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		web.header('Access-Control-Allow-Headers', 
			'Origin, X-Requested-With, Content-Type, Accept')
		web.header("Access-Control-Allow-Methods", "GET, PUT, POST")
		dicc = controladora.getValue()
		return json.dumps(dicc)		

if __name__ == "__main__":
	app.run()
