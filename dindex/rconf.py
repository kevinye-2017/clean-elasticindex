#! /usr/bin/env python
import ConfigParser
import os

path = os.getcwd()
config_path = path + '/' + 'delastic.conf'
print config_path
def elastic_user():
	auth = []
	cfg = ConfigParser.ConfigParser()
	cfg.readfp(open(config_path))

	auth = [cfg.get('elasticsearch','elastic_user'),cfg.get('elasticsearch','elastic_password')]
	return tuple(auth)
