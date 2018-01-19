from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    long_description = readme_file.read()

# Get the version number from VERSION file
with open(path.join(here, 'VERSION'), encoding='utf-8') as version_file:
    version = version_file.read().strip()

setup(
    name='{{cookiecutter.package_name}}',
    version=version,
    description='{{cookiecutter.description}}',
    long_description=long_description,
    url='https://github.com/XiaochenCui/{{cookiecutter.repo_name}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    license='GPLv3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ],

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords='',  # Optional

    install_requires=[],
    packages=find_packages(exclude=['tests']),
)
