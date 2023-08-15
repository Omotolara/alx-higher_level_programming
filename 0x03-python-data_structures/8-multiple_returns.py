#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        first_character = None
    else:
        return (len(sentence), sentence[0])
