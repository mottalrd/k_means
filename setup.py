from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("./requirements.txt", session=PipSession())

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(name='KMeans',
      version='1.0',
      description='A simple K means implementation',
      author='Alfredo Motta',
      package_dir = {'': 'lib'},
      packages=[''],
      install_requires=reqs)
