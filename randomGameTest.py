#open up a review for a random game, then see what the classifier comes up with.
import pickle
import sys
from reviewClassifier import Classifier
classData =  pickle.load(open("reviewClassifier.p", "rb", -1))

def classifyGame(game):
    myClassifier = Classifier()
    return myClassifier.classify(classData, game)

def classifyGameReviewFile(fileName):
    f = open(fileName, 'r')
    fText = '\n'.join(f.readlines())
    return classifyGame(fText)

print(classifyGameReviewFile(sys.argv[1]))
