#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import json
import requests


def number_of_subscribers(subreddit):
     """query a subreddit and retrive no of subscribers"""
    
    user = {"User-Agent": "laden_brandon"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=user)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
