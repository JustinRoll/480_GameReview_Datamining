from clusterGames import *
from  reviewGoldStandard import *
import pickle
from copy import deepcopy
import sys
#load all reviews from the gold standard
#   check if there are reviews from the gold standard that didn't get parsed correctly; discard those
#   update gold standard
#cluster the reviews

#evaluate purity
def getGoldStandardReviews(gs):
    reviews = pickle.load(open("data/gameReviewDict.p", "rb"))
    reviewsList = []
    for gameSystemKey, systemDict in reviews.items():
        for gameKey, gameReview in systemDict.items():
            if "review" in gameReview and "scores" in gameReview and "gamespot score" in gameReview["scores"] and gameKey in gs.goldStandardList:
                reviewsList.append((gameKey, gameSystemKey, gameReview))
    return reviewsList 

def updateGoldStandard(gs):
    gsTempMap = deepcopy(gs.goldStandardMap)
    for key in gsTempMap.keys():
        if key not in gs.goldStandardList:
            del gs.goldStandardMap[key]


def main():
    clusterType = sys.argv[1]
    features = sys.argv[2]
    gs = GoldStandard()
    revs = getGoldStandardReviews(gs)
    gs.goldStandardList = [rev[0] for rev in revs]
    updateGoldStandard(gs)
    if len(sys.argv) < 3:
        print("Enter kmeans or dbscan for the clustering algorithm")
        print("Enter wc or tfidf or entity for the features")
        return
    if clusterType.lower() == "kmeans":
        if features.lower() == "wc":
            clusters = cluster_gamesGSkm_wc(revs, gs)
        elif features.lower() == "tfidf":
            clusters = cluster_gamesGSkm_tfidf(revs, gs)
        else:
            clusters = cluster_gamesGSkm_ent(revs, gs) 

    elif clusterType.lower() == "dbscan":
        #cluster_gamesGSDb_tfidf(
        if features.lower() == "wc":
            clusters = cluster_gamesGSdb_wc(revs, gs)
        elif features.lower() == "tfidf":
            clusters = cluster_gamesGSdb_tfidf(revs, gs)
        else:
            clusters = cluster_gamesGSdb_ent(revs, gs)
    print(calculate_purity(clusters, gs))

main()
