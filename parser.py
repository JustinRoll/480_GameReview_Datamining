import re


class Parser:

    def __init__(self):
        pass

    def parseSimpleLine(self, line):
        subRegex = r"(\w+): ([\w-]+ ?\w+)"
        regex = re.compile(subRegex)
        result = regex.findall(line)
        if result:
            return result
        else:
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
                print(result.group(1))
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
                    for userReview in userReviews:
                        userReview.replace("||", "\n")
                        userReviewDict = {}
                        subGroups = self.parseSimpleLine(userReview)
                        if subGroups:
                            for subGroup in subGroups:
                                userReviewDict[subGroup[0]] = subGroup[1]
                            print(userReviewDict)
                            userReviewList.append(userReviewDict)

                elif result.group(1).strip() == "Addition":
                    subDict = {}
                    subRegex = r"(\w+): ([\w-]+ ?\w+)"
                    parsedlines = result.group(2).strip().replace("||", "\n")
                    subGroups = re.findall(subRegex, result.group(2).strip())
                    for subGroup in subGroups:
                        subDict[subGroup[0]] = subGroup[1]

                    review['Addition'] = subDict
                else:
                    review[result.group(1).strip()] = result.group(2).strip()

f = open("/Users/jroll/dev/480/480_GameReview_Datamining/data/Gamespot-Cleaned/DS/DragonQuestVHandoftheHeavenlyBride.txt", "r")
parser = Parser()
parser.parse(f.read().replace('\n', '||'))

