import pickle
reviews = pickle.load(open("data/gameReviewDict.p", "rb"))

#reviews = {}
#ff10 = "Ff10 is a great game"
#dq7 = "dq7 is pretty good"
#ps2Reviews = {"Final Fantasy 10": ff10, "Dragon Quest 7" : dq7}
#reviews["ps2"] = ps2Reviews


#"ps2" : {"Final Fantasy 10": "here is some text"} , {"Dragon Quest 7": "here is some more text"} }
badReviews = []
totalReviewCount = 0

for k, v in reviews.items():
    for subKey, gameReview in v.items():
        #print(subKey)
        totalReviewCount+= 1
        for key, value in gameReview.items():
            if len(key) < 100:
                print(key)
            else:
                print(" ")
                print("Bad review for %s" % subKey)
                print(" ")
                badReviews.append(subKey)
                break
def main():
    pass


print("This many bad reviews: %d" %len(badReviews))

print("This many total reviews: %d" %totalReviewCount)
