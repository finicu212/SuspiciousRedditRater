## This module is responsible for language processing

import nltk

'''
body = "> All I see is some blind hatred and counting all Ukrainians as nazis. \n\nI am sorry facts make you uncomfortable. You can go have a chat with them in the Ukrainian subreddits, lol, see if your opinions persist.\n\n>Since when did people rise by themselves?\n\nUhhh, since forever? Or are you trying to insinuate that the Maidan protests and the captures of city administrations in the West were not an organic grassroots Ukrainian movement?!\n\n>A bunch of miners won't help, separate cases in Ukraine happen now and then, now what? \n\nSo where are they? Don't be shy, I've already asked for evidence above - where are the Ukrainian calls for justice for the murderers in Odessa, for the nazi punitive battalions, for regular attacks against civilian targets the ukkie army still perpetrates regularly? Maybe there is at least a movement for implementing the Minsk Agreements, which would stop the war? \n\n>Stop judging all the people by their criminals.\n\nWhen there is not a voice coming from a country other than these of the criminals - who have the power and thus have appointed themselves not-criminals, to begin with, - it is patently obvious that the silent majority of its population is perfectly fine with what those cannibals are doing."
relevant_words = [('see', 'VBP'), ('is', 'VBZ'), ('blind', 'NN'), ('counting', 'VBG'), ('nazis', 'NN'), ('am', 'VBP'), ('sorry', 'JJ'), ('facts', 'NNS'), ('make', 'VBP'), ('uncomfortable', 'JJ'), ('go', 'VB'), ('have', 'VB'), ('chat', 'NN'), ('Ukrainian', 'JJ'), ('subreddits', 'NNS'), ('lol', 'NN'), ('see', 'VBP'), ('opinions', 'NNS'), ('persist', 'VBP'), ('people', 'NNS'), ('rise', 'VB'), ('Uhhh', 'NNP'), ('forever', 'RB'), ('are', 'VBP'), ('trying', 'VBG'), ('insinuate', 'VB'), ('Maidan', 'NNP'), ('protests', 'NNS'), ('captures', 'NNS'), ('city', 'NN'), ('administrations', 'NNS'), ('West', 'NNP'), ('not', 'RB'), ('organic', 'JJ'), ('grassroots', 'NNS'), ('Ukrainian', 'JJ'), ('movement', 'NN'), ('A', 'NNP'), ('bunch', 'NN'), ('miners', 'NNS'), ("n't", 'RB'), ('help', 'VB'), ('separate', 'JJ'), ('cases', 'NNS'), ('Ukraine', 'NNP'), ('happen', 'VB'), ('now', 'RB'), ('then', 'RB'), ('now', 'RB'), ('So', 'RB'), ('are', 'VBP'), ('Do', 'VBP'), ("n't", 'RB'), ('be', 'VB'), ('shy', 'JJ'), ("'ve", 'VBP'), ('already', 'RB'), ('evidence', 'NN'), ('are', 'VBP'), ('Ukrainian', 'JJ'), ('calls', 'NNS'), ('justice', 'NN'), ('murderers', 'NNS'), ('Odessa', 'NNP'), ('nazi', 'JJ'), ('punitive', 'JJ'), ('battalions', 'NNS'), ('regular', 'JJ'), ('attacks', 'NNS'), ('civilian', 'JJ'), ('targets', 'NNS'), ('ukkie', 'JJ'), ('army', 'NN'), ('still', 'RB'), ('perpetrates', 'VBZ'), ('regularly', 'RB'), ('Maybe', 'RB'), ('is', 'VBZ'), ('movement', 'NN'), ('implementing', 'VBG'), ('Minsk', 'NNP'), ('Agreements', 'NNP'), ('stop', 'VB'), ('war', 'NN'), ('Stop', 'NNP'), ('judging', 'NN'), ('people', 'NNS'), ('criminals', 'NNS'), ('is', 'VBZ'), ('not', 'RB'), ('voice', 'NN'), ('coming', 'VBG'), ('country', 'NN'), ('other', 'JJ'), ('criminals', 'NNS'), ('have', 'VBP'), ('power', 'NN'), ('thus', 'RB'), ('have', 'VB'), ('not-criminals', 'NNS'), ('begin', 'VB'), ('is', 'VBZ'), ('patently', 'RB'), ('obvious', 'JJ'), ('silent', 'JJ'), ('majority', 'NN'), ('population', 'NN'), ('is', 'VBZ'), ('perfectly', 'RB'), ('fine', 'JJ'), ('cannibals', 'NNS'), ('are', 'VBP'), ('doing', 'VBG')]
'''



def extract_relevant_words(comment_body: str) -> list:
    # TODO: Before word_tokenizing, remove all links from the comment.
    toks = nltk.word_tokenize(comment_body)
    tags = nltk.pos_tag(toks)

    relevant_words = []
    for t in tags:

            relevant_words.append(t)

    print(f"{relevant_words = }")
    return relevant_words


def is_tag_relevant(t: tuple) -> bool:
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