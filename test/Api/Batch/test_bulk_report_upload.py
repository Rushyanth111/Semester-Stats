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
        res = self.client.post("/batch/", json=data)

        print(res.json())

        self.assertEqual(res.status_code, 201, "Creation of data did not happen")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.close()
