import praw
import time

r = praw.Reddit('Simple Trollbot :P')
r.login('not_a_trollbot', 'trollbot')
submission = r.get_submission(submission_id='11v36o')
flat_comments = submission.comments_flat

subreddit = r.get_subreddit('pics')
subreddit_comments = subreddit.get_comments()

already_done = []
for comment in subreddit_comments:
    if comment.id not in already_done:
        comment.reply(comment.body)
        already_done.append(comment.id)
        time.sleep(4800)
