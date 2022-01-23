得到多只标的在一段时间的如下额外的数据

:param info ['is_st', 'acc_net_value', 'unit_net_value', 'futures_sett_price', 'futures_positions'] 中的一个

:param security_list 证券列表

:param start_date 开始日期

:param end_date 结束日期

:param count 数量, 与 start_date 二选一, 不可同时使用, 必须大于 0

# :return <df=True>:pandas.DataFrame

列索引是股票代码, 行索引是datetime.datetime