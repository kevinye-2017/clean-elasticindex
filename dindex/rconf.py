#!/usr/bin/env python

import ConfigParser
import os

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
config_file_path=os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."),'delastic.conf')
def elastic_user():
	auth = []
	cfg = ConfigParser.ConfigParser()
	cfg.readfp(open(config_file_path))

	auth = [cfg.get('elasticsearch','elastic_user'),cfg.get('elasticsearch','elastic_password')]
	return tuple(auth)
