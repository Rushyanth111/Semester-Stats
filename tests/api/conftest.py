from fastapi.testclient import TestClient
from semesterstat.api import app
from shutil import copy2
from distutils.dir_util import copy_tree
import pytest
import os


@pytest.fixture(scope="package")
def create_env(tmpdir_factory):
    respath = tmpdir_factory.mktemp("Resources", False)
    basepath = tmpdir_factory.getbasetemp()
    copy_tree("Resources", str(respath))
    copy2("config.ini", str(basepath))
    os.chdir(basepath)


@pytest.fixture(scope="package")
def client(create_env):
    with TestClient(app) as cl:
        yield cl
