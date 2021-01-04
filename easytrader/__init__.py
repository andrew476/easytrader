'''
https://www.zhihu.com/question/27011996/answer/1487708274
在使用python2的时候，我们被教导需要在作为python模块的目录中放置一个__init__.py文件，否则python解释器不会将该目录视为python模块，而对于这种目录的import操作都会报错。
因此__init__.py文件是python包的定义.
实际上，如果目录中包含了 __init__.py 时，当用 import 导入该目录时，会执行__init__.py 里面的代码。
'''
# -*- coding: utf-8 -*-
import urllib3
#导入urllib3网络请求库，实现get post headers功能
from easytrader import exceptions
#从易贸中导入exceptions例外
from easytrader.api import use, follower
#从易贸.api中导入use, follower这两个函数
from easytrader.log import logger
#从易贸.log中导入logger这个函数
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#disable_warnings 禁用urllib3的安全警告
__version__ = "0.22.0"
#版本
__author__ = "shidenggui"
#作者
