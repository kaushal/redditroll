def populateWordDict(dictionary):
    f = open("nouns.txt", "r")
    for line in f:
        dictionary["nouns"].append(line)
    f = open("verbs.txt", "r")
    for line in f:
        dictionary["verbs"].append(line)
    return dictionary
