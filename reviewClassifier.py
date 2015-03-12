import random,operator,nltk
import functools
import rmse
from sklearn.naive_bayes import MultinomialNB
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.corpus import udhr
from nltk import bigrams, trigrams, ngrams
from nltk.tokenize import word_tokenize, sent_tokenize 
from nltk.corpus import stopwords, wordnet
from nltk.stem.snowball import SnowballStemmer
from sentencePolarity import SentencePolarity

class Classifier:

    def __init__(self, reviews):
        self.reviews = reviews
        self.polarity = SentencePolarity('twitter_sentiment_list.csv')
    
    def getBucket(self, count):
        if count <= 0:
            returnCount = None
        elif count >= 1 and count <= 5:
            returnCount = "low"
        elif count >= 6:
            returnCount = "high"

        return returnCount
    
    def getOverallFeatures(self, doc):
         
        featureDict = {}
        wordDict, topicWordDict, sents, stemmedWordDict = self.extractReviewWords(doc)
        wordList = sorted([word.lower() for word in set(stemmedWordDict.keys()) if word not in stopwords.words('English') and word not in ',-.;();$' and word not in '-' and word not in '.'],
                key = lambda x : stemmedWordDict[x], reverse=True)
        topWordList = [wordList[i] for i in range(0, 100 if len(wordList) > 100 else len(wordList) - 1)]
        positiveSentenceCount = 0
        negativeSentenceCount = 0

        for sent in sents:
        
            tokenizedSent = [word for word in word_tokenize(sent) if ',' not in word and '.' not in word]
            negProb, posProb = self.polarity.classifySentiment(tokenizedSent)
            if posProb >= .6:
                positiveSentenceCount += 1
            if negProb >= .6:
                negativeSentenceCount += 1

            #for word in tokenizedSent:
            #    posProb, negProb = self.polarity.classifyWord(word)
            #    if negProb >= .8:
            #        featureDict[word + " neg polarity"] = 1
            #    if posProb >= .8:
            #        featureDict[word + " pos polarity"] = 1 

            #wordTrigrams = trigrams(tokenizedSent)
            #for trigram in wordTrigrams:
            #    featureDict[trigram] = True
        for unigram in topWordList:
            featureDict[unigram] = stemmedWordDict[unigram] #self.getBucket(stemmedWordDict[unigram])
        
        featureDict["posSentences"] = positiveSentenceCount
        featureDict["negSentences"] = negativeSentenceCount
        return featureDict

    
    #return a dictionary with words and a count of all the words in the review
    def extractReviewWords(self, doc):
        wordDict = {}
        topicWordDict = {}
        stemmedWordDict = {}
        stemmer = SnowballStemmer('english')
        sents = []        

        
                #tokenize all words
                #to do: pos tag all words?        
        wordTokens = word_tokenize(doc)
        for word in wordTokens:
            self.incrementDictCount(word, wordDict)
            self.incrementDictCount(stemmer.stem(word), stemmedWordDict)
                        #self.incrementDictCount(key, topicWordDict)
        for sent in sent_tokenize(doc):
            sents.append(sent)
        return wordDict, topicWordDict, sents, stemmedWordDict  


    def incrementDictCount(self, item, incDict):
        if item in incDict:
                incDict[item] += 1
        else:
                incDict[item] = 1        

    def classifyOverallReviews(self):

        docs = [(review[2]["review"], 1) for review in self.reviews if review[2]["scores"]["gamespot score"] >= 6] + [(review[2]["review"], 0) for review in self.reviews if review[2]["scores"]["gamespot score"] < 6]
        random.shuffle(docs)

        featureSets = [(self.getOverallFeatures(d),label) for (d, label) in docs]
        firstThird = int(len(featureSets)/3)
        train, test = featureSets[:firstThird], featureSets[firstThird:]
        classifier = SklearnClassifier(MultinomialNB()).train(train)
        #classifier = nltk.NaiveBayesClassifier.train(train)
        #print(classifier.show_most_informative_features(20)) can't show most informative features with multinomial
 
        return rmse.getError(classifier, test), nltk.classify.accuracy(classifier,test) 
 
    def getAverages(self, function):
        accuracyTotal = 0.0
        rmseTotal = 0.0
        accuracies = []
        for i in range(0, 5):
            rmse, accuracy = function()
            accuracies.append(accuracy)
            accuracyTotal += accuracy
            rmseTotal += rmse
        print(accuracies)
        return rmseTotal / 5.0, accuracyTotal / 5.0
