import praw
from pkg import lang
from better_profanity import profanity
# from dotenv import load_dotenv
from prawcore import Redirect, NotFound, Forbidden
import os
import sys

# -*- coding: utf-8 -*-
# load_dotenv()
sys.stdout.reconfigure(encoding='utf-8')

def grade_words(words, bad_words):
    bad_word_count = 0
    appearances = {}
    for word in words:
        if word in bad_words.keys():
          if word in appearances:
            appearances[word] += 1
          else:
            appearances[word] = 1

          bad_word_count += 1
    if bad_word_count == 0:
        return 0
    else:
        appearances = sorted(appearances, key=appearances.get, reverse=True)
        print('Some of the bad words found in your entered subreddit: ' + str(appearances[:10]))
        print(f"{bad_word_count} / {len(words)}")
        return round(max((10 * (bad_word_count / len(words))), 1), 2)

reddit = praw.Reddit(
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    password = os.getenv('PASS'),
    user_agent = "python:com.SuspiciousRater:v0.0.7",
    username = os.getenv('RATER_USER'),
)

def getSubmissionTitleSplit(submission):
  title = submission.title
  selftext = submission.selftext
  text = title + ' ' + selftext
    
  return text.split()

def training(quarantine_sub):
  subreddit = reddit.subreddit(quarantine_sub)
  subreddit.quaran.opt_in()

  bad_word_count = {}

  for submission in subreddit.top(limit=15):
    words = getSubmissionTitleSplit(submission)
    
    for word in words:
      word = word.lower()
      if not profanity.contains_profanity(word):
        continue
      bad_word_count[word] = bad_word_count.get(word, 0) + 1
    
    submission.comments.replace_more(limit=10)
    comments = submission.comments.list()
    
    for comment in comments:
      body = comment.body
      
      words = lang.extract_relevant_words(body)
      for word in words:
        word = word.lower()
        if not profanity.contains_profanity(word):
          continue
        bad_word_count[word] = bad_word_count.get(word, 0) + 1

  appearances = sorted(bad_word_count, key=bad_word_count.get, reverse=True)
  print('Some of the bad words found in training subreddit: ' + str(appearances[:10]))

  return bad_word_count

def getInputRedditWords(inputReddit):
  subreddit = reddit.subreddit(inputReddit)

  word_count = set()

  for submission in subreddit.top(limit=5):
    words = getSubmissionTitleSplit(submission)

    for word in words:
      word = word.lower()
      if not profanity.contains_profanity(word):
        continue
      word_count.add(word)

    submission.comments.replace_more(limit=10)
    comments = submission.comments.list()

    for comment in comments:
      body = comment.body

      words = lang.extract_relevant_words(body)
      for word in words:
        word = word.lower()
        if not profanity.contains_profanity(word):
          continue
        word_count.add(word)

  return list(word_count) 

exists = False

while not exists:
  try:
    inputSubreddit = input('Please enter a subreddit to train on (i.e. russia): ')
    reddit.subreddits.search_by_name(inputSubreddit)
    exists = True
  except:
    print('You entered an invalid subreddit. Please enter a valid one.')

print('Training grader...')
print()

bad_word_count = training(inputSubreddit)

print('Training done!')

exists = False

while not exists:
  try:
    inputSubreddit = input('Please enter a subreddit to rate: ')
    reddit.subreddits.search_by_name(inputSubreddit)
    exists = True
  except:
    print('You entered an invalid subreddit. Please enter a valid one.')

print()
print('rating your subreddit...')

words = getInputRedditWords(inputSubreddit)
grade = grade_words(words, bad_word_count)

print()
print('The entered subreddit has a suspicious score of ' + str(grade) + ' out of 10!')

