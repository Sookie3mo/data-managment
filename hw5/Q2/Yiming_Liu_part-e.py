from pyspark import SparkContext
from operator import add
sc = SparkContext()
product = sc.textFile("product.txt")
product1 = product.map(lambda x : x.split(","))
product2 = product1.map(lambda t: (t[3],float(t[1])))
product3 = product2.reduceByKey(add)
product4  = product2.groupByKey().map(lambda x: (x[0],list(x[1])))
productNum = product4.mapValues(lambda l: len(l))
productAve = productNum.join(product3).map(lambda t: (t[0],t[1][1]/t[1][0]))
re = sorted(productAve.collect())
for item in re:
	print item[0],",",item[1]