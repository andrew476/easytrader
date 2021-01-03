'''
https://blog.csdn.net/weixin_38391755/article/details/80380786/
Makefile是描述编译规则的文件
'''
test:
#一般用来测试makefile的流程。
	pytest -vx --cov=easytrader tests
