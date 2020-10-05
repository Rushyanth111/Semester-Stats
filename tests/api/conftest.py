import os
from distutils.dir_util import copy_tree
from shutil import copy2

import pytest
from fastapi.testclient import TestClient

from semesterstat.api import app


@pytest.fixture(scope="package", autouse=True)
def create_env(rootdir, tmp_path_factory):
    respath = tmp_path_factory.mktemp("Resources", False)
    basepath = tmp_path_factory.getbasetemp()
    copy_tree("Resources", str(respath))
    copy2("config.ini", str(basepath))
    os.chdir(basepath)
    yield
    os.chdir(rootdir)


@pytest.fixture(scope="module")
def client(create_env):
    with TestClient(app) as cl:
        yield cl
