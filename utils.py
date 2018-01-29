import re

def remove_unwanted_chars(line):
    line = re.subn('<.*>', '', line)[0] # removing <APPLAUSE> etc
    line = re.subn('&.*?;', ' ', line)[0]
    line = re.subn(' [-+\s*-*]+ ', ' - ', line)[0] # not cool but works, removes '-- -' and the likes
    line = line.rstrip() # removing whitespace at end of string
    return line

def remove_malformed_lines(speech):
    return list(filter(lambda l: len(l) > 2, speech))

def read_speech_from_file(f):
    speech = []
    f.readline(); f.readline() # skipping header
    for line in f:
        line = remove_unwanted_chars(line)
        speech.append(line)
    return speech

def preprocess_speech(file):
    with open(file) as f:
        speech = read_speech_from_file(f)
        speech = remove_malformed_lines(speech)
        speech = ' '.join(speech)
        speech = re.subn('\s+', ' ', speech)[0] # multiple white spaces are now a single space
    return speech
