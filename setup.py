from setuptools import setup
import os
import sys

if (sys.version_info.major == 3 and sys.version_info.minor == 6) or\
    (sys.version_info.major == 3 and sys.version_info.minor == 7) or\
    (sys.version_info.major == 3 and sys.version_info.minor == 8) or\
    (sys.version_info.major == 3 and sys.version_info.minor == 9) or\
    (sys.version_info.major == 3 and sys.version_info.minor == 10):
    print('[SETUP] bayeso supports Python {}.{} version in this system.'.format(sys.version_info.major, sys.version_info.minor))
else:
    sys.exit('[ERROR] bayeso does not support Python {}.{} version in this system.'.format(sys.version_info.major, sys.version_info.minor))

path_requirements = 'requirements.txt'
list_packages = [
    'bayeso',
    'bayeso.bo',
    'bayeso.gp',
    'bayeso.tp',
    'bayeso.trees',
    'bayeso.wrappers',
    'bayeso.utils'
]

with open(path_requirements) as f:
    required = f.read().splitlines()

setup(
    name='bayeso',
    version='0.5.3',
    author='Jungtaek Kim',
    author_email='jtkim@postech.ac.kr',
    url='https://bayeso.org',
    license='MIT',
    description='Simple, but essential Bayesian optimization package',
    packages=list_packages,
    python_requires='>=3.6, <4',
    install_requires=required,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)
