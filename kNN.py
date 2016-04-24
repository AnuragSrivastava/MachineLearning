import numpy as np
import operator

def createDataset():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['Action', 'Action', 'Romantic', 'Romantic']
    return group, labels

def classify(inX, k):
    dataSet, labels = createDataset()
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDist = sqDiffMat.sum(axis=1)
    dist = sqDist ** 0.5
    sortedDist = dist.argsort()
    classCount = {}
    for i in range(k):
        votedLabel = labels[sortedDist[i]]
        classCount[votedLabel] = classCount.get(votedLabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter, reverse=True)
    return sortedClassCount[0][0]


print classify([1,2], 3)