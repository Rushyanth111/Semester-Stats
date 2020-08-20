from setuptools import setup, find_packages
import glob

setup(
    name="semesterstat",
    version="0.1",
    packages=find_packages(),
    maintainer="Rushyanth111",
    maintainer_email="Rushyanth111@gmail.com",
    description="A Program to automate everything VTU",
    data_files=[
        ("datafiles", glob.glob("FormattedData/*")),
        ("resources", glob.glob("Resources/*")),
    ],
    zip_safe=False,
    py_modules=["semesterstat"],
)
