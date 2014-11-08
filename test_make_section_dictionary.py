"""
    test_make_section_dictionary.py -- query VIVO and return a dictionary
    containing the section entities.  Key is section number, value is URI

    Version 0.0 MC 2014-08-23
    --  Initial version.  Make a dictionary and show first entries
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.0"

from vivocourses import make_section_dictionary
from datetime import datetime

print datetime.now(), "Start"
print datetime.now(), "Making section dictionary"
section_dictionary = make_section_dictionary(debug=True)
print datetime.now(), "section dictionary has ", len(section_dictionary),\
    "entries"
print datetime.now(), "First 20 entries:"
labels = sorted(section_dictionary.keys()[0:20])
for label in labels:
    uri = section_dictionary[label]
    print datetime.now(), label, uri
print datetime.now(), "Finish"
