from setuptools import setup

setup(
    name='spark-testing-base',
<<<<<<< HEAD
    version='0.6.1',
=======
    version='0.7.0',
>>>>>>> upstream/master
    author='Holden Karau',
    author_email='holden@pigscanfly.ca',
    packages=['sparktestingbase', 'sparktestingbase.test'],
    url='https://github.com/holdenk/spark-testing-base',
    license='LICENSE.txt',
    description='Spark testing for python',
    long_description='',
    install_requires=[
        'unittest2',
        'findspark',
        'pytest'
    ],
    test_requires=[
        'nose',
        'coverage',
        'unittest2'
    ],
)
