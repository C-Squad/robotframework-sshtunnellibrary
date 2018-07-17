from setuptools import setup
from os.path import abspath, dirname, join

with open(join(dirname(abspath(__file__)), 'SSHTunnelLibrary', 'version.py')) as f:
    VERSION = re.search("\nVERSION = '(.*)'", f.read()).group(1)

CLASSIFIERS = '''
Development Status :: 5 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()
      
DESCRIPTION = ""
with open(join(CURDIR, 'README.md')) as f:
    DESCRIPTION = f.read()

setup(name='robotframework-sshtunnellibrary',
      version=VERSION,
      description='SSH Tunnel Library for Robot framework',
      author='C-Squad',
      author_email='csquad.dev@gmail.com',
      license= 'Apache-2.0',
      long_description=DESCRIPTION,
      url='https://github.com/C-Squad/robotframework-sshtunnellibrary',
      platforms= 'any',
      classifiers=CLASSIFIERS,
      packages=[
            'SSHTunnelLibrary'
      ],
      install_requires=[
            'robotframework',
            'sshtunnel'
      ])
