#!/usr/bin/python
# #coding:utf-8

import gevent
from gevent import monkey

gevent.monkey.patch_all(thread=False, socket=False, select=False)

# 导入翻译模块
from TranslateFuncT import translate_func

IN_FILE_DICT = './IN_DICT/'
OUT_FILE_DICT = './OUT_DICT/'

BOOK = {}




def read(file_name):
    file_name = IN_FILE_DICT + file_name
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            BOOK.update({i: line})
            i += 1


def translate_ff(i, content):
    content = translate_func(content)
    BOOK[i] += content
    print('翻译完成:%d' % i)


def trans():
    g_list = []
    for i in BOOK.keys():
        content = BOOK[i]
        g = gevent.spawn(translate_ff, i, content)
        g_list.append(g)
        print('任务添加:%d' % i)
    gevent.joinall(g_list)


def write(file_name):
    file_name = OUT_FILE_DICT + file_name
    with open(file_name, 'wr+') as f:
        i = 0
        while i <= len(BOOK):
            if i :
                f.write(BOOK[i])
                print('写入成功%d' % i)


def run():
    # 读取文档内容, 分段保存在字典中, 并标号
    file_name = '1.txt'

    read(file_name)

    # 遍历字典, 使用协程调用翻译, 并添加到字典字符串中.
    trans()

    # 遍历字典, 写入内容
    write(file_name)


if __name__ == '__main__':
    run()
