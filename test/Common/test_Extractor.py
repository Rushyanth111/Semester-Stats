from semesterstat.common import (
    get_usn_batch,
    get_usn_dept,
    get_subject_semester,
    get_subject_scheme,
    get_subject_dept,
    is_usn_diploma,
    is_subject_lab,
)

import unittest


class UsnExtractorTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.sample_usn = (
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

    def test_batch(self):
        for query, batch, dept, diploma in self.sample_usn:
            assert get_usn_batch(query) == batch

    def test_dept(self):
        for query, batch, dept, diploma in self.sample_usn:
            assert get_usn_dept(query) == dept

    def test_diploma(self):
        for query, batch, dept, diploma in self.sample_usn:
            assert is_usn_diploma(query) == diploma


class SubjectExtractorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sample_subcodes = (
            ("17CS41", 4, 2017, "CS", False),
            ("15MATDIP31", 3, 2015, "XX", False),
            ("18ECS84", 8, 2018, "EC", False),
            ("18ECMP68", 6, 2018, "EC", False),
            ("18ECL67", 6, 2018, "EC", True),
            ("15EC553", 5, 2015, "EC", False),
        )

    def test_semester(self):
        for query, sem, scheme, dept, lab in self.sample_subcodes:
            assert get_subject_semester(query) == sem

    def test_scheme(self):
        for query, sem, scheme, dept, lab in self.sample_subcodes:
            assert get_subject_scheme(query) == scheme

    def test_dept(self):
        for query, sem, scheme, dept, lab in self.sample_subcodes:
            assert get_subject_dept(query) == dept

    def test_lab(self):
        for query, sem, scheme, dept, lab in self.sample_subcodes:
            assert is_subject_lab(query) == lab
