import sys
from random import choice

def generate_reply(post):
    """
    Runs through the logic of creating a comment to post as a reply to another post.
    If the post is not worth replying to, an empty string will be returned.

    Arguments:
    post - The post that is potentially being replied to.
    """

    #Makes it easier for comparisons later.
    post = post.lower()

    message = ""

    #Feel free to add any sort of funny, condescending behavior!
    if "ironic" in post:
        message += "Actually, that isn't even ironic. It's just coincidental."
    elif " idea " in post or "idea." in post:
        message += "Wow. That is the stupidest idea I have ever heard."
    else:
        for preposition in prepositions():
            print preposition
            if preposition + "." in post or preposition + "?" in post or preposition + "!" in post:
                message += "Dude. Are you really ending a sentence with a preposition? I used to do that, and then " + random.choice(["my dad got a job.", "I turned 12."])

    if not message == "":
        message += "\nYou " + insulting_adjective() + " " + insulting_noun() + "!"
    return message

def prepositions():
    """
    Returns a random preposition from our list of prepositions.
    """

    try:
        with open("prepositions.txt") as preps:
            return preps.read().split()
    except EnvironmentError:
        print "Dude! make a list of prepositions!"
        sys.exit()

def insulting_adjective():
    """
    Returns a random adjective from our list of offensive adjectives.
    """

    try:
        with open("insulting_adjectives.txt") as adj_list:
            return choice(adj_list.read().split())
    except EnvironmentError:
        print "Dude! Make a list of adjectives!"
        sys.exit()

def insulting_noun():
    """
    Returns a random noun from our list of offensive nouns
    """

    try:
        with open("insulting_nouns.txt") as noun_list:
            return choice(noun_list.read().split())
    except EnvironmentError:
        print "Dude! Make a list of nouns!"
        sys.exit()
