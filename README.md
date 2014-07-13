Scrabble Solver
===============

Inspired by scrabblefinder.com and samwho/scrabble-solver.

Uses TWL06 dictionary and sqlite database to quickly find words.

Requirements
------------

* Python 2.7+
* colorama
* sqlalchemy
* sqlite3

To install database:

    $ python init.py

To use:

    $ ./scrabble.py "lttrse"
    $ ./scrabble.py --help
    $ ./scrabble.py "ltterse" --starts "let" --contains "ter" --ends "s" --longer 4 --shorter 8

API:

    * --starts
    * --contains
    * --ends
    * --longer
    * --shorter

The filters can be used in combination with each other. They can also be used outside the context of a given number of tiles. e.g. `./scrabble.py --starts "ze"` will list all known words which start with 'ze'.
