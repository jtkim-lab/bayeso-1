from setuptools import setup
import os
import sys

if (sys.version_info.major == 2 and sys.version_info.minor == 7) or\
    (sys.version_info.major == 3 and sys.version_info.minor == 5) or\
    (sys.version_info.major == 3 and sys.version_info.minor == 6):
    print('[SETUP] bayeso supports Python {}.{} version in this system.'.format(sys.version_info.major, sys.version_info.minor))
else:
    sys.exit('[ERROR] bayeso does not support Python {}.{} version in this system.'.format(sys.version_info.major, sys.version_info.minor))

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='bayeso',
    version='0.3.2',
    author='Jungtaek Kim',
    author_email='jtkim@postech.ac.kr',
    url='https://github.com/jungtaekkim/bayeso',
    license='MIT',
    description='Bayesian optimization package',
    packages=['bayeso', 'bayeso.utils'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, != 3.3.*, !=3.4.*, <4',
    install_requires=required,
)
