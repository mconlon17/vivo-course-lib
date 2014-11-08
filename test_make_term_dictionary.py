"""
    test_make_term_dictionary.py -- query VIVO and return a dictionary
    containing the term entities.  Key is term number, value is URI

    Version 0.0 MC 2014-08-23
    --  Initial version.  Make a dictionary and show first entries
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.0"

from vivocourses import make_term_dictionary
from datetime import datetime

print datetime.now(), "Start"
print datetime.now(), "Making term dictionary"
term_dictionary = make_term_dictionary(debug=True)
print datetime.now(), "term dictionary has ", len(term_dictionary),\
    "entries"
print "datetime.now(), First 20 entries:"
labels = sorted(term_dictionary.keys()[0:20])
for label in labels:
    uri = term_dictionary[label]
    print datetime.now(), label, uri
print datetime.now(), "Finish"
