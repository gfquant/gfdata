# -*- coding: utf-8 -*-
# @time: 2022/1/20 0:09
# @Author：lhf
# ----------------------
import os
import datetime
from importlib import import_module
from pathlib import Path

from pydantic import BaseModel

from gfdata import PACKAGE_DIR


def docs_by_url(url: str) -> str:
    """
    根据url获取接口文档；规则：docs目录下，路径'/'替换为'+'加上后缀'.md'形成文件名
    :param url:
    :return:
    """
    # 去掉后缀
    if not url.startswith('/'):
        url = '/' + url
    sep = Path(url).with_suffix('').parts
    rule = '+'.join(sep[1:]) + '.md'
    file = os.path.join(PACKAGE_DIR, 'docs', rule)
    try:
        with open(file, encoding='utf8') as f:
            des = f.read()
    except Exception as e:
        print(f'读取文件失败 {file}: {e}')
        des = sep[-1]
    else:
        if not des:
            des = sep[-1]
    return des


def args_by_url(url: str) -> BaseModel:
    """
    根据url获取接口参数模型；规则：args模块下，路径'/'替换为__作为model命名方式
    :param url:
    :return:
    """
    if not url.startswith('/'):
        url = '/' + url
    sep = Path(url).with_suffix('').parts  # 去掉后缀/或.xxx
    # 分割为model和obj
    model = ['gfdata', 'args']
    model.extend(sep[1:-1])  # 去掉首尾
    model = import_module('.'.join(model))
    obj = getattr(model, sep[-1])
    return obj


# 默认值设置-------------------------------------------------------------------
CODE_SEP = ","  # 多字段时的分隔符


def get_today() -> datetime.date:
    return datetime.date.today()


DIV_TIME = datetime.time(20)  # 交易日分割时间

TRADING_PRE = get_today() - datetime.timedelta(days=7)

TRADING_PRE_DT = datetime.datetime.strptime(
    TRADING_PRE.strftime('%Y-%m-%d') + ' ' + DIV_TIME.strftime('%H:%M:%S.%f'), '%Y-%m-%d %H:%M:%S.%f')

TRADING_TODAY: object = get_today()

TRADING_TODAY_DT = datetime.datetime.strptime(
    TRADING_TODAY.strftime('%Y-%m-%d') + ' ' + DIV_TIME.strftime('%H:%M:%S.%f'), '%Y-%m-%d %H:%M:%S.%f')
