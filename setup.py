from setuptools import setup, find_packages

name = 'joistpy'
version = '0.1.3'
author = 'Matthew Upshaw'
author_email = 'matthew.upshaw02@gmail.com'
description = 'Library that acts as a database for SJI steel open web bar joist shapes for easy use in structural calculations.'
packages = find_packages()
package_data = {
    'joistpy': ['property files/*.csv'],
}
classifiers = [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Operating System :: OS Independent',
]
python_requires = '>=3.8'

setup(name=name, version=version, author=author, author_email=author_email, description=description, packages=packages, package_data=package_data, classifiers=classifiers, python_requires=python_requires)
