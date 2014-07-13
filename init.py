from collections import Counter
from models import Anagram, Word, get_session


s = get_session()
words = {}
# Loads all the words into the database
with open('./TWL06.txt', 'rb') as f:
    for word in f.read().splitlines():
        # Create a dictionary of words
        lowered = word.lower()
        sort = "".join(sorted(lowered))
        entry = words.get(sort, "")
        if entry:
            entry += ","
        words[sort] = entry + lowered

        # Add the word into the database
        s.add(Word(
            word=lowered,
            length=len(sort),
        ))

for sort, anagrams in words.iteritems():
    count = Counter(sort)
    s.add(Anagram(
        sorted=sort,
        words=anagrams,
        length=len(sort),
        a=count.get('a', 0),
        b=count.get('b', 0),
        c=count.get('c', 0),
        d=count.get('d', 0),
        e=count.get('e', 0),
        f=count.get('f', 0),
        g=count.get('g', 0),
        h=count.get('h', 0),
        i=count.get('i', 0),
        j=count.get('j', 0),
        k=count.get('k', 0),
        l=count.get('l', 0),
        m=count.get('m', 0),
        n=count.get('n', 0),
        o=count.get('o', 0),
        p=count.get('p', 0),
        q=count.get('q', 0),
        r=count.get('r', 0),
        s=count.get('s', 0),
        t=count.get('t', 0),
        u=count.get('u', 0),
        v=count.get('v', 0),
        w=count.get('w', 0),
        x=count.get('x', 0),
        y=count.get('y', 0),
        z=count.get('z', 0),
    ))

s.commit()
