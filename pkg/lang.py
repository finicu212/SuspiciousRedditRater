## This module is responsible for language processing

import nltk
import re

'''
body = 'Nazis, cannibals, knowing child-killers, and scum who make half a hundred civilians being burned alive for their political opinions a point of pride and a national holiday do not deserve respect.'
relevant_words = [('Nazis', 'NNP'), ('cannibals', 'NNS'), ('knowing', 'VBG'), ('child-killers', 'NNS'), ('scum', 'NN'), ('make', 'VBP'), ('hundred', 'JJ'), ('civilians', 'NNS'), ('being', 'VBG'), ('alive', 'JJ'), ('political', 'JJ'), ('opinions', 'NNS'), ('point', 'NN'), ('pride', 'NN'), ('national', 'JJ'), ('holiday', 'NN'), ('do', 'VBP'), ('not', 'RB'), ('deserve', 'VB'), ('respect', 'NN')]

body = 'Fine then its the liberals ndp conservatives in Canada and democrats and republicans. I chose the Democrats and liberals because they both have known monetary gains to make in the Ukraine if Ukraine opposes Russia.'
relevant_words = [('Fine', 'NNP'), ('then', 'RB'), ('liberals', 'NNS'), ('ndp', 'VBP'), ('conservatives', 'NNS'), ('Canada', 'NNP'), ('liberals', 'NNS'), ('have', 'VBP'), ('monetary', 'JJ'), ('gains', 'NNS'), ('make', 'VB'), ('Ukraine', 'NNP'), ('Ukraine', 'NNP'), ('opposes', 'VBZ'), ('Russia', 'NNP')]
'''

# Use this function outside of the module.
# Returns a list of relevant words, as marked by __is_tag_relevant function.
def extract_relevant_words(comment_body: str) -> list:
    # Before word_tokenizing, remove all links from the comment.
    comment_body = re.sub(r'(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*', " ", comment_body)

    toks = nltk.word_tokenize(comment_body)
    tags = nltk.pos_tag(toks)

    relevant_words = []
    for t in tags:
        if __is_tag_relevant(t):
            relevant_words.append(t[0])

    return relevant_words


# Do not call this function outside of the module.
def __is_tag_relevant(t: tuple) -> bool:
    whitelisted_tags = ['JJ', 'JJR', 'NN', 'NNS', 'NNP', 'VB', 'VBZ', 'VBP', 'VBG', 'RB']
    blacklisted_words = ['[', ']', '>', '<', '%', r'\\', '\'re', 'n\'t', '\'s', 'are', 'be']
    
    # First should add all fail conditions, ordered by most generally inclusive to least inclusive
    if t[0] in blacklisted_words:
        return False

    # Then all success conditions, ordered by least inclusive to most generally inclusive
    if t[1] in whitelisted_tags:
        return True

    # Catch all tags which didn't qualify and exclude them
    return False