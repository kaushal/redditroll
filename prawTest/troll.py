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
        if "ironic" in str(comment.body):
            comment.reply("Actually that isn't even ironic. It's just coincidental.")
        elif "idea" in str(comment.body):
            comment.reply("Wow. That's the stupidest idea I have ever heard!")
        print comment.body
        print "\n"

def main():
    USER = "repetition_is_key"
    PASS = "repetition"
    r = praw.Reddit("Just for fun... :P")
    r.login(USER, PASS)
    while True:
        subreddit = r.get_subreddit('all')
        subreddit_comments = subreddit.get_comments()
        postReply(subreddit_comments)
        sleep(300)

if __name__ == '__main__':
    main()
