import praw
from time import sleep

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
        if comment.id not in already_done:
            comment.reply(comment.body)
            already_done.append(comment.id)


def main():
    USER = "repetition_is_key"
    PASS = "repetition"
    r = praw.Reddit("Just for fun... :P")
    r.login(USER, PASS)
    submission = r.get_submission(submission_id='11v36o')
    #flat_comments = submission.comments_flat

    subreddit = r.get_subreddit('all')
    subreddit_comments = subreddit.get_comments()
    postReply(subreddit_comments)

if __name__ == '__main__':
    main()
