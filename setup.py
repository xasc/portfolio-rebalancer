# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

name = 'rebalance'
description = (
    'A web app to make portfolio rebalancing easy.'
)
version = '0.0.0'


setup(
    name=name,
    version=version,
    description=description,
    author='Christoph Sax',
    author_email='c_sax@mailbox.org',
    packages=find_packages(),
    namespace_packages=['rebalance'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'morepath'
    ],
    extras_require=dict(
        test=[
            'pytest',
            'webtest',
        ],
    ),
    entry_points=dict(
        console_scripts=[
            'rebalance-start = rebalance.server.__main__:run',
        ],
    ),
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Programming Language :: Python :: 3.5',
    ]
)
