"""
    test_make_section_rdf.py -- given a course section structure,
    make RDF for the section and roles that link the section to term,
    instructor and course

    Version 0.1 MC 2014-08-23
    --  Initial version.
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.1"

from vivocourses import make_section_rdf
from datetime import datetime

section_data = {
    "section_name": "AST4035 Spring 2014 3553",
    "section_number": "3553",
    "term_uri": "http://term_uri",
    "course_uri": "http://course_uri",
    "course_name": "The Planets Except Pluto",
    "course_new": False,
    "person_uri": "http://person_uri"
}


print datetime.now(), "Start"

[rdf, section_uri] = make_section_rdf(section_data)
print "Section for existing course uri=", section_uri
print rdf

section_data['course_new'] = True
[rdf, section_uri] = make_section_rdf(section_data)
print "Section for new course uri=", section_uri
print rdf

print datetime.now(), "Finish"