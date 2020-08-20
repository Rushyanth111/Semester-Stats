from semesterstat.api import app
from fastapi.testclient import TestClient

from test.BaseForDB import CommonTestClass

"""
Part of Integration Testing, Everything Else has been Tested.

- test default:
    - batch only
        - with dept
        - with sem
        - dept + sem

- test Params
    - test invalid List + Detail Request as a 404.

- test detain
    - detain only
        - with dept
        - with sem
        - dept + sem
    - detain + listusn
        - with dept
        - with sem
        - dept + sem
    - detain + detail
        - with dept
        - with sem
        - dept + sem
    - detain + backlogs
        - with dept
        - with sem
        - dept + sem
    - detain + listusn + backlogs
        - with dept
        - with sem
        - dept + sem

- test listusn
    - listusn only
        - with dept
        - with sem
        - dept + sem
    - listusn + backlogs
        - with dept
        - with sem
        - dept + sem

- test backlogs
    - only backlogs
        - with dept
        - with sem
        - dept + sem

"""


class ApiBatchTest(CommonTestClass):
    @classmethod
    def setUpClass(cls) -> None:
        super(ApiBatchTest, cls).setUpClass()
        cls.client = TestClient(app)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.close()
        super(ApiBatchTest, cls).tearDownClass()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass
