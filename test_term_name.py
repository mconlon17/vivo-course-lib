
"""
    test_term_name.py -- given a UF term number, return a spelled out
    term name.

    Version 0.0 MC 2014-08-23
    --  Initial version.  For various term numbers, print out term names
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.0"

from vivocourses import term_name
from vivocourses import NoSuchAcademicTermException
from datetime import datetime

print datetime.now(), "Start"
term_numbers = ["20135", "20121", "20122", "145", "", None, "20148"]
for term_number in term_numbers:
    try:
        print datetime.now(), term_number, term_name(term_number)
    except NoSuchAcademicTermException:
        print "No such academic term", term_number
print datetime.now(), "Finish"
