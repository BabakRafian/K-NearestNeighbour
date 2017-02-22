'''
@Author: Babak Rafian
This program finds and reports the k number of closest neighbour for each data point in Iris.csv
'''
import pandas as pd
import sys
import math

trainData = pd.read_csv('data/Iris.csv')
testData = pd.read_csv('data/Iris_Test.csv')
k = int(sys.argv[1])

# Using eucladian distance formula calculates the distance between
def diSim(p,q):
    sLength=p.sepal_length - q.sepal_length
    sWidth= p.sepal_width - q.sepal_width
    pLength=p.petal_length - q.petal_length
    pWidth = p.petal_width - q.petal_width

    eucladianDist = math.sqrt(math.pow(sLength,2)+math.pow(sWidth,2)+math.pow(pLength,2)+math.pow(pWidth,2))
    return eucladianDist

def predict(list):
    setosaCount=0
    versicolorCount=0
    virginicaCount=0
    #print(list[0][0][4])
    for i in range(k):
        if list[i][0][4]=='Iris-setosa':
            setosaCount+=1
        elif list[i][0][4]=='Iris-versicolor':
            versicolorCount+=1
        elif list[i][0][4]=='Iris-virginica':
            virginicaCount+=1
    answer = max(setosaCount,versicolorCount,virginicaCount)
    #print('Answer is: {0}'.format(answer))
    #print('setosa is: {0}'.format(setosaCount))
    #print('versicolor is: {0}'.format(versicolorCount))
    #print('virginica: {0}'.format(virginicaCount))
    prediction =''
    if answer == setosaCount:
        prediction = 'Iris-setosa'
    elif answer == versicolorCount:
        prediction = 'Iris-versicolor'
    elif answer == virginicaCount:
        prediction= 'Iris-virginica'
    return prediction

sys.stdout.write("Transaction ID  Actual Class  Predicted Class  Posterior Probability")

dataCount= 0
errorCount=0
print
for i in range(testData.__len__()):
    dataCount+=1
    p = testData.iloc[i]
    list = []
    for j in range(trainData.__len__()):
        q= trainData.iloc[j]
        #if i!=j: #makes sure that it is not the same data point
        dist = diSim(p,q)
        tupl = (q, dist)
        if len(list) <= k:
            list.append(tupl)
        else:
            for x in range(k):
                if dist < list[x][1] and dist>0:# take care of duplicates
                    del list[x]
                    list.append(tupl)
                    break
    prediction = predict(list)
    if prediction != p[4]:
        errorCount +=1
    sys.stdout.write('\t{0}\t{1}'.format(dataCount, p[4]))
    print('\t{0}\t\t'.format(prediction))

print('Total data: {0}'.format(dataCount))
print('Error Count: {0}'.format(errorCount))
    #for y in range(k):
        #sys.stdout.write("{0}  \t".format(i+1))
        #sys.stdout.write("\t{0}".format(list[y][0]+1))
        #sys.stdout.write("\t%.1f"%(round(list[y][1],1)))

    #print

