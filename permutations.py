def permutation(inputString):
    if len(inputString) == 1:
        return inputString

    finalList = [] #where I will store the permutations
    for char in inputString:
        partialList = permutation(inputString.replace(char, ""))

        for element in partialList:
            if char + element not in finalList:
                finalList.append(char + element)
    return finalList

print permutation("a1b2c3")
