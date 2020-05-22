import random
import string
import unittest

from faker import Faker
from faker.providers import BaseProvider


class SemesterStatsProvider(BaseProvider):
    def __init__(self, generator):
        super().__init__(generator)
        self.letters = string.ascii_uppercase + "1234567890"

    def gen_usn(self):
        return self.bothify("#??##??###", letters=self.letters)

    def gen_subject_code(self):
        if random.randint(0, 100) % 5 == 0:
            return self.bothify("##??L##", letters=self.letters)
        else:
            return self.bothify("##??##", letters=self.letters)

    def gen_batch(self):
        pass

    def gen_scheme(self):
        pass


class BaseClassUnitTestCase(unittest.TestCase):
    def bnc_init(self):
        self.fake = Faker()
        self.fake.add_provider(SemesterStatsProvider)
