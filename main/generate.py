#!/usr/bin/env python
# -*- coding: GB18030 -*-


"""
 Name        : get_name_score.py
 Created on  : 2017/06/18 11:27
 Author      : Liuker <liu@liuker.xyz>
 Version     : 1.0.0
 Copyright   : Copyright (C) 2013 - 2017, Liuker's Blog, https://liuker.org.
 Description : �� http://life.main.com/xingming.asp ��ַ���������Ա������Զ��ύ��������ȡ���ҳ���еķ��������
"""

# config
from config import sys_config
from config import user_config
# app
import re
import sys
import urllib
import urllib2
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("GB18030")


def get_name_postfixs():
    """
        �����Ƿ�ʹ�õ��ֺ��û����õ��Ա��������ȡ���е������б�
    :return: �����б�
    """
    target_name_postfixs = set()

    # �Ƿ��е�������
    has_limit_word = False
    limit_word = user_config.setting["limit_world"]
    if limit_word is not None and len(limit_word) > 0:
        has_limit_word = True

    if has_limit_word:
        if user_config.setting["sex"] == "��":
            fpath_input = sys_config.FPATH_DICTFILE_BOYS_SINGLE
        elif user_config.setting["sex"] == "Ů":
            fpath_input = sys_config.FPATH_DICTFILE_GIRLS_SINGLE

        for line in open(sys_config.FPATH_DICTFILE_BOYS_SINGLE):
            iter_name = str(line).strip()
            target_name_postfixs.add("%s%s" % (iter_name, limit_word))
            target_name_postfixs.add("%s%s" % (limit_word, iter_name))
    else:
        if user_config.setting["sex"] == "��":
            fpath_input = sys_config.FPATH_DICTFILE_BOYS_DOUBLE
        elif user_config.setting["sex"] == "Ů":
            fpath_input = sys_config.FPATH_DICTFILE_GIRLS_DOUBLE

        for line in open(fpath_input):
            iter_name = str(line).strip()
            target_name_postfixs.add(iter_name)

    return target_name_postfixs


def compute_name_score(name_postfix):
    """
        ���ýӿڣ�ִ�м��㣬���ؽ��
    :param name_postfix: 
    :return: ���
    """
    result_data = {}
    params = {}

    # �������ͣ�0��ʾ������1��ʾũ��
    params['data_type'] = "0"
    params['year'] = "%s" % str(user_config.setting["year"])
    params['month'] = "%s" % str(user_config.setting["month"])
    params['day'] = "%s" % str(user_config.setting["day"])
    params['hour'] = "%s" % str(user_config.setting["hour"])
    params['minute'] = "%s" % str(user_config.setting["minute"])
    params['pid'] = "%s" % str(user_config.setting["area_province"])
    params['cid'] = "%s" % str(user_config.setting["area_region"])
    # ϲ�����У�0��ʾ�Զ�������1��ʾ�Զ�ϲ����
    params['wxxy'] = "0"
    params['xing'] = "%s" % (user_config.setting["name_prefix"])
    params['ming'] = name_postfix
    # ��ʾŮ��1��ʾ��
    if user_config.setting["sex"] == "��":
        params['sex'] = "1"
    else:
        params['sex'] = "0"
    params['act'] = "submit"
    params['isbz'] = "1"

    post_data = urllib.urlencode(params)
    req = urllib2.urlopen(sys_config.REQUEST_URL, post_data)
    content = req.read()

    soup = BeautifulSoup(content, 'html.parser', from_encoding="GB18030")
    full_name = get_full_name(name_postfix)

    # print soup.find(string=re.compile(u"�����������"))
    for node in soup.find_all("div", class_="chaxun_b"):
        node_cont = node.get_text()
        if u'�����������' in node_cont:
            name_wuge = node.find(string=re.compile(u"�����������"))
            result_data['wuge_score'] = name_wuge.next_sibling.b.get_text()
        if u'������������' in node_cont:
            name_wuge = node.find(string=re.compile(u"������������"))
            result_data['bazi_score'] = name_wuge.next_sibling.b.get_text()

    result_data['total_score'] = float(result_data['wuge_score']) + float(result_data['bazi_score'])
    result_data['full_name'] = full_name
    return result_data


def get_full_name(name_postfix):
    """
        ��ȡ����������
    :param name_postfix: 
    :return: 
    """
    return "%s%s" % ((user_config.setting["name_prefix"]), name_postfix)


def sorted_list_by_dict_key(alist, key, reverse=False):
    """
        �Խ������
    :param alist: 
    :param key: 
    :param reverse: A boolean, reverse=True sort descending, default is false.
    :return: 
    """
    try:
        new_list = sorted(alist, key=lambda k: k['%s' % key], reverse=reverse)
        return new_list
    except Exception, e:
        return alist


def process(output_fpath):
    """
        ���㲢�ҽ����������ļ�
    :param output_fpath: ����ļ�·��
    :return: 
    """
    # ������п��õ������б�
    all_name_postfixs = get_name_postfixs()

    # ���������ļ�
    fout = open(output_fpath, "w")
    fout.write("����\t��������\t�������\t�ܷ�\n")

    cur_idx = 0
    all_count = all_name_postfixs.__len__()
    name_data_list = []
    for name_postfix in all_name_postfixs:
        cur_idx += 1
        try:
            # �����ֵĺ�׺��Ϊ�������м���
            name_data_dict = compute_name_score(name_postfix)
            name_data_list.append(name_data_dict)
        except Exception as e:
            print "error:", name_postfix, e
            continue

        print "%d/%d" % (cur_idx, all_count),
        print "\t".join((name_data_dict['full_name'],
                         u"��������=" + str(name_data_dict['bazi_score']),
                         u"�������=" + str(name_data_dict['wuge_score']),
                         u"�ܷ�=" + str(name_data_dict['total_score'])
                         ))

        fout.write(name_data_dict['full_name'] + "\t"
                   + str(name_data_dict['bazi_score']) + "\t"
                   + str(name_data_dict['wuge_score']) + "\t"
                   + str(name_data_dict['total_score']) + "\n")

    fout.flush()
    fout.close()

    # ����
    new_name_data_list = sorted_list_by_dict_key(name_data_list, "total_score", reverse=True)

    # ����ź���Ľ�����ļ�
    fout_sorted = open(output_fpath + ".sorted", "w")
    fout_sorted.write("����\t��������\t�������\t�ܷ�\n")
    for name_data_dict in new_name_data_list:
        fout_sorted.write(name_data_dict['full_name'] + "\t"
                          + str(name_data_dict['bazi_score']) + "\t"
                          + str(name_data_dict['wuge_score']) + "\t"
                          + str(name_data_dict['total_score']) + "\n")
    fout_sorted.flush()
    fout_sorted.close()


if __name__ == "__main__":
    print u"��ʼ����................................"
    process(user_config.setting['output_fpath'])
    print u"�������................................"
