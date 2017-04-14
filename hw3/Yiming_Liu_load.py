#@Yiming Liu
#inf551 assignment3
#input : python Yiming_Liu_load.py "data" (if directory "data" is under the same path of load.py)

import json
import mysql.connector
import glob
import sys
#glob get content under a directory

#connect sql
cnx = mysql.connector.connect(user='inf551', password='inf551', host='127.0.0.1', database='inf551')
cursor = cnx.cursor()

path = sys.argv[1]
jsonFilenames = glob.glob(path + "/*.json")
dataCandidate = []
dictCandidate = {}
#get candidate data
for filename in jsonFilenames:
    jsonFile = open(filename, 'r')
    data = json.load(jsonFile)
    dictCandidate.update(data["candidates"])
    print dictCandidate
    year = filename[5:9]
    deName = str(dictCandidate['democrat'])
    reName = str(dictCandidate['republican'])
    dataCandidate.append([year,deName,reName])
    print year
    print deName
    print reName
    print dataCandidate
    jsonFile.close()
#insert into candidate table, executemany is more efficient than excute several loops
loadCandidate = "INSERT INTO Candidate VALUES (%s,%s,%s)"
cursor.executemany(loadCandidate,dataCandidate)


dataVote = []
#get vote data
for filename in jsonFilenames:
    jsonFile = open(filename, 'r')
    data = json.load(jsonFile)
    data= data['votes']
    stateListU = data.keys()
    voteList = []
    for i in range(0,len(stateListU)):
        if len(data[stateListU[i]].values()) == 2:
            voteList.append([data[stateListU[i]].values()[1]['democrat'],data[stateListU[i]].values()[1]['republican'],data[stateListU[i]].values()[0]['democrat'],data[stateListU[i]].values()[0]['republican']])
        else:
            voteList.append([data[stateListU[i]].values()[0]['democrat'],data[stateListU[i]].values()[0]['republican'],0,0])
    #transform unicode to string
    stateList = []
    for item in stateListU:
        item = str(item)
        stateList.append(item)
    #merge year, state, vote counts into one list
    voteItem = [filename[5:9]]
    voteTable = []
    for i in range(0, len(stateList)):
        voteItem = [filename[5:9]]
        voteItem.append(stateList[i])
        voteItem.extend(voteList[i])
        voteTable.append(voteItem)
    dataVote.extend(voteTable)

#insert into vote table
loadVote = "INSERT INTO Vote VALUES (%s,%s,%s,%s,%s,%s)"
cursor.executemany(loadVote,dataVote)

cnx.commit()
cursor.close()
cnx.close()






