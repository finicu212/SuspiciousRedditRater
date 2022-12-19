import praw
from pkg import lang

# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

reddit = praw.Reddit(
    client_id="o15VigttId3z68mTrV4Jyg",
    client_secret="8W4KVNr7cnBbNatbXvX5aaGowA4B_A",
    password="notgonnatellu",
    user_agent="python:com.SuspiciousRater:v0.0.7 (by /u/the-dark-defender)",
    username="minculeteandrei",
)
subreddit = reddit.subreddit("russia")
subreddit.quaran.opt_in()

word_count = {}

for submission in subreddit.top(limit=5):
  # selftext = the main body of the post
  title = submission.title
  selftext = submission.selftext
  
  text = title + ' ' + selftext
  
  words = text.split()
  
  for word in words:
    word_count[word] = word_count.get(word, 0) + 1
  
  submission.comments.replace_more()
  print()
  comments = submission.comments.list()
  
  for comment in comments:
    body = comment.body
    
    words = lang.extract_relevant_words(body)
    for word in words:
      word_count[word] = word_count.get(word, 0) + 1

# Sort the dictionary by value in descending order
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_word_count[:100]:
  print(f'{word}: {count}')
