from pyspark import SparkContext
sc = SparkContext()
product = sc.textFile("product.txt")
company = sc.textFile("company.txt")
product1 = product.map(lambda x : x.split(","))
company1 = company.map(lambda x : x.split(","))
product2 = product1.map(lambda i: (i[3],i[0]))
company2 = company1.map(lambda i:(i[0],i[2]))
productCountry = product2.join(company2).map(lambda i: (i[1][0],i[1][1]))
re = sorted(productCountry.distinct().collect())
for item in re:
	print item[0],",",item[1]