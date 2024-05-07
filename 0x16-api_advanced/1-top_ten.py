#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import json
import requests


def top_ten(subreddit):
     """Query Reddit and print titles of the first 10 hot posts"""
    
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "laden_brandon"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
