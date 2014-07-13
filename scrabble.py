#!/usr/bin/env python
import argparse
import itertools
import string
import sqlite3
from collections import defaultdict
from colorama import init, Fore


def get_frequency(word):
    freq = {}
    for w in word:
        freq[w] = freq.get(w, 0) + 1
    return freq


def get_query_snippet(word):
    fq = get_frequency(word)
    word = set(word)
    query = []
    for letter in string.ascii_lowercase:
        if letter not in word:
            query.append("%s == 0" % (letter,))
        else:
            freq = fq.get(letter)
            query.append("%s <= %d" % (letter, freq))
    return " AND ".join(query)


def solver(word, longer=False, shorter=False):
    if '?' not in word:
        return get_query_snippet(word)

    i = word.count('?')
    word = word.replace('?', '')

    query = []
    # Grab all possible permutations for the number of question marks there are
    combinations = itertools.combinations_with_replacement(string.ascii_lowercase, i)
    for c in combinations:
        query.append("(%s)" % (get_query_snippet(word + "".join(c))))

    return " OR ".join(query)


def starts(word):
    return "SELECT length, word from words WHERE word LIKE '%s%%'" % word


def ends(word):
    return "SELECT length, word from words WHERE word LIKE '%%%s'" % word


def contains(word):
    return "SELECT length, word from words WHERE word LIKE '%%%s%%'" % word


def display(what):
    init()
    for length, words in what.iteritems():
        print Fore.RED, length
        print Fore.WHITE, "\t".join(sorted(words))


parser = argparse.ArgumentParser()
parser.add_argument(
    'letters',
    nargs='?',
    help='String of letters to find. Use ? for blank tiles.',
)
parser.add_argument(
    '--starts',
)
parser.add_argument(
    '--ends',
)
parser.add_argument(
    '--contains',
)
parser.add_argument(
    '--longer',
    type=int,
    help='Return words longer than',
)
parser.add_argument(
    '--shorter',
    type=int,
    help='Return words shorter than',
)

args = parser.parse_args()
# If letters exist then get all matching words and filter on them
if args.letters:
    extras = []
    if args.longer:
        extras.append("length > %d" % args.longer)
    if args.shorter:
        extras.append("length < %d" % args.shorter)
    extras.append("(" + solver(args.letters, args.longer) + ")")
    query = "SELECT DISTINCT length, words FROM anagrams WHERE %s" % (" AND ".join(extras),)

    # Connect and run query
    c = sqlite3.connect('words.db').cursor()
    word_sets = defaultdict(set)
    for length, words in c.execute(query).fetchall():
        ws = words.split(",")
        ws = [w for w in ws
              if (not args.starts or (args.starts and w.startswith(args.starts)))
              and (not args.ends or (args.ends and w.endswith(args.ends)))
              and (not args.contains or (args.contains and args.contains in w))]

        if ws:
            word_sets[length].update(ws)

else:
    if args.contains:
        query = contains(args.contains)
    elif args.starts:
        query = starts(args.contains)
    elif args.ends:
        query = ends(args.ends)

    c = sqlite3.connect('words.db').cursor()
    word_sets = defaultdict(set)
    for length, words in c.execute(query).fetchall():
        word_sets[length].update([words])

display(word_sets)
