获取一支或者多只证券的行情数据

:param security 一支证券代码或者一个证券代码的list

:param count 与 start_date 二选一，不可同时使用.数量, 返回的结果集的行数, 即表示获取 end_date 之前几个 frequency 的数据

:param start_date 与 count 二选一，不可同时使用. 字符串或者 datetime.datetime/datetime.date 对象, 开始时间

:param end_date 格式同上, 结束时间, 默认是 **当前交易日20点**

:param frequency 单位时间长度, 几天或者几分钟, 现在支持'Xd','Xm', 'daily'(等同于'1d'), 'minute'(等同于'1m'), X是一个正整数, 分别表示X天和X分钟

:param fields 字符串list, 默认是None(表示['open', 'close', 'high', 'low', 'volume', 'money']这几个标准字段), 支持以下属性 ['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit', 'low_limit', 'avg', 'pre_close', 'paused']

:param skip_paused 是否跳过不交易日期(包括停牌, 未上市或者退市后的日期). 如果不跳过, 停牌时会使用停牌前的数据填充, 上市前或者退市后数据都为 nan

~~:param panel: 当传入一个标的列表的时候，是否返回一个panel对象，默认为True，表示返回一个panel对象~~

:param fill_paused : False 表示使用NAN填充停牌的数据，True表示用close价格填充，默认True


# :return pandas.DataFrame

如果是一支证券, 则返回pandas.DataFrame对象, 行索引是datetime.datetime对象, 列索引是行情字段名字;

如果是多支证券, 返回一个dataframe对象，在这个对象中额外多出code、time两个字段，分别表示该条数据对应的标的、时间