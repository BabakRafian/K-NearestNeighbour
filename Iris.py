'''
@Author: Babak Rafian
This program finds and reports the k number of closest neighbour for each data point in Iris.csv
'''
import pandas as pd
import sys
import math

data = pd.read_csv('data/Iris.csv')
k = int(sys.argv[1])


def diSim(p,q):
    sLength=p.sepal_length - q.sepal_length
    sWidth= p.sepal_width - q.sepal_width
    pLength=p.petal_length - q.petal_length
    pWidth = p.petal_width - q.petal_width

    eucladianDist = math.sqrt(math.pow(sLength,2)+math.pow(sWidth,2)+math.pow(pLength,2)+math.pow(pWidth,2))
    return eucladianDist


sys.stdout.write("Transaction ID  1st ID 1st Prox")
sys.stdout.write("\t\t2nd ID 2nd Prox")
sys.stdout.write("\t\t3rd ID 3rd Prox")
for i in range(4,k+1):
    sys.stdout.write("\t\t{0}th ID {0}th Prox".format(i))


print
for i in range(data.__len__()):
    p = data.iloc[i]
    list = []
    for j in range(data.__len__()):
        q= data.iloc[j]
        if i!=j: #makes sure that it is not the same data point
            dist = diSim(p,q)
            tupl = (j, dist)
            if len(list) <= k:
                list.append(tupl)
            else:
                for x in range(k):
                    if dist < list[x][1] and dist>0:# take care of duplicates
                        del list[x]
                        list.append(tupl)
                        break
    for y in range(k):
        sys.stdout.write("{0}  \t".format(i+1))
        sys.stdout.write("\t{0}".format(list[y][0]+1))
        sys.stdout.write("\t%.1f"%(round(list[y][1],1)))

    print

