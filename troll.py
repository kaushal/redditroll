from redditFunctions import *
from trollFunctions import *
from pprint import pprint as pp2


def main():
    print 'the cake is a lie'
    wordList = {}
    wordList["nouns"] = []
    wordList["verbs"] = []
    wordList = populateWordDict(wordList)
    client = login('not_a_trollbot', 'trollbot')
    j = subredditInfo(client, 1, 'funny', '', True)
    pp2(j["data"])
if __name__ == '__main__':
        main()
