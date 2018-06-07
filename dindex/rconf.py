import ConfigParser
import sys

sys.path.append('..')
def elastic_user():
	auth = []
	cfg = ConfigParser.ConfigParser()
	cfg.read('delastic.conf')

	auth = [cfg.get('elasticsearch','elastic_user'),cfg.get('elasticsearch','elastic_password')]
	return tuple(auth)
