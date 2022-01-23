获取股票/基金/指数的信息

:param code 证券代码

:param date 查询日期: 日期字符串/date对象/datetime对象, 注意传入datetime对象时忽略日内时间

# :return Dict

有如下属性:

* code: 证券编码
* display_name: 中文名称
* name: 缩写简称
* start_date: 上市日期, [datetime.date] 类型
* end_date: 退市日期， [datetime.date] 类型, 如果没有退市则为2200-01-01
* type: stock(股票)，index(指数)，futures(期货)、options(期权)；基金则返回次级分类：etf(ETF基金)，fja（分级A），fjb（分级B）
* parent: 分级基金的母基金代码