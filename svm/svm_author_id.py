#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]


#########################################################
### your code goes here ###

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

for c in [10000]: # 1000, 100, 10
	print c
	t = time()
	clf = SVC(kernel = 'rbf', C = c).fit(features_train, labels_train)
	print 'training time: %d.2 seconds' % (time() - t)

	t = time()
	pred = clf.predict(features_test)
	print 'predicting time: %d.2 seconds' % (time() - t)
	print accuracy_score(pred, labels_test)
	print sum(pred)

#########################################################


