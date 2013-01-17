def getListIndex(target, list):
    count = 0
    for item in list:
        if item == target:
            return count
        count += 1

def bubbleUp(wordDict, topTenList, word, startValue = -1): # this method 
    if startValue is -1:
        if wordDict[topTenList[0]] < wordDict[word]:
            topTenList[0] = word
            startValue = 0
        else:
            return topTenList
    while startValue < 9:
        currentWord = topTenList[startValue]
        nextWord = topTenList[startValue + 1]
        if wordDict[currentWord] > wordDict[nextWord]:#swap
            temp = topTenList[startValue + 1]
            topTenList[startValue + 1] = topTenList[startValue]
            topTenList[startValue] = temp
        else:
            return topTenList
        startValue += 1
    return topTenList

def topTen(wordDict, topTenList, word):
    if len(topTenList) < 10:
        topTenList.append(word)
        return topTenList
    elif word in topTenList:
        return bubbleUp(wordDict, topTenList, word, getListIndex(word, topTenList))
    else:
        return bubbleUp(wordDict, topTenList, word)

def main():
    f  = open('pg11.txt', 'r')
    wordDict = {}
    topTenList = []
    lines = f.readlines()
    for line in lines:
        words = line.split(' ')
        for word in words:
           if word == '\n' or word == ' ' or word == '\r\n' or word == '': # only if necessary  
               continue
           if not word in wordDict:
               wordDict[word] = 1
           else:
               wordDict[word] += 1
           topTenList = topTen(wordDict, topTenList, word)
    print topTenList
    #for item in topTenList:
        #print "**%s**" %(item)
        #print wordDict[item]

if __name__ == "__main__":
    main()
