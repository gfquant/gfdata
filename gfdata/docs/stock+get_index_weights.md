获取指数成份股给定日期的权重数据，每月的月底或者月初更新一次，请点击指数列表查看指数信息

params:index_id: 代表指数的标准形式代码， 形式：指数代码.交易所代码，例如"000001.XSHG"。

params:date: 查询权重信息的日期，形式："%Y-%m-%d"，例如"2018-05-03"；

# return:pandas.DataFrame

各 column 的含义如下:

* code:证券代码

* display_name:证券名称

* date:数据公布日期

* weight:所占权重

查询到对应日期，且有权重数据，返回 pandas.DataFrame， code(股票代码)，display_name(股票名称), date(日期), weight(权重)；

查询到对应日期，且无权重数据， 返回距离查询日期最近日期的权重信息；

找不到对应日期的权重信息， 返回距离查询日期最近日期的权重信息；