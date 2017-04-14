from pyspark import SparkContext
sc = SparkContext()
person = sc.textFile("person.txt")
purchase = sc.textFile("purchase.txt")
person1 = person.map(lambda x : x.split(","))
purchase1 = purchase.map(lambda x : x.split(","))
person2 = person1.map(lambda i: (i[0],i[2]))
purchase2 = purchase1.map(lambda i:(i[0],i[1]))
personName = person2.join(purchase2).filter(lambda i: "los angeles" in i[1][0] and "john" in i[1][1])
re = sorted(personName.map(lambda i: i[0]).distinct().collect())
for i in range(0,len(re)):
	print re[i]