from setuptools import setup
from os.path import abspath, dirname, join

version_file = join(dirname(abspath(__file__)), 'SSHTunnelLibrary', 'version.py')

with open(version_file) as file:
      code = compile(file.read(), version_file, 'exec')
      exec(code)

setup(name='robotframework-sshtunnellibrary',
      version=VERSION,
      description='SSH Tunnel Library for Robot framework',
      author='C-Squad',
      author_email='csquad.dev@gmail.com',   
      license= 'MIT',
      platforms= 'any',
      packages=[
            'SSHTunnelLibrary'
      ],
      install_requires=[
            'robotframework',
            'sshtunnel'
      ])