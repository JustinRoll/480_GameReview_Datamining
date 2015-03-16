from clusterGames import *
from  reviewGoldStandard import *
import pickle
from copy import deepcopy
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
    gs = GoldStandard()
    revs = getGoldStandardReviews(gs)
    gs.goldStandardList = [rev[0] for rev in revs]
    updateGoldStandard(gs)
    clusters = cluster_gamesGSkb(revs, gs)
    print(calculate_purity(clusters, gs))

main()
