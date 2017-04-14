#@Yiming Liu
#inf551 assignment3
# input : python Yiming_Liu_search.py "year" "name" "state"
# The host has been changed to 127.0.0.1, so the script can run in local mysql
import mysql.connector
import sys

inputYear = sys.argv[1]
inputName = sys.argv[2]
inputState = sys.argv[3]

cnx = mysql.connector.connect(user='inf551', password='inf551',host='127.0.0.1', database='inf551')
cursor = cnx.cursor()

checkDeRe =('SELECT EXISTS(SELECT * FROM Candidate WHERE year =' + inputYear + ' AND democratName = "' + inputName + '")')
cursor.execute(checkDeRe)
check = cursor.fetchall()

if check[0][0] == 1:
    searchDe = ("SELECT elecDemocrat, popDemocrat from Vote WHERE year = " + inputYear + " AND state = \"" + inputState+"\"")
    cursor.execute(searchDe)
    result = cursor.fetchall()

else:
    searchRe = ("SELECT elecRepublican, popRepublican from Vote WHERE year = " + inputYear + " AND state = \"" + inputState+"\"")
    cursor.execute(searchRe)
    result = cursor.fetchall()


print "EV:",result[0][0],";""PV:",result[0][1]
cursor.close()
cnx.close()

