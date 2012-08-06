#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def run_setup():
    setup(
        name='metranome',
        version='0.0.1',
        description='An AMQP Cron-like system',
        keywords = 'AMQP',
        url='http://github.com/philipcristiano/metranome',
        author='Philip Cristiano',
        author_email='metranome@philipcristiano.com',
        license='BSD',
        packages=[],
        install_requires=[
            'pika'
        ],
        test_suite='tests',
        long_description=read('README.md'),
        zip_safe=True,
        classifiers=[
        ],
        entry_points="""
        [console_scripts]
            metranome=metranome.main:main
        """,
    )

if __name__ == '__main__':
    run_setup()
