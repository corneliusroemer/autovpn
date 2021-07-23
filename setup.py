from setuptools import setup

setup(
    name='autovpn',
    version='0.1.0',
    py_modules=['autovpn'],
    install_requires=[
        'Click',
        'sortedcontainers',
        'toml',
    ],
    entry_points={
        'console_scripts': [
            'autovpn = autovpn:cli',
        ],
    },
)
