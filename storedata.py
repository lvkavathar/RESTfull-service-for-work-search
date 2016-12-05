#!/usr/bin/python

import mysql.connector
import sys
import json
for line in sys.stdin:
	line = line.strip()
	words=line.split('\t')
	words[1]=words[1].replace("/works/","")
	words[2] = int(words[2])
	data = json.loads(words[04])
	title = data["title"]
	con = mysql.connector.connect(user='root',password='toor',host='127.0.0.1',database='project02')
	cur = con.cursor()
	arg = (words[1],words[2],words[3],words[4],title)
	query = ("INSERT INTO cat values (%s,%s,%s,%s,%s)")
	cur.execute(query, arg)
	con.commit()
	cur.close()
	con.close()

