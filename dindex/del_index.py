#!/usr/bin/env python

import requests
import json
import rconf

class QueryIndex(object):
	def __init__(self, status=None, index=None, uuid=None, rep=None, 
			pri=None, docs_deleted=None, pri_store_size=None, 
			health=None, store_size=None, docs_count=None, url=None):
		self.status = status
        	self.index = index
        	self.uuid = uuid
        	self.rep = rep
        	self.pri = pri
        	self.docs_deleted = docs_deleted
        	self.pri_store_size = pri_store_size
        	self.health = health
        	self.store_size = store_size
        	self.docs_count = docs_count
        	self.url = url

	def queryindex(self):
		res = requests.get(self.url,auth=rconf.elastic_user())
	 	return res.json
	def deleteindex(self):
		res = requests.delete(self.url,auth=rconf.elastic_user())
		return res
