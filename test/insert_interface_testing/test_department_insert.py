from test.BaseClassUtils import BaseClassUnitTestCase
import semesterstats.models as model


class DeparmentInsertTest(BaseClassUnitTestCase):
    def setUp(self):
        self.db = model.ModelInterface()
        self.bnc_init()

    def test_insert_department(self):
        d = model.DepartmentModel(DepartmentCode="XTX", DepartmentName="Tester")
        self.db.insert_department(d)

    def test_insert_department_bulk(self):

        d = [
            model.DepartmentModel(
                DepartmentCode=self.fake.gen_usn(), DepartmentName=self.fake.name()
            )
            for _ in range(300)
        ]

        self.db.insert_department_bulk(d)
