#!/usr/bin/env python

from dindex import del_index
from datetime import datetime, timedelta
import time

qi = del_index.QueryIndex(url='http://localhost:9200/_cat/indices?h=i,creation.date&format=json&pretty')
res = qi.queryindex()

list_delindex = []
list_del_watcher_index = []
#get x days ago index
def get_days_timestamp(x=0):
	d = datetime.now()
	dx = d - timedelta(days=x)
	timest = int(time.mktime(dx.timetuple()))
	return timest
def delete_xdays_index():
	t = get_days_timestamp(7)
	for l in res():
		ct = int(l['creation.date'][:10])
		if ct < t:
			if l['i'] == ".watches" or l['i'] == ".security-6" or l['i'] == ".kibana":
				pass
			else:
				list_delindex.append(l['i'])
		else:
			pass	

delete_xdays_index()

####delete index
for l in list_delindex:
	delete_index = del_index.QueryIndex(url='http://localhost:9200/' + l)
	response = delete_index.deleteindex()
	print response,l
