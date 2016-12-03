#!/usr/bin/python

import mysql.connector
import sys
for line in sys.stdin:
	line = line.strip()
	words=line.split('\t')
	words[1]=words[1].replace("/works/","")
	words[2] = int(words[2])
	con = mysql.connector.connect(user='root',password='Venkat@123',host='127.0.0.1',database='project02')
	cur = con.cursor()
	arg = (words[1],words[2],words[3],words[4])
	query = ("INSERT INTO cat_work values (%s,%s,%s,%s)")
	cur.execute(query, arg)
	con.commit()
	cur.close()
	con.close()

