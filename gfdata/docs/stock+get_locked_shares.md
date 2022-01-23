获取指定日期区间内的限售解禁数据

:param stock_list:一个股票代码的 list

:param start_date:开始日期

:param end_date:结束日期

:param forward_count:交易日数量， 可以与 start_date 同时使用， 表示获取 start_date 到 forward_count 个交易日区间的数据

# :return: pandas.DataFrame

各 column 的含义如下:

day: 解禁日期

code: 股票代码

num: 解禁股数

rate1: 解禁股数/总股本

rate2: 解禁股数/总流通股本