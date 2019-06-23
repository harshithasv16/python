from setuptools import setup

setup(
    name="buddy",
    version="0.1",
    packages=['src'],
    py_modules = ['src.launch','src.chain','src.util'],
    install_requires=[
        'click',
    ],
    # console script entrypont
    entry_points='''
        [console_scripts]
        buddy=src.launch:work
    ''',
)
