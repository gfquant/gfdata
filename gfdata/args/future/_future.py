# -*- coding: utf-8 -*-
# @time: 2022/2/15 0:12
# @Author：lhf
# ----------------------
import datetime
from enum import Enum
from typing import Union, Optional
from pydantic import BaseModel

from gfdata.attach import get_today, TRADING_PRE_DT, TRADING_TODAY_DT, TRADING_TODAY, TRADING_PRE, CODE_SEP


class get_future_contracts(BaseModel):
    underlying_symbol: str = 'AU'
    date: datetime.date = TRADING_TODAY


class get_dominant_future(BaseModel):
    underlying_symbol: str = CODE_SEP.join(['AU', 'IF'])
    start_date: Optional[datetime.date] = None
    end_date: datetime.date = TRADING_TODAY


# ------------------------------------------------------------------------
class _factor_carry_method(Enum):
    value = 'value'
    mean = 'mean'
    diff = 'diff'


class factor_carry(BaseModel):
    method: _factor_carry_method  # 支持的统计方法
    start: Optional[datetime.date] = None
    end: Optional[datetime.date] = TRADING_TODAY
    underlying_list: str = None
    rule: str = 'log_yoy'
    R: Optional[int] = None  # 设为可选参数；有些method需要，有些不需要


class _factor_returns_method(Enum):
    value = 'value'
    rise_pct = 'rise_pct'
    cv = 'cv'
    cv_price_rate = 'cv_price_rate'


class factor_returns(BaseModel):
    method: _factor_returns_method  # 支持的统计方法
    start: Optional[datetime.date] = None
    end: Optional[datetime.date] = TRADING_TODAY
    underlying_list: str = None
    R: int  # 必须要有


class _factor_warehouse_method(Enum):
    value = 'value'
    diff = 'diff'
    quantile = 'quantile'


class factor_warehouse(BaseModel):
    method: _factor_warehouse_method  # 支持的统计方法
    start: Optional[datetime.date] = None
    end: Optional[datetime.date] = TRADING_TODAY
    underlying_list: str = None
    R: Optional[int] = None  # 设为可选参数；有些method需要，有些不需要
