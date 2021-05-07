import os
import sys

# Add vendor directory to module search path
parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')

sys.path.append(vendor_dir)

from twython import Twython

from auth import (
    API_key,
    API_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    API_key,
    API_secret,
    access_token,
    access_token_secret
)

message = 'This was tweeted from a python script using the Twitter API!'
twitter.update_status(status=message)
print("Tweeted: %s" %message)