from matplotlib import pyplot as plt
from pandas import Series, DataFrame

def pieChart(dlist, explode, labels, title):
	plt.pie(dlist, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
	plt.axis('equal')
	plt.title('Parameter Comparison of '+title)
	plt.show()

def barChart(indices, dlist, ticklist, Xlabel, Ylabel, Title):
	bar_width = 0.4
	opacity = 0.6
	plt.bar(indices, dlist, bar_width, alpha=opacity, color='g')
	plt.xlabel(Xlabel)
	plt.ylabel(Ylabel)
	plt.title(Title)
	plt.xticks(indices, ticklist, rotation=60)
	plt.tight_layout()
	plt.show()

def barChartComp(ddict, key, indices, clist):
	newdict = {}
	for key,value in ddict[key].items():
		newdict[key]=value
	df = DataFrame(newdict)
	df.index = indices
	df = df.T
	for i in df.columns:
		if i not in clist:
			del df[i]
	df.plot(kind='bar')
	plt.show()
