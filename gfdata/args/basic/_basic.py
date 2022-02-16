# -*- coding: utf-8 -*-
# @time: 2022/2/15 0:12
# @Author：lhf
# ----------------------
import datetime
from enum import Enum
from typing import Union, Optional
from pydantic import BaseModel

from gfdata.attach import get_today, TRADING_PRE_DT, TRADING_TODAY_DT, TRADING_TODAY, TRADING_PRE, CODE_SEP


class convert_code(BaseModel):
    code: str = CODE_SEP.join(['000001.SZ', 'FU2103', 'I2109-C-810'])


class get_all_securities(BaseModel):
    types: str = CODE_SEP.join(['etf', 'lof'])
    date: Optional[datetime.date] = TRADING_TODAY


class get_security_info(BaseModel):
    code: str = '512880.XSHG'
    date: Optional[datetime.date] = None  # TRADING_TODAY


class _get_extras__info(Enum):  # get_extras函数的info参数
    is_st = 'is_st'
    acc_net_value = 'acc_net_value'
    unit_net_value = 'unit_net_value'
    futures_sett_price = 'futures_sett_price'
    futures_positions = 'futures_positions'
    adj_net_value = 'adj_net_value'


class get_extras(BaseModel):
    info: _get_extras__info = 'is_st'
    security_list: str = CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    start_date: Optional[datetime.date] = None  # TRADING_PRE
    end_date: datetime.date = TRADING_TODAY
    count: Optional[int] = None


class get_trade_days(BaseModel):
    start_date: str = '2005-01-01'
    end_date: str = TRADING_TODAY
    count: int = None


class get_bars(BaseModel):
    security: str = CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    count: Optional[int] = None
    unit: str = '1d'
    fields: Optional[str] = CODE_SEP.join(['date', 'open', 'close', 'high', 'low', 'volume', 'money'])
    include_now: bool = False
    end_dt: str
    fq_ref_date: str = None
    df: bool = True


class get_price(BaseModel):
    security: str = CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    start_date: Optional[str] = None  # TRADING_PRE_DT
    end_date: Optional[str] = TRADING_TODAY_DT
    frequency: str = '1d'
    fields: Optional[str] = CODE_SEP.join(['date', 'open', 'close', 'high', 'low', 'volume', 'money'])
    skip_paused: Optional[bool] = True
    fq: Optional[str] = 'pre'
    count: Optional[int] = None
    pre_factor_ref_date: Optional[datetime.date] = get_today()
    fill_paused: Optional[bool] = True


class get_call_auction(BaseModel):
    security: str = CODE_SEP.join(['000001.XSHE', '600000.XSHG'])
    start_date: Optional[str] = None  # TRADING_PRE_DT
    end_date: Optional[str] = TRADING_TODAY
    fields: Optional[str] = CODE_SEP.join(['time', 'current', 'volume', 'money', 'a1_p', 'a1_v', 'b1_p', 'b1_v'])
