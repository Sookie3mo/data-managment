from pyspark import SparkContext
sc = SparkContext()
purchase = sc.textFile("purchase.txt")
product = sc.textFile("product.txt")
purchase1 = purchase.map(lambda x : x.split(","))
product1 = product.map(lambda x : x.split(","))
purchase2 = purchase1.map(lambda i:(i[3],i[1]))
product2 = product1.map(lambda i: (i[0],i[2]))
seller = product2.join(purchase2)
phoneseller = seller.filter(lambda i: "cell phone" in i[1][0]).map(lambda i: i[1][1])
laptopseller = seller.filter(lambda i: "laptop" in i[1][0]).map(lambda i: i[1][1])
re = sorted(laptopseller.subtract(phoneseller).collect())
for i in range(0,len(re)):
	print re[i]
