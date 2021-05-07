
# for package management. I want to be able to use this with AWS Lambda so I 
# thought it would be easier if all the packages were right here
import os
import sys

# this is a txt file on my website where the random lines to be tweeted come from.
data_url = 'https://www.souder.ca/TweetableText.txt'

# Add vendor directory to module search path - for external modules
parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')

sys.path.append(vendor_dir)

# imports
from twython import Twython
from twython import TwythonError
import urllib.request
import random

# for randomness
random.seed()

# get twitter auth stuff
from auth import (
    API_key,
    API_secret,
    access_token,
    access_token_secret
)

# twitter API setup
twitter = Twython(
    API_key,
    API_secret,
    access_token,
    access_token_secret
)

# file manipulation
data = urllib.request.urlopen(data_url).read(2000).decode("utf-8").split("\n")
num_lines = len(data)-1

success=False

pickedLine = random.randint(0, num_lines-1)
print(pickedLine)


#while(success==False):
try:
    # create message
    message =data[pickedLine]

    # send message
    twitter.update_status(status=message)

    #success=True
except TwythonError:
    pickedLine += 1
    if(pickedLine >= num_lines):
        pickedLine=0
    print(pickedLine)
    
    # create message
    message =data[pickedLine]

    # send message
    twitter.update_status(status=message)