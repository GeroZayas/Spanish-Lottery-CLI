from setuptools import setup

setup(
    name='my_module',
    version='1.0',
    packages=['my_module'],
    entry_points={
        'console_scripts': [
            'my_module=my_module.__main__:main'
        ]
    }
)
