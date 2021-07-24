from setuptools import setup

setup(
    name="autovpn",
    description="A CLI wrapper for Cisco's Anyconnect VPN tool",
    license="MIT",
    author="Cornelius Roemer",
    url="https://github.com/corneliusroemer/autovpn",
    version="0.2.0",
    py_modules=["autovpn"],
    install_requires=[
        "Click",
        "sortedcontainers",
        "toml",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "autovpn = autovpn:cli",
        ],
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Operating System :: POSIX",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: System :: Networking",
        "Topic :: Utilities",
    ],
    keywords="cli wrapper cisco anyconnect vpn passwordless",
    project_urls={
        "Documentation": "https://github.com/corneliusroemer/autovpn",
        "Source": "https://github.com/corneliusroemer/autovpn",
        "Tracker": "https://github.com/corneliusroemer/autovpn/issues",
    },
)
