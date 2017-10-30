import numpy
import pandas as pd
from math import sqrt
import sys

def ghs(data1,data2):
	'''
	GHS - Geometric Histogram Separation
	----------------------------------------------
	Input:
	data1,data2 - The data samples - list or numpy.ndarray

	Output:
	BCA, BCL, GHS - The metrics - tuple of float64
	----------------------------------------------
	This function measures the Box Counting Area (BCA) and
	the Box Counting Linear (BCL) between data1 and data2.
	The GHS is measured as average of BCA square root and BCL.
	'''
	hist1, bins1 = numpy.histogram(data1)
	hist2, bins2 = numpy.histogram(data2)
	both = numpy.concatenate((bins1,bins2))
	# n is the number of bins (average between the number of both bins)
	n = len(both)/2
	rnge = (numpy.min(both),numpy.max(both))
	hist1, bins1 = numpy.histogram(data1,bins=n,range=rnge,normed=True)
	hist2, bins2 = numpy.histogram(data2,bins=n,range=rnge,normed=True)

	# since both histograms have same bins, dy is the intersection:
	dx = (rnge[1]-rnge[0])/n
	dy = numpy.minimum(hist1,hist2)

	# ao is the relative area  
	ao = numpy.sum(dy*dx)

	a_height = numpy.max(hist1)
	b_height = numpy.max(hist2)
	c_height = numpy.max(dy)

	bcl = (a_height+b_height-2.0*c_height)/(a_height+b_height)
	bca = 1.0 - (ao) / (2.0 - ao)
	ghs = ( sqrt(bca) + bcl ) / 2.0
	return bca,bcl,ghs

if __name__ == "__main__":
	'''
	Call structres:
		python ghs.py data1.csv data2.csv parameter
		python ghs.py data1.csv data2.csv		
 	'''
	d1 = pd.read_csv(sys.argv[1]).dropna()
	d2 = pd.read_csv(sys.argv[2]).dropna()
	if len(sys.argv)== 4:
		bca,bcl,ghs = ghs(d1[sys.argv[3]], d2[sys.argv[3]])
	else:
		bca,bcl,ghs = ghs(d1, d2)
	print("BCA:"+str(bca)+"\nBCL:"+str(bcl)+"\nGHS:"+str(ghs))
