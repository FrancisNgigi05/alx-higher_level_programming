#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return None

    first_letter = sentence[0]

    sentence_len = len(sentence)

    result = (sentence_len, first_letter)

    return result
