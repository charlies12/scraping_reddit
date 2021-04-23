import os
import praw
import pandas as pds
import datetime as dt

# hmm, necessary stuff I guess
reddit = praw.Reddit(client_id=os.environ.get('R_CLIENT_ID'),
                     client_secret=os.environ.get('R_SECRET_KEY'),
                     user_agent=os.environ.get('R_USER_AGENT'),
                     username=os.environ.get('R_USERNAME'),
                     password=os.environ.get('R_PASSWORD'))

# Genshin impact reddit
subreddit = reddit.subreddit('Genshin_Impact')

# chooses the most popular post
# Also limiting to 30 posts
hot_subreddit = subreddit.hot(limit=30)
# some_comments = subreddit.comments(limit=20)
# print(some_comments)
# making a dictionary
topics_dict = { "title": [],
                "score": [],
                "id" : [], "url": [],
                "comms_num": [],
                "created": [],
                "body": []
                }

# showing info
for submission in hot_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

# using pandas here
topics_data = pds.DataFrame(topics_dict)


# time stamps
def get_date(created):
    return dt.datetime.fromtimestamp(created)


time_stamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp=time_stamp)

topics_data.to_csv('genshin_impact_hot.csv', index=False)





