from alchemyapi import AlchemyAPI
import json
import numpy as np
import matplotlib.pyplot as plt                
from operator import itemgetter
alchemyapi = AlchemyAPI() 
import random
#classData =  pickle.load(open("reviewClassifier.p", "rb", -1))

#def classifyGame(game):
#    myClassifier = Classifier()
#    return myClassifier.classify(classData, game) 

def chart3(entities):
    import numpy as np
    import matplotlib.pyplot as plt
    
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    menStd =   (2, 3, 4, 1, 2)
    
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, menMeans, width, color='r')
    
    womenMeans = (25, 32, 34, 20, 25)
    rects2 = ax.bar(ind+width, womenMeans, width, color='y')
    
    # add some text for labels, title and axes ticks
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )
    
    ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
    
    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                    ha='center', va='bottom')
    
    #autolabel(rects1)
    #autolabel(rects2)
    
    plt.show() 


def makeChart2(entities):
    placeTypes = ['City', 'Continent', 'Country', 'GeographicFeature', 'Region', 'StateOrCounty']
    orgTypes = ['Company', 'Organization', 'Facility']
    person = ['Person']
    thingTypes = ['Degree','EntertainmentAward','FinancialMarketIndex','HealthCondition', 'Holiday', 'JobTitle', 'Movie', 'MusicGroup', 'NaturalDisaster',
    'Anniversary', 'Automobile','Degree','EntertainmentAward','FinancialMarketIndex','HealthCondition','Holiday','JobTitle','Movie','MusicGroup','NaturalDisaster',
    'OperatingSystem','PrintMedia','Product','RadioProgram','RadioStation','Sport','SportingEvent','Technology','TelevisionShow','TelevisionStation','EmailAddress',
    'TwitterHandle','Hashtag','IPAddress','Quantity','Money']

    data = [(entity["text"], int(entity["count"])) for entity in entities]
    data = sorted(data, key=itemgetter(1), reverse=True)
    #N = len( data )         
    N = 4
    people = [(entity["text"], int(entity["count"])) for entity in entities if entity["type"] == "Person"]
    orgs = [(entity["text"], int(entity["count"])) for entity in entities if entity["type"] in orgTypes]
    places = [(entity["text"], int(entity["count"])) for entity in entities if entity["type"] in placeTypes]
    things = [(entity["text"], int(entity["count"])) for entity in entities if entity["type"] in thingTypes]
    

    menMeans = (20, 35, 30, 35, 27)
    
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, menMeans, width, color='g')
    
    womenMeans = (25, 32, 34, 20, 25)
    rects2 = ax.bar(ind+width, womenMeans, width, color='b')
    
    # add some text for labels, title and axes ticks
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('People', 'Places', 'Orgs', 'Things', 'G5') )
    
    ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
    
    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                    ha='center', va='bottom')
    
    autolabel(rects1)
    autolabel(rects2)
    
    plt.show()


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def makeChart(entities):
    data = sorted([(entity["text"], int(entity["count"]), entity["sentiment"]["type"]) for entity in entities], key=itemgetter(1))
    posdata = [item for item in sorted(data, key=itemgetter(1)) if item[2].lower() == "positive"]
    negdata =  [item for item in sorted(data, key=itemgetter(1)) if item[2].lower() == "negative"] 
    neutraldata =  [item for item in sorted(data, key=itemgetter(1)) if item[2].lower() == "neutral"] 
    N = len(posdata) + len(negdata) + len(neutraldata)
    y = np.arange(1, N+1)
    posx = np.array([ num for (s, num, sent) in data  if sent.lower() == "positive"]) 
    negx = np.array([ num for (s, num, sent) in data if sent.lower() == "negative"])
    neutralx = np.array([ num for (s, num, sent) in data if sent.lower() == "neutral"])
    labels = np.array([s for (s, num, sent) in data]) 
    # Example data

    index = 0
    for entity, count, sentiment in data:
        if sentiment.lower() == "positive":
                color = "g"
        elif sentiment.lower() == "negative":
                color = "r"
        else:
                color = "y"
        plt.barh(index - 0.5, count, 0.7, color=color)
        index+=1
    y_pos = np.arange(N)
    
    plt.yticks(y_pos, labels)
    plt.xlabel('Entity Count')
    plt.title('Named Entities')

    plt.show()

def makeChartA(entities):
    data = [(entity["text"], int(entity["count"])) for entity in entities]
    data = sorted(data, key=itemgetter(1), reverse=True)
    N = len( data )
    y = np.arange(1, N+1)
    x = [ num for (s, num) in data ] 
    labels = np.array([s for (s, num) in data])
    # Example data
    y_pos = np.arange(len(labels))

    error = np.random.rand(len(labels))

    plt.barh(y_pos, 3+10*rand(5), xerr=error, align='center', alpha=0.4)
    plt.yticks(y_pos, labels)
    plt.xlabel('Count')
    plt.title('Named Entities')

    plt.show()


def makeChartOld(entities):
    """data = [ ("data1", 34), ("data2", 22),
        ("data3", 11), ( "data4", 28),
        ("data5", 57), ( "data6", 39),
        ("data7", 23), ( "data8", 98)]"""
    #for entity in entities:
    #    print(entity["text"])
    #    print(int(entity["count"]))
    data = [(entity["text"], int(entity["count"])) for entity in entities]
    data = sorted(data, key=itemgetter(1), reverse=True)
    N = len( data )
    y = np.arange(1, N+1)
    x = [ num for (s, num) in data ]
    fig, ax = plt.subplots()
    def autolabel(rects, labels):
    # attach some text labels
        for i in range(0, len(rects)):
                rect = rects[i]
                label = labels[i]
                height = rect.get_height()
                ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, label, ha='center', va='bottom') 
 
    labels = [ s for (s, num) in data ]
    width = 1
    bar1 = plt.bar( x, y, width, color="g")
    plt.ylabel( 'Count' )
    #plt.xticks(x + width/2.0, labels )
    
    plt.yticks(y + width/2.0, labels )
    #autolabel(bar1, labels)
    plt.show()
    
def getEntityFeatures(doc):
    entities = getEntities(doc)
    featureDict = {}
    for entity in entities:
        featureDict[entity["text"] + "_ex_"] = int(entity["count"])
    return featureDict      

def getKeyWordsFeatures(doc):
    keywords = getKeyWords(doc)
    featureDict = {}
    for keyword in keywords:
        featureDict[keyword["text"] + "_kw_"] = float(keyword["relevance"])
    return featureDict      

def getKwEntityFeatures(doc):
    featureDict = getEntityFeatures(doc)
    kwDict = getKeyWordsFeatures(doc)
    featureDict.update(kwDict)
    return featureDict


def getKeyWords(text):
    response = alchemyapi.keywords('text', text, {'sentiment': 1})

    if response['status'] == 'OK':
        return [entity for entity in response['keywords']]
    else:
        print('Error in entity extraction call: ', response['statusInfo'])  
        return None 

def getEntities(text):
    response = alchemyapi.entities('text', text, {'sentiment': 1})

    if response['status'] == 'OK':
        return [entity for entity in response['entities']]
    else:
        print('Error in entity extraction call: ', response['statusInfo'])  
        return None
