# -*- coding: utf-8 -*-
# @time: 2022/1/21 16:56
# @Author：lhf
# ----------------------
import datetime
from enum import Enum
from typing import Union, Optional
from pydantic import BaseModel

from gfdata.attach import get_today, TRADING_PRE_DT, TRADING_TODAY_DT, TRADING_TODAY, TRADING_PRE, CODE_SEP


class help_fields__name(Enum):
    balance = 'balance'
    income = 'income'
    cash_flow = 'cash_flow'
    indicator = 'indicator'

    valuation = 'valuation'

    bank_indicator = 'bank_indicator'
    security_indicator = 'security_indicator'
    insurance_indicator = 'insurance_indicator'


class finance__help_fields(BaseModel):
    name: help_fields__name


class finance__get_valuation(BaseModel):
    security: str = CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    start_date: Optional[str] = None  # TRADING_PRE_DT
    end_date: Optional[str] = TRADING_TODAY_DT
    fields: Optional[str] = CODE_SEP.join([
        # "id",
        "code",
        "pubDate",
        "pe_ratio",
        "turnover_ratio",
        "pb_ratio",
        "ps_ratio",
        "pcf_ratio",
        "capitalization",
        "market_cap",
        "circulating_cap",
        "circulating_market_cap",
        "day",
        "pe_ratio_lyr"
    ])
    count: Optional[int] = None


class finance__get_stat(BaseModel):
    name: help_fields__name
    fields: str = None  # 可以不传
    security: str = None  # 可以不传# CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    stat: str = ''  # 季度: 格式是: 年 + 'q' + 季度序号, 例如: '2015q1', '2013q4'；年份: 格式就是年份的数字, 例如: '2015', '2016'


class finance__get_date(BaseModel):
    name: help_fields__name
    fields: str = None  # 可以不传
    security: str = None  # 可以不传# CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    date: str = ''


class finance__get_count(BaseModel):
    name: help_fields__name
    fields: str = None  # 可以不传
    security: str = None  # 可以不传# CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    end_date: str = ''
    count: int = 1
