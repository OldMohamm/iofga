#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : iofga - Email OSINT
# @url    : http://github.com/OldMohamm
# @author : Mohammed AMer (OldMohamm)

from setuptools import setup 

setup(
    name='iofga',

    version='0.1.5',
    description='Email OSINT',
    url='https://github.com/OldMohamm',
    
    author = 'Mohammed  (OldMohamm) Amer',
    author_email='fbiarabic@gmail.com',
    license='GPLv3',

    install_requires = ['colorama','requests','urllib3'],
    console =['iofga.py'],
)