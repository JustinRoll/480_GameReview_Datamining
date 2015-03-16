import nltk
from sklearn import metrics
import string
import os
from sklearn.cluster.dbscan_ import DBSCAN
from sklearn.cluster.dbscan_ import dbscan
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer
from sklearn.manifold import MDS
from nltk.stem.porter import PorterStemmer
from scipy.spatial import distance
import collections
import pickle
from pprint import pprint
import numpy as np
from featureUtil import *
from sklearn.feature_extraction import DictVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans, MiniBatchKMeans
import reviewGoldStandard

token_dict = {}
stemmer = PorterStemmer()

def process_text(text, stem=True):
    text = text.translate(string.punctuation)
    tokens = word_tokenize(text)
 
    if stem:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]
 
    return tokens

#future method, evaluate the clusters based on a gold standard
#return a purity level

#assume that we have global variables goldStandard, goldStandardList:
def calculate_purity(clusters):
    #for each cluster, get the count of the most frequent class, keep a running sum of this, then at the end
    #divide by the number of samples in the gold standard 
    #clusters will be a dictionary with index 0: cluster1, index 1: cluster2 etc
    #goldStandard is an array with index 0: labeled category cluster1, ... etc.        
    numAgreed = 0
    for clusterIndex, cluster in clusters.items():
        agreeMap = {}
        #create a map with categories and their counts. then sort the map and grab the category with the highest count
        for sample in cluster:
            sampleclass = goldStandardMap[sample]
            if sampleClass in agreeMap:
                agreeMap[sampleClass] += 1
            else:
                agreeMap[sampleClass] = 1
                #now we can choose the cluster with the highest class
        highestList = sorted([(cluster, agreed) for cluster, agreed in agreeMap.items()], key=itemgetter[1], reverse=True)
        highest = highestList[0][1]
        numAgreed += highest
    return numAgreed * 1.0 / float(len(goldStandardList))

#fit game into a cluster, then figure out what game is in that cluster by looking up all the values
def getGameCluster(reviews, gameName, gameText):
    numReviews = 800
    revDict = listn_reviews(reviews, numReviews)
    revDict[gameName] = gameText.lower().translate(string.punctuation)
    cluster = mkm_cluster_text(token_dict, 60, gameName=gameName)
    return cluster

def listn_reviews(reviews, n=100):
    count = 0
    for gameSystemKey, systemDict in reviews.items():
        if count > n:
            break
        for gameKey, gameReview in systemDict.items():
            if count > n:#just to reduce sample size
                break
            if "review" in gameReview and "scores" in gameReview and "gamespot score" in gameReview["scores"]:
                lowers = gameReview["review"].lower()
                no_punctuation = lowers.translate(string.punctuation)
                token_dict[gameKey] = no_punctuation
                count += 1
    return token_dict 

def cluster_games(reviews):
    for gameSystemKey, systemDict in reviews.items():
        count = 0
        for gameKey, gameReview in systemDict.items():
            count+=1
            if count > 50:#just to reduce sample size
                break
            if "review" in gameReview and "scores" in gameReview and "gamespot score" in gameReview["scores"]:
                lowers = gameReview["review"].lower()
                no_punctuation = lowers.translate(string.punctuation)
                token_dict[gameKey] = no_punctuation
                #print(getEntities(gameReview["review"]))
    cluster = mkm_cluster_text(token_dict)
    return cluster

def cluster_gamesOld(reviews):
    for gameSystemKey, systemDict in reviews.items():
        count = 0
        for gameKey, gameReview in systemDict.items():
            count+=1
            if count > 20:#just to reduce sample size
                break
            if "review" in gameReview and "scores" in gameReview and "gamespot score" in gameReview["scores"]:
                lowers = gameReview["review"].lower()
                no_punctuation = lowers.translate(string.punctuation)
                token_dict[gameKey] = no_punctuation
                #print(getEntities(gameReview["review"]))
    cluster = cluster_text(token_dict)
    return cluster 

def mkm_cluster_text(docs, numClusters, gameName=None):
    """ Transform texts to coordinates using named entities and cluster texts using DBSCAN """
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    sortedValues = [token_dict[key] for key in sorted(token_dict.keys())]
    sortedLabels = [key for key in sorted(token_dict.keys())]
    model = tfidf.fit_transform(sortedValues)    
    
    km = MiniBatchKMeans(n_clusters=numClusters, init='k-means++', n_init=1, init_size=1000, batch_size=1000).fit(model)
 
    tfidf_cluster = collections.defaultdict(list)
    inpCluster = -1
    for idx, label in enumerate(km.labels_):
        tfidf_cluster[label].append(sortedLabels[idx])
        if gameName != None and sortedLabels[idx] == gameName:
            inpCluster = label    
    
    if gameName != None and inpCluster != -1:
        return tfidf_cluster[inpCluster]
    else:
        return tfidf_cluster 

def dbscancluster_text(docs):
    """ Transform texts to coordinates using named entities and cluster texts using DBSCAN """
    
    vec = DictVectorizer()
    #tfidf = HashingVectorizer(tokenizer=tokenize, stop_words='english')
    docFeaturesLabeled = [(docName, getKwEntityFeatures(doc)) for docName, doc in docs.items()]
    docFeatures = [item[1] for item in docFeaturesLabeled]
    labels = [item[0] for item in docFeaturesLabeled]
    model = vec.fit_transform(docFeatures).todense()
    eps = .7 #radius
    min_samples = 2 #number of samples in a cluster
    
    metric = distance.cosine
    dbscan_model = DBSCAN(eps=eps, min_samples=min_samples, metric = metric).fit(model)
 
    tfidf_cluster = collections.defaultdict(list)

    for idx, label in enumerate(dbscan_model.labels_):
        tfidf_cluster[label].append(labels[idx])

    #plot(tfidf_model, dbscan_model, sortedLabels)
    return tfidf_cluster

def knncluster_text(docs):
    """ Transform texts to coordinates using named entities and cluster texts using DBSCAN """
    
    vec = DictVectorizer()
    #tfidf = HashingVectorizer(tokenizer=tokenize, stop_words='english')
    docFeaturesLabeled = [(docName, getKwEntityFeatures(doc)) for docName, doc in docs.items()]
    docFeatures = [item[1] for item in docFeaturesLabeled]
    labels = [item[0] for item in docFeaturesLabeled]
    model = vec.fit_transform(docFeatures)
   
    metric = distance.cosine
    knn_model = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(model) 
    tfidf_cluster = collections.defaultdict(list)

    for idx, label in enumerate(knn_model.labels_):
        tfidf_cluster[label].append(labels[idx])

    #plot(tfidf_model, dbscan_model, sortedLabels)
    return tfidf_cluster 

def cluster_text_Old(token_dict, entities):
    """ Transform texts to Tf-Idf coordinates and cluster texts using DBSCAN """

    #entities = [getEntities(doc) for docName, doc in 
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    sortedValues = [token_dict[key] for key in sorted(token_dict.keys())]
    sortedLabels = [key for key in sorted(token_dict.keys())]
    tfidf_model = tfidf.fit_transform(sortedValues).todense()
    eps = .37 #radius
    min_samples = 2 #number of samples in a cluster
    
    metric = distance.cosine
    dbscan_model = DBSCAN(eps=eps, min_samples=min_samples, metric = metric).fit(tfidf_model)
 
    tfidf_cluster = collections.defaultdict(list)

    for idx, label in enumerate(dbscan_model.labels_):
        tfidf_cluster[label].append(sortedLabels[idx])

    #plot(tfidf_model, dbscan_model, sortedLabels)
    return tfidf_cluster 

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

def plot(X, db, labels_true):
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    print('Estimated number of clusters: %d' % n_clusters_)
    print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
    print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
    print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))

##############################################################################
# Plot result
    import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = 'k'

        class_member_mask = (labels == k)

        xy = X[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, .2], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)

        xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, .2], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=6)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()  

#for k, v in reviews.items():
#    for subKey, gameReview in v.items():
#        
#        if "review" in gameReview:
#            lowers = gameReview["review"].lower()
#            no_punctuation = lowers.translate(string.punctuation)
#            token_dict[k] = no_punctuation

"""for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path = subdir + os.path.sep + file
        shakes = open(file_path, 'r')
        text = shakes.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(None, string.punctuation)
        token_dict[file] = no_punctuation"""
        
#this can take some time
#print(cluster_games(reviews))
