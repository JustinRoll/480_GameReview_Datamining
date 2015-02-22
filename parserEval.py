import pickle
reviews = pickle.load(open("data/gameReviewDict.p", "rb"))

#reviews = {}
#ff10 = "Ff10 is a great game"
#dq7 = "dq7 is pretty good"
#ps2Reviews = {"Final Fantasy 10": ff10, "Dragon Quest 7" : dq7}
#reviews["ps2"] = ps2Reviews


#"ps2" : {"Final Fantasy 10": "here is some text"} , {"Dragon Quest 7": "here is some more text"} }


#evaluate the review and check if it has all the categories
def isInvalidReview(review):
    catCount = 0
    tooLong = False

    baseCategories = {"the good":True, "the bad":True, "game name":True, "date":True, "scores":True, "addition":True, "user reviews":True}
    for reviewKey, reviewValue in review.items():
        #print(reviewKey)
        if reviewKey in baseCategories:
            catCount += 1
        if len(reviewKey) > 100:
            tooLong = True

    if len(baseCategories) != catCount or tooLong == True:
        
        print(catCount)
        return True
    else:
        return False


def evalReviews(reviews):

    badReviews = []
    totalReviewCount = 0

    for k, v in reviews.items():
        for gameName, gameReview in v.items():
            #print(subKey)
            if isInvalidReview(gameReview):
                print("bad review for %s" % gameName)
                badReviews.append(gameName)
            
            totalReviewCount+= 1
    
    print("This many bad reviews: %d" %len(badReviews))

    print("This many total reviews: %d" %totalReviewCount) 

def main():
    evalReviews(reviews)


main()



