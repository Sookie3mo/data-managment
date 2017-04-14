from pyspark import SparkContext
sc = SparkContext()
person = sc.textFile("person.txt")
person1 = person.map(lambda x : x.split(","))
person2 = person1.map(lambda i: (i[0],i[1],i[2]))
personLA = person2.filter(lambda i: "los angeles" in i[2])
re = sorted(personLA.map(lambda i: i[0]).collect())
for i in range(0,len(re)):
	print re[i]


