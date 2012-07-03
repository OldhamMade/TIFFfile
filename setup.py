from setuptools import setup, find_packages
import os, sys

setup(name="TIFFfile",
      description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
      version="2012.06.06",
      url="http://github.com/unpluggd/TIFFfile",
      packages=find_packages(exclude="specs"),
      install_requires=[
          'numpy',
          ],
      )
