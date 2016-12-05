#!/usr/bin/python

import mysql.connector
import os,sys
from flask import Flask, jsonify, render_template, request, abort, make_response
from flask import Response
import simplejson as json
import json
import requests
app = Flask(__name__)

@app.route('/search/<string:title>',methods=['GET','POST'])
def search(title) :
	con = mysql.connector.connect(user='root',password='toor',host='127.0.0.1',database='project02')
	cur = con.cursor()
	query = ("SELECT Details FROM cat WHERE title  LIKE %s")
	cur.execute(query,("%" + title + "%",))
	try:
	 os.remove("newfile1.txt")
	except OSError:
	 pass
	
	file = open("newfile1.txt", "w")
	for  Details in cur:
                file.write(Details[0].encode('utf8'))
		print Details[0]
	file.close()
        cur.close()
        con.close()        
	file = open("newfile1.txt", "r")
        return file.read().decode('utf8')	
	
@app.route('/work/<string:id>',methods=['GET','POST'])
def work(id) :
        con = mysql.connector.connect(user='root',password='toor',host='127.0.0.1',database='project02')
        cur = con.cursor()
        query = ("SELECT Details FROM cat WHERE Object_Id = %s")
        cur.execute(query,(id,))
	try:
         os.remove("newfile.txt")
        except OSError:
         pass
	file = open("newfile.txt", "w")
        for Details in cur:
		data = json.loads(Details[0])
		url = "https://openlibrary.org"+data["authors"][0]["author"]["key"] +".json"
  		response=requests.get(url)
  		result = json.loads(response.content)
		file.write(Details[0].encode('utf8'))
		file.write(result["name"].encode('utf8'))
		file.close()
        cur.close()
        con.close()
	file = open("newfile.txt", "r")
        return file.read().decode('utf8')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="80")







