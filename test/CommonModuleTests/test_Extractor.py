from semesterstat.common.extractor import (
    batch_from_usn,
    dept_from_usn,
    semester_from_subject,
    scheme_from_subject,
    dept_from_subject,
)

import unittest


class ExtractorTest(unittest.TestCase):
    def setUp(self):
        self.sample_usn = (
            ("1CR17CS117", 2017, "CS"),
            ("1CR16IS117", 2016, "IS"),
            ("1CR14ME117", 2014, "ME"),
            ("1CR10CV117", 2010, "CV"),
            ("1CR18EE117", 2018, "EE"),
        )

    def test_batch_from_usn(self):
        for query, batch, dept in self.sample_usn:
            assert batch_from_usn(query) == batch

    def test_dept_from_usn(self):
        for query, batch, dept in self.sample_usn:
            assert dept_from_usn(query) == dept

    def test_semester_from_subject(self):
        pass

    def test_scheme_from_subject(self):
        pass

    def test_dept_from_subject(self):
        pass
