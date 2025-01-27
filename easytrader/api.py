# -*- coding: utf-8 -*-
import logging
#导入日志库，抛弃print
import sys
#sys是针对与Python解释器相关的变量和方法

import six
#six库是对于python2和python3的兼容库，使用six库可以使写的代码不用进行修改就能在python2或者python3的环境下进行运行
from easytrader.joinquant_follower import JoinQuantFollower
#从易贸.joinquant_follower 中导入JoinQuantFollower类
from easytrader.log import logger
#从易贸.log中导入logger变量
from easytrader.ricequant_follower import RiceQuantFollower

from easytrader.xq_follower import XueQiuFollower
from easytrader.xqtrader import XueQiuTrader
#同上，导入功能函数
if sys.version_info <= (3, 5):
    raise TypeError("不支持 Python3.5 及以下版本，请升级")
#获取元组类型的版本信息
#下面定义了一些功能函数
def use(broker, debug=False, **kwargs):
    """用于生成特定的券商对象
    :param broker:券商名支持 ['yh_client', '银河客户端'] ['ht_client', '华泰客户端']
    :param debug: 控制 debug 日志的显示, 默认为 True
    :param initial_assets: [雪球参数] 控制雪球初始资金，默认为一百万
    :return the class of trader

    Usage::

        >>> import easytrader
        >>> user = easytrader.use('xq')
        >>> user.prepare('xq.json')
    """
    if debug:
        logger.setLevel(logging.DEBUG)
#如果debug为真，则logger = logging.getLogger("easytrader")=返回指定名称的记录器。设置此记录器的日志记录级别。级别必须是int或str。
    if broker.lower() in ["xq", "雪球"]:
        return XueQiuTrader(**kwargs)
#broker中介。这段代码看不懂
    if broker.lower() in ["yh_client", "银河客户端"]:
        from .yh_clienttrader import YHClientTrader

        return YHClientTrader()

    if broker.lower() in ["ht_client", "华泰客户端"]:
        from .ht_clienttrader import HTClientTrader

        return HTClientTrader()

    if broker.lower() in ["wk_client", "五矿客户端"]:
        from easytrader.wk_clienttrader import WKClientTrader

        return WKClientTrader()

    if broker.lower() in ["htzq_client", "海通证券客户端"]:
        from easytrader.htzq_clienttrader import HTZQClientTrader

        return HTZQClientTrader()

    if broker.lower() in ["gj_client", "国金客户端"]:
        from .gj_clienttrader import GJClientTrader

        return GJClientTrader()

    if broker.lower() in ["gf_client", "广发客户端"]:
        from .gf_clienttrader import GFClientTrader

        return GFClientTrader()

    if broker.lower() in ["ths", "同花顺客户端"]:
        from .clienttrader import ClientTrader

        return ClientTrader()

    raise NotImplementedError


def follower(platform, **kwargs):
    """用于生成特定的券商对象
    :param platform:平台支持 ['jq', 'joinquant', '聚宽’]
    :param initial_assets: [雪球参数] 控制雪球初始资金，默认为一万,
        总资金由 initial_assets * 组合当前净值 得出
    :param total_assets: [雪球参数] 控制雪球总资金，无默认值,
        若设置则覆盖 initial_assets
    :return the class of follower

    Usage::

        >>> import easytrader
        >>> user = easytrader.use('xq')
        >>> user.prepare('xq.json')
        >>> jq = easytrader.follower('jq')
        >>> jq.login(user='username', password='password')
        >>> jq.follow(users=user, strategies=['strategies_link'])
    """
    if platform.lower() in ["rq", "ricequant", "米筐"]:
        return RiceQuantFollower()
    if platform.lower() in ["jq", "joinquant", "聚宽"]:
        return JoinQuantFollower()
    if platform.lower() in ["xq", "xueqiu", "雪球"]:
        return XueQiuFollower(**kwargs)
    raise NotImplementedError
#上面两个函数真没看明白。跳过以后看
