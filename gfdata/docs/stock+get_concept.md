
获取股票所属概念板块。

:param security_or_securities 标的代码或标的列表

:param concept_source 目前只提供一种数据来源

:param date 要查询的提起, 日期字符串/date对象/datetime对象, 注意传入datetime对象时忽略日内时间

# :return: pandas.DataFrame

各 column 的含义如下:

code: 证券代码

number: 编号(和code一起确定唯一编号)

concept_code: 概念编码

concept_name: 概念名称


