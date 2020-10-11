import pytest

from semesterstat.common.usn_extractor import (
    get_usn_batch,
    get_usn_dept,
    is_usn_diploma,
)


@pytest.mark.parametrize(
    ["query", "batch", "dept", "diploma"],
    [
        ("1CR17CS117", 2017, "CS", False),
        ("1CR16IS113", 2016, "IS", False),
        ("1CR14ME154", 2014, "ME", False),
        ("1CR10CV161", 2010, "CV", False),
        ("1CR18EE222", 2018, "EE", False),
        ("1RV18EC410", 2017, "EC", True),
        ("1RV18EC400", 2017, "EC", True),
        ("1RV18EC405", 2017, "EC", True),
        ("1RV18EC405", 2017, "EC", True),
        ("1RV15EC405", 2014, "EC", True),
        ("1RV15EC404", 2014, "EC", True),
        ("1RV15EC404", 2014, "EC", True),
    ],
)
class TestUsnExtractor:
    def test_batch(self, query, batch, dept, diploma):
        assert get_usn_batch(query) == batch

    def test_dept(self, query, batch, dept, diploma):
        assert get_usn_dept(query) == dept

    def test_diploma(self, query, batch, dept, diploma):
        assert is_usn_diploma(query) == diploma
