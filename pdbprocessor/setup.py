from setuptools import setup
setup(
    name='pdbprocessor',
    version='0.2.0',
    entry_points={
        'console_scripts': [
            'pdbprocessor=pdbprocessor:main'
        ]
    }
)
