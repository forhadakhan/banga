# setup.py
from setuptools import setup, find_packages

setup(
    name='banga',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'banga = banga.module:main_function',
        ],
    },
    author='Forhad Khan (forhadakhan)',
    description='Unified Bengali Tools Package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
