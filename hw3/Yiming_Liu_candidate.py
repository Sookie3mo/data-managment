#@Yiming Liu
#inf551 assignment3
# input : python Yiming_Liu_candidate.py "year"
# The host has been changed to 127.0.0.1, so the script can run in local mysql

import mysql.connector
import sys
cnx = mysql.connector.connect(user='inf551', password='inf551', host='127.0.0.1', database='inf551')
cursor = cnx.cursor()
inputyear = sys.argv[1]

query = ("select democratName, republicanName from Candidate  where year = " + inputyear)
cursor.execute(query)
name = cursor.fetchall()
print "democrat:",name[0][0]
print "republican:",name[0][1]



