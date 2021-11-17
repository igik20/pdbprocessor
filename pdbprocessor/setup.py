from setuptools import setup
setup(
    name='pdbprocessor',
    version='Alpha 0.1',
    entry_points={
        'console_scripts': [
            'pdbprocessor=pdbprocessor:main'
        ]
    }
)