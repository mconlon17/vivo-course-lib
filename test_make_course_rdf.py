"""
    test_make_course_rdf.py -- given a course course structure,
    make RDF for the course and roles that link the course to term,
    instructor and course

    Version 0.1 MC 2014-08-23
    --  Initial version.
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.1"

from vivocourses import make_course_rdf
from datetime import datetime

course_data = {
    "course_number": "3553",
    "course_name": "The Planets Except Pluto",
    "person_uri": "http://person_uri"
}

print datetime.now(), "Start"

[rdf, course_uri] = make_course_rdf(course_data)
print "course for existing course uri=", course_uri
print rdf

print datetime.now(), "Finish"
