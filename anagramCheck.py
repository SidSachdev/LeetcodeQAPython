# Not the optimal way
def AnagramCheck(sent, sent2):
    x = sent.replace(" ", "").lower()
    y = sent2.replace(" ", "").lower()

    print(sorted(x) == sorted(y))

AnagramCheck("clint Eastwood","old west action")


#Optimal Way
def AnagramCheck2(sent, sent2):
    x = sent.replace(" ", "").lower()
    y = sent2.replace(" ", "").lower()

    #Edge Case Check

    if len(x) != len(y):
        return False

    count = {}

    for letter in x:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in y:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

print(AnagramCheck2("xclint Eastwood","old wesssssst action"))