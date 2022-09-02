from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='matching_algorithim',
    version='0.1.0',
    description='matching algorthm for mentor/mentee matching for the UBC URO REX Program',
    long_description=readme,
    author='Melvin Mathews',
    author_email='me@melvinmathews.dev',
    url='https://github.com/melmatt7/matching_algorithim',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)