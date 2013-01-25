import praw
import time

def populateWordDict(dict):
	f = open("partsOfSpeech/nouns.txt", "r")
	for line in f:
		dict['nouns'].append(line)
	f = open("partsOfSpeech/verbs.txt", "r")
	for line in f:
		dict["verbs"].append(line)

	return dict

def postReply(comments):
	for comment in comments:
		if comment.id not in already_done:
			print comment.body
			#comment.reply(comment.body)
			already_done.append(comment.id)


def main():
	USER = "not_a_trollbot"
	PASS = "trollbot"
	r = praw.Reddit("Just for fun... :P")
	r = praw.login(USER, PASS)
	submission = r.get_submission(submission_id='11v36o')
	flat_comments = submission.comments_flat
	
	subreddit = r.get_subreddit('all')
	subreddit_comments = subreddit.get_comments()
	postReply(subreddit_comments)

