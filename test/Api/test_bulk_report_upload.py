import unittest
from fastapi.testclient import TestClient
from semesterstat.api import app


class BulkReportTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app)

    def test_upload_bulk(self):
        data = [
            {
                "Usn": "1CR17CS117",
                "Name": "Some Random Name",
                "Subcode": "17CS51",
                "Subname": "Enterprenuership and Something LOL",
                "Internals": 5,
                "Externals": 20,
            }
        ]
        res = self.client.post("/bulk/", json=data)

        self.assertEqual(res.status_code, 201, "Creation of data did not happen")

    def test_upload_bulk_conflict(self):
        data = [
            {
                "Usn": "1CR17CS115",
                "Name": "Some Random Name",
                "Subcode": "17CS51",
                "Subname": "Enterprenuership and Something LOL",
                "Internals": 5,
                "Externals": 20,
            },
            {
                "Usn": "1CR17CS115",
                "Name": "Some Random Name",
                "Subcode": "17CS51",
                "Subname": "Enterprenuership and Something LOL",
                "Internals": 5,
                "Externals": 20,
            },
        ]

        res = self.client.post("/bulk/", json=[data[0]])

        self.assertEqual(res.status_code, 201)

        res = self.client.post("/batch/", json=[data[1]])

        self.assertEqual(res.status_code, 201)
