import unittest
import semesterstats.models as model


class TestInsertInterface(unittest.TestCase):
    def test_insert_interface(self):
        d = model.DepartmentStructure(Code="XTX", Name="Tester")
        x = model.ModelInterface()
        self.assertEqual(x.insert_department(d), True)


if __name__ == "__main__":
    unittest.main()
