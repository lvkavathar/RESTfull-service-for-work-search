#!/usr/bin/python

import  sys
import mysql.connector
import simplejson as json
con = mysql.connector.connect(user='root',password='Venkat@123',host='127.0.0.1',database='project02')
cur = con.cursor()
query = ("SELECT Details FROM cat_work WHERE Details  LIKE '%Juv%'")
cur.execute(query)
for  Details in cur:
	print Details
	data = json.loads(Details)
cur.close()
con.close()








