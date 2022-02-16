# -*- coding: utf-8 -*-
# @time: 2022/2/15 0:13
# @Author：lhf
# ----------------------
import datetime
from enum import Enum
from typing import Union, Optional
from pydantic import BaseModel

from gfdata.attach import get_today, TRADING_PRE_DT, TRADING_TODAY_DT, TRADING_TODAY, TRADING_PRE, CODE_SEP


class get_locked_shares(BaseModel):
    stock_list: str = CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    start_date: Optional[str] = None  # TRADING_PRE_DT
    end_date: Optional[str] = TRADING_TODAY
    count: int = None


class get_billboard_list(BaseModel):
    stock_list: str = CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    start_date: Optional[str] = None  # TRADING_PRE_DT
    end_date: Optional[str] = TRADING_TODAY
    count: int = None


class get_money_flow(BaseModel):
    security_list: str = CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    start_date: Optional[str] = None  # TRADING_PRE_DT
    end_date: Optional[str] = TRADING_TODAY
    fields: str = None
    count: int = None


class get_concept(BaseModel):
    security_or_securities: str = CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    concept_source: str = 'default'
    date: Optional[datetime.date] = TRADING_TODAY


class get_concept_stocks(BaseModel):
    concept_code: str = 'GN036'
    date: Optional[datetime.date] = TRADING_TODAY


class get_concepts(BaseModel):
    pass


class get_industry(BaseModel):
    security: str = CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    date: Optional[datetime.date] = TRADING_TODAY


class get_industry_stocks(BaseModel):
    industry_code: str = '801010'
    date: Optional[datetime.date] = TRADING_TODAY


class _get_industries__name(Enum):  # get_extras函数的info参数
    zjw = 'zjw'
    sw_l1 = 'sw_l1'
    sw_l2 = 'sw_l2'
    sw_l3 = 'sw_l3'
    jq_l1 = 'jq_l1'
    jq_l2 = 'jq_l2'


class get_industries(BaseModel):
    name: _get_industries__name = 'zjw'
    date: Optional[datetime.date] = TRADING_TODAY


class get_index_weights(BaseModel):
    index_id: str = '000001.XSHG'
    date: Optional[datetime.date] = TRADING_TODAY


class get_locked_shares(BaseModel):
    stock_list: str = CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    start_date: Optional[datetime.date] = TRADING_TODAY
    end_date: Optional[datetime.date] = None  # TRADING_TODAY
    forward_count: int = None


class get_marginsec_stocks(BaseModel):
    date: Optional[datetime.date] = TRADING_TODAY


class get_margincash_stocks(BaseModel):
    date: Optional[datetime.date] = TRADING_TODAY


class get_index_stocks(BaseModel):
    index_symbol: str = '000001.XSHG'
    date: Optional[datetime.date] = TRADING_TODAY
