from setuptools import setup, find_packages

import boringCalc


VERSION = '0.0.1'
DESCRIPTION = 'A very simple calculator app.'
LONG_DESCRIPTION = 'A calculator with 4 functions (addition, subtraction, multiplication and division) plus a neat little rating system a the end.'

# Setting up
setup(
    name="boringCalc",
    version=VERSION,
    author="Dean James (deanjames1)",
    author_email="deanomcardle@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(where="boringCalc"),
    install_requires=[],
    keywords=['python', 'calculator'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)