#!/usr/bin/python

import mysql.connector
import os,sys
from flask import Flask, jsonify, render_template, request, abort, make_response
from flask import Response
import simplejson as json
import json
app = Flask(__name__)

@app.route('/search/<string:title>',methods=['GET','POST'])
def search(title) :
	con = mysql.connector.connect(user='root',password='Venkat@123',host='127.0.0.1',database='project02')
	cur = con.cursor()
	query = ("SELECT Details FROM cat_work WHERE Details  LIKE %s")
	cur.execute(query,("%" + title + "%",))
	for  Details in cur:
		return Details
	cur.close()
	con.close()
@app.route('/work/<string:id>',methods=['GET','POST'])
def work(id) :
        con = mysql.connector.connect(user='root',password='Venkat@123',host='127.0.0.1',database='project02')
        cur = con.cursor()
        query = ("SELECT Details FROM cat_work WHERE Object_Id = %s")
        cur.execute(query,(id,))
        for  Details in cur:
                return Details
        cur.close()
        con.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="80")







