"""
    test_make_course_dictionary.py -- query VIVO and return a dictionary
    containing the course entities.  Key is course number, value is URI

    Version 0.0 MC 2014-08-23
    --  Initial version.  Make a dictionary and show first entries
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.0"

from vivocourses import make_course_dictionary
from datetime import datetime

print datetime.now(), "Start"
print datetime.now(), "Making course dictionary"
course_dictionary = make_course_dictionary(debug=True)
print datetime.now(), "Course dictionary has ", len(course_dictionary),\
    "entries"
print "datetime.now(), First 20 entries:"
labels = sorted(course_dictionary.keys()[0:20])
for label in labels:
    uri = course_dictionary[label]
    print datetime.now(), label, uri
print datetime.now(), "Finish"
