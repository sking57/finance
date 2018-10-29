from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # make a list of the lines of each file
    lines1 = set(a.split("\n"))
    lines2 = set(b.split("\n"))
    # return common lines as a list
    return list(lines1.intersection(lines2))


def sentences(a, b):
    """Return sentences in both a and b"""

    # separate each file into sentences
    sentences1 = set(sent_tokenize(a))
    sentences2 = set(sent_tokenize(b))
    # return common sentences as a list
    return list(sentences1.intersection(sentences2))


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # create sets of substrings of length n
    ss1 = set()
    ss2 = set()
    for c in range(len(a)-n+1):
        ss1.add(a[c:c+n])
    for c in range(len(b)-n+1):
        ss2.add(b[c:c+n])
    # return common substrings in sets as a list
    return list(ss1.intersection(ss2))