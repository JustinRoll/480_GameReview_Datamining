import re
import os
import pickle

class Parser:

    def __init__(self):
        pass

    def parseSimpleLine(self, line):
        subRegex = r"(\w+): ([\w-]+ ?\w+)$"
        regex = re.compile(subRegex)
        result = regex.findall(line)
        if result:
            return result
        else:
            return None

    def parseUserReview(self, text):
        #UserName: madd_hatter
        #Rating: 9.3
        #Date: Aug 30, 2006 1:59 pm PT
        #Review:  Okay, let's start with the
        
        if "username:" in text.lower() and "rating:" in text.lower() and "date:" in text.lower() and "review:" in text.lower():
            userReviewDict = {}
            lineArray = text.split("||")
            userReviewDict["UserName"] = lineArray[1].split(":")[1].strip()
            userReviewDict["Rating"] = lineArray[2].split(":")[1].strip()
            userReviewDict["date"] = lineArray[3].replace("Date:", "").strip()
            userReviewDict["review"] = " ".join(lineArray[4:])
            return userReviewDict
        else:
            #print("bad dict")
            #print(text)
            #print("/end bad dict")
            return None



    def parse(self, text):
#        regexp = re.sub("-------------------------------------------------", text)
        review = {}
        lines = text.split("-------------------------------------------------")
        regexText = ":::(.+):::(.+)"
        for line in lines:
            regex = re.compile(regexText)
            result = regex.search(line)
            if result:
                #print(result.groups())
                #print(result.group(1))
                if result.group(1).strip() == "Scores":
                    subDict = {}
                    subRegex = r"(\w+ \w+): (\w+.[0-9]+)"
                    subGroups = re.findall(subRegex, result.group(2).strip())
                    for subGroup in subGroups:
                        subDict[subGroup[0]] = float(subGroup[1])
                    review["Scores"] = subDict
                elif "User Reviews" in result.group(1):
                    #print(result.group(1))
                    userReviewList = []
                    userReviews = result.group(1).split("::::::")
                    for userReview in userReviews[1:]:
                        #userReview = userReview.replace("||", "\n")
                        userReviewDict = self.parseUserReview(userReview)
                        if userReviewDict:
                            userReviewList.append(userReviewDict)
                    review["userReviews"] = userReviewList

                elif result.group(1).strip() == "Addition": #working
                    subDict = {}
                    subRegex = r"(\w+): ([\w-]+ ?\w+)"
                    parsedlines = result.group(2).strip().replace("||", "\n")
                    subGroups = re.findall(subRegex, result.group(2).strip())
                    for subGroup in subGroups:
                        subDict[subGroup[0]] = subGroup[1]
                    review['Addition'] = subDict
                else:
                    review[result.group(1).strip()] = result.group(2).strip()

        return review

def parseFiles(path):
    files = os.listdir(path)
    parser = Parser()
    reviews = {}
    for fName in files:
        f = open(path + fName)
        reviews[fName] = parser.parse(f.read().replace('\n', '||'))
    return reviews

def parseDir(path):
    #get all subdirectories, parse them into
    print(os.listdir(path))
    reviews = {}
    for folder in os.listdir(path):
        if "DS_Store" not in folder:
            reviews[folder] = parseFiles(path + folder + "/")
    return reviews

reviews = parseDir("/Users/jroll/dev/480/480_GameReview_Datamining/data/Gamespot-Cleaned/")
pickle.dump(reviews, open( "data/gameReviewDict.p", "wb" ))
#print(savedDict)
#print(reviews)
#validation here
