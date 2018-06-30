from setuptools import setup
from os.path import abspath, dirname, join

version_file = join(dirname(abspath(__file__)), 'SSHTunnelLibrary', 'version.py')

with open(version_file) as file:
      code = compile(file.read(), version_file, 'exec')
      exec(code)

setup(name='robotframework-sshtunnel',
      version=VERSION,
      description='SSH Tunnel Library for Robot framework',
      author='',
      author_email='',    
      packages=[
            'SSHTunnelLibrary'
      ],
      install_requires=[
            'robotframework',
            'sshtunnel'
      ])