#!/usr/bin/env python
# -*- coding: GB18030 -*-

"""
 Name        : sys_config.py
 Created on  : 2017/06/18 11:28
 Author      : Liuker <liu@liuker.xyz>
 Version     : 1.0.0
 Copyright   : Copyright (C) 2013 - 2017, Liuker's Blog, https://liuker.org.
 Description : ϵͳ�����á�
"""
import os

ROOT_PATH = os.path.join(os.path.dirname(__file__), os.pardir)

# ����ı���ַ
REQUEST_URL = "http://life.httpcn.com/xingming.asp"

# �ʵ��ļ�·�����к���˫����
FPATH_DICTFILE_BOYS_DOUBLE = os.path.abspath(os.path.join(ROOT_PATH, "./dicts/boys_double.txt"))
# �ʵ��ļ�·�����к���������
FPATH_DICTFILE_BOYS_SINGLE = os.path.abspath(os.path.join(ROOT_PATH, "./dicts/boys_single.txt"))
# �ʵ��ļ�·����Ů����˫����
FPATH_DICTFILE_GIRLS_DOUBLE = os.path.abspath(os.path.join(ROOT_PATH, "./dicts/girls_double.txt"))
# �ʵ��ļ�·����Ů����������
FPATH_DICTFILE_GIRLS_SINGLE = os.path.abspath(os.path.join(ROOT_PATH, "./dicts/girls_single.txt"))
