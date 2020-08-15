from semesterstat.common.extractor import (
    batch_from_usn,
    dept_from_usn,
    semester_from_subject,
    scheme_from_subject,
    dept_from_subject,
    is_diploma,
    is_lab,
)

import unittest


class ExtractorTest(unittest.TestCase):
    def setUp(self):
        self.sample_usn = (
            ("1CR17CS117", 2017, "CS", False),
            ("1CR16IS113", 2016, "IS", False),
            ("1CR14ME154", 2014, "ME", False),
            ("1CR10CV161", 2010, "CV", False),
            ("1CR18EE222", 2018, "EE", False),
            ("1RV18EC410", 2018, "EC", True),
            ("1RV18EC400", 2018, "EC", True),
            ("1RV18EC405", 2018, "EC", True),
            ("1RV18EC405", 2018, "EC", True),
            ("1RV15EC405", 2015, "EC", True),
            ("1RV15EC404", 2015, "EC", True),
            ("1RV15EC404", 2015, "EC", True),
        )

        self.sample_subcodes = (
            ("17CS41", 4, 2017, "CS", False),
            ("15MATDIP31", 3, 2015, "XX", False),
            ("18ECS84", 8, 2018, "EC", False),
            ("18ECMP68", 6, 2018, "EC", False),
            ("18ECL67", 6, 2018, "EC", True),
            ("15EC553", 5, 2015, "EC", False),
        )

    def test_batch_from_usn(self):
        for query, batch, dept, diploma in self.sample_usn:
            assert batch_from_usn(query) == batch

    def test_dept_from_usn(self):
        for query, batch, dept, diploma in self.sample_usn:
            assert dept_from_usn(query) == dept

    def test_is_diploma(self):
        for query, batch, dept, diploma in self.sample_usn:
            assert is_diploma(query) == diploma

    def test_semester_from_subject(self):
        for query, sem, scheme, dept, lab in self.sample_subcodes:
            assert semester_from_subject(query) == sem

    def test_scheme_from_subject(self):
        for query, sem, scheme, dept, lab in self.sample_subcodes:
            assert scheme_from_subject(query) == scheme

    def test_dept_from_subject(self):
        for query, sem, scheme, dept, lab in self.sample_subcodes:
            assert dept_from_subject(query) == dept

    def test_is_lab(self):
        for query, sem, scheme, dept, lab in self.sample_subcodes:
            assert is_lab(query) == lab
