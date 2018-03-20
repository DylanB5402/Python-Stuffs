import praw

reddit = praw.Reddit(client_id='pg8gEuw8i0VMBg', client_secret='2UHpkdLDFellHBsSvMI5B_LjAk4', )

subreddit = reddit.subreddit("showerthoughts")

for submission in subreddit.hot(limit=5):
        print("Title: ", submission.title)