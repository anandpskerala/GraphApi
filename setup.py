import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='GraphApi',
      version='0.1.1',
      description='API wrapper for Microsoft Graph written in Python',
      long_description=read('README.md'),
      url='https://github.com/anandpskerala/GraphApi',
      long_description_content_type="text/markdown",
      author='Anand',
      author_email='anandps002@gmail.com',
      license='MIT',
      packages=['GraphApi'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)