import random
from urllib.request import urlopen
import sys

from pip._vendor.distlib.compat import raw_input

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class uci(mika):":
      "Make a class named uci that is-a mika.",
    "class uci(object):\n\tdef __init__(self, aka)" :
      "class uci has-a __init__ that takes self and aka parameters.",
    "class uci(object):\n\tdef afen(self, aka)":
      "class uci has-a function named afen that takes self and aka parameters.",
    "foo = uci()":
      "Set foo to an instance of class uci.",
    "foo.afen(aka)":
      "From foo get the afen function, and call it with parameters self, aka.",
    "foo.widia = 'anisa'":
      "From foo get the widia attribute and set it to 'anisa'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("uci"))]
    other_names = random.sample(WORDS, snippet.count("aka"))
    results = []
    param_names = []

    for i in range(0, snippet.count("aka")):
        param_count = random.randint(1,3)
        param_names.append(','.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("mika", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("uci", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("aka", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print ('question'())

            raw_input("> ")
            print ("ANSWER:  %s\n\n" % answer)
except EOFError:
    print ("\nBye")