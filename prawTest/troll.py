import praw
from time import sleep
import condescending
import random

#List of accounts of our bots
__accounts = ["repetition_is_key"]

def populateWordDict(dict):
    f = open("partsOfSpeech/nouns.txt", "r")
    for line in f:
        dict['nouns'].append(line)
    f = open("partsOfSpeech/verbs.txt", "r")
    for line in f:
        dict["verbs"].append(line)

    return dict

def postReply(comments):
    already_done = []
    for comment in comments:
		reply = condescending.generate_reply(str(comment.body))
		if not reply == "":
			comment.reply(reply)
        print comment.body
        print "\n"

def switch_accounts(current_acc):
    """
    Returns a different account than current_acc to be logged in
    """
    new_acc = random.choice(__accounts)
    while not new_acc == current_acc:
        return new_acc

def main():
    USER = ""
    while True:
        r = praw.Reddit("Just for fun... :P")
        USER = switch_accounts(USER)
        r.login(USER, "repetition")
        while True:
            subreddit = r.get_subreddit('all')
            subreddit_comments = subreddit.get_comments()
            postReply(subreddit_comments)
            sleep(300)

if __name__ == '__main__':
    main()
