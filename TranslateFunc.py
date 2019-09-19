#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Author  :   Allen
 
@License :   (C) Copyright 2018, Allen's Studio
 
@Contact :   188512936@qq.com
 
@Software:   VS2017
 
@File    :   Translate_Func.py
 
@Time    :   June 21,2018
 
@Desc    :   实现翻译的爬虫功能.
 
'''


import json
import requests  # pip intasll requests
from Py4Js import *


# 谷歌翻译方法
def google_translate(content):
    js = Py4Js()
    tk = js.getTk(content)

    if len(content) > 4891:
        print("翻译的长度超过限制！！！")
        return ''

    param = {'tk': tk, 'q': content}

    print('1')
    # result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
    #     &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param)
    result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en 
        &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss 
        &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param)

    print('2')
    # 返回的结果为Json，解析为一个嵌套列表
    trans = result.json()[0]
    ret = ''
    for i in range(len(trans)):
        line = trans[i][0]
        if line != None:
            ret += trans[i][0]

    if ret:
        return (True, ret)
    else:
        return (False, ret)


def translate_func(content):
    '''集成百度、谷歌、有道多合一的翻译'''

    print('0')
    trans = google_translate(content)

    return trans

