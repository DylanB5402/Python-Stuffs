import pypub
import praw, os
praw_object = praw.Reddit(user_agent='pypub/1.0')
top_submission_list = praw_object.get_subreddit('https://parahumans.wordpress.com/table-of-contents/').get_top(limit=10)
top_submission_url_list = [submission.url for submission in top_submission_list]
epub = pypub.Epub('Test')
for url in top_submission_url_list:
    try:
         c = pypub.create_chapter_from_url(url)
         epub.add_chapter(c)
    except ValueError:
         pass
epub.create_epub(os.getcwd())