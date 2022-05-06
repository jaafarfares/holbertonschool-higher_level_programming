#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        tuplee = NULL
    else:
        tuplee = length, sentence[0]
    return tuplee
