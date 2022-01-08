#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        x = (len(sentence), sentence[0])
    else:
        x = (len(sentence), None)
    return x
