'''
INF551 assignment 2
lax.json Query (Input: terminal or time or type; Output: the total numbers of passengers)
@Yiming Liu

This script supports searching keywords to be case-insensitive. For example, the input could be:
python lax_Yiming_Liu.py tBI ArriVal deParTURE

The way of getting lax.json is through "urllib".

language: python 2.7.10
'''


import json
import urllib
import sys

#get the data from lax.json
url = 'https://s3-us-west-1.amazonaws.com/inf551/lax.json'
page = urllib.urlopen(url)
data = page.read()
target = json.JSONDecoder().decode(data)
laxData =  target['data']


TerminalList = ['t1','t2','t3','t4','t5','t6','tbi']
TimeList = ['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
TypeList = ['arrival','departure']

op= sys.argv[1:]
terminal = []
time = []
type = []
# read the query options from IO and save them into 3 lists
i = 0

for i in range(0,len(op)):
    if op[i].lower() in TerminalList:
        terminal.append(op[i].lower())
    if op[i] in TimeList:
        time.append(op[i])
    if op[i].lower() in TypeList:
        type.append(op[i].capitalize())

# transfrom the terminal request from t1 to Terminal 1
terminalTran = []

f = {
        'tbi':'Tom Bradley International Terminal',
        't1':'Terminal 1',
        't2':'Terminal 2',
        't3':'Terminal 3',
        't4':'Terminal 4',
        't5':'Terminal 5',
        't6':'Terminal 6',
    }

for i in range (0,len(terminal)):
    if terminal[i] in f.keys():
        terminalTran.append(f.get(terminal[i]))

#check if any request list is empty
if terminalTran == []:
    terminalTran = ['Tom Bradley International Terminal','Terminal 1','Terminal 2','Terminal 3','Terminal 4','Terminal 5','Terminal 6']
if time == []:
    time = TimeList
if type == []:
    type = ['Arrival','Departure']

#search the laxData for the requests and calculate the total number of passengers
count = 0

for j in range(0,len(laxData)):
    if (laxData[j][10] in terminalTran) and (laxData[j][11] in type) and (laxData[j][9][0:4] in time):
        count = count + int(laxData[j][13])

print count





