from sklearn import tree
from sklearn import ensemble
from sklearn import neighbors
from sklearn import neural_network

#[Height,Weight,Shoe Size]
X = [
    [181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
    [166, 65, 40], [190, 90, 47], [175, 65, 39], [177, 64, 39],
    [159, 55, 37], [171, 75, 42], [181, 85, 43]
]

# Labels 
Y = ['male', 'female', 'female', 'female', 'male', 'male', 
    'male', 'female', 'male', 'female', 'male']

# Declaration of Classfiers
# DecisionTreeClassifier
DecisionTreeClf = tree.DecisionTreeClassifier()
# DecisionTreeClassifier
RandomForestClf = ensemble.RandomForestClassifier()
# K-Nearest Neighbors Classfier
KNearestNeighborsClassifier = neighbors.KNeighborsClassifier()
# MLP Classfier
MLPClassfier = neural_network.MLPClassifier()


DecisionTreeClf = DecisionTreeClf.fit(X,Y)
RandomForestClf = RandomForestClf.fit(X,Y)
KNearestNeighborsClassifier = KNearestNeighborsClassifier.fit(X,Y)
MLPClassfier = MLPClassfier.fit(X,Y)

TestInput = [[190,90,48]]

DecisionTreeClfPredication = DecisionTreeClf.predict(TestInput)
RandomForestClfPredication = RandomForestClf.predict(TestInput)
KNearestNeighborsPrediction = KNearestNeighborsClassifier.predict(TestInput)
MLPClassfierPredication = MLPClassfier.predict(TestInput)

print('-------------'*4)
print('Decision Tree Prediction Result = ' + str(DecisionTreeClfPredication))
print('-------------'*4)
print('Random Forest Prediction Result =' + str(RandomForestClfPredication))
print('-------------'*4)
print('K-Nearest Neighbors Prediction Result =' + str(KNearestNeighborsPrediction))
print('-------------'*4)
print('MLPClassfier Prediction Result =' + str(MLPClassfierPredication))
print('-------------'*4)
