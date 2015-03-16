#open up a review for a random game, then see what the classifier comes up with.
import pickle
import sys
from reviewClassifier import Classifier
from alchemyapi import AlchemyAPI
import json
from featureUtil import *
alchemyapi = AlchemyAPI()


classData =  pickle.load(open("reviewClassifier.p", "rb", -1))

def classifyGame(game):
    myClassifier = Classifier()
    return myClassifier.classify(classData, game)

def classifyGameReviewFile(fileName):
    f = open(fileName, 'r')
    fText = '\n'.join(f.readlines())
    return classifyGame(fText)

def getEntitiesPrint(text):
    response = alchemyapi.entities('text', text, {'sentiment': 1})

    if response['status'] == 'OK':
        print('## Response Object ##')
        print(json.dumps(response, indent=4))

        print('')
        print('## Entities ##')
        for entity in response['entities']:
            print('text: ', entity['text'].encode('utf-8'))
            print('type: ', entity['type'])
            print('relevance: ', entity['relevance'])
            print('sentiment: ', entity['sentiment']['type'])
            if 'score' in entity['sentiment']:
                print('sentiment score: ' + entity['sentiment']['score'])
            print('')
    else:
        print('Error in entity extraction call: ', response['statusInfo']) 

#f = open(sys.argv[1], 'r')
#fText = '\n'.join(f.readlines())
#f.close()
#print(classifyGameReviewFile(sys.argv[1]))
#print(getEntities(fText))
#print(makeChart(getEntities(fText)))
