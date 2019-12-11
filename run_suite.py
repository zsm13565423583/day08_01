#导包
import unittest
#定义测试套件
from tools.HTMLTestReportCN import HTMLTestRunner

suite =unittest.defaultTestLoader.discover("./scripts")
#获取报告文件流---实例化THMLTestRunner======调用run方法
with open("./report/report.html","wb") as f:
    HTMLTestRunner(stream=f).run(suite)