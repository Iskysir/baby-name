#!/usr/bin/env python
# -*- coding: GB18030 -*-

"""
 Name        : user_config.py
 Created on  : 2017/06/18 11:28
 Author      : Liuker <liu@liuker.xyz>
 Version     : 1.0.0
 Copyright   : Copyright (C) 2013 - 2017, Liuker's Blog, https://liuker.org.
 Description : �û����á�
"""
import os

ROOT_PATH = os.path.join(os.path.dirname(__file__), os.pardir)

setting = {}

# �޶��֣���������˸�ֵ�����ȡ�õ����ֵ䣬����ȡ�ö����ֵ�
setting["limit_world"] = "��"
# ��
setting["name_prefix"] = "��"
# �Ա�ȡֵΪ �� ���� Ů
setting["sex"] = "��"
# ʡ��
setting["area_province"] = "����"
# ����
setting["area_region"] = "����"
# �����Ĺ������
setting['year'] = "2017"
# �����Ĺ����·�
setting['month'] = "6"
# �����Ĺ�������
setting['day'] = "18"
# �����Ĺ���Сʱ
setting['hour'] = "18"
# �����Ĺ�������
setting['minute'] = "18"
# ��������ļ�����
setting['output_fname'] = "example.txt"
setting['output_fpath'] = os.path.abspath(os.path.join(ROOT_PATH, "outputs", setting['output_fname']))
