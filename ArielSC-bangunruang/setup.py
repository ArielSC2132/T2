from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'bangun ruang'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="ArielSC-bangunruang",
    version=VERSION,
    author="M Ariel",
    author_email="<smrgariel@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/loliktry/pyPi-module',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['bangun','ruang'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)