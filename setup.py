"""Setup Package Configuration
"""
from setuptools import setup, find_packages


setup(
    name="treescript-diff",
    version="0.1",
    description="Determines the difference between two TreeScript files.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="DK96-OS",
    url="https://github.com/DK96-OS/treescript-diff",
    project_urls={
        "Issues": "https://github.com/DK96-OS/treescript-diff/issues",
        "Source Code": "https://github.com/DK96-OS/treescript-diff"
    },
    license="GPLv3",
    packages=find_packages(exclude=['test']),
    entry_points={
        'console_scripts': [
            'treescript-diff=treescript_diff.__main__:main',
            'treescript_diff=treescript_diff.__main__:main',
        ],
    },
    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
