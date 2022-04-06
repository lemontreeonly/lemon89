# @Project: Lemon85
# @Auth ： 柠檬班-土豆
# @Time ： 2021/10/28 21:53
# @E-mail ：121313927@qq.com
# @Company：湖南省零檬信息技术有限公司
# @Site: http://www.lemonban.com
# @Forum: http://testingpai.com


from web.common import web1
from web.test_data import test_data
from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()
driver.implicitly_wait(10)


# 读取测试数据
url = test_data.url
username = test_data.login_user["username"]
pwd = test_data.login_user["password"]
s_key = test_data.s_key

# 调用库存查询函数
result = web1.search_key(url= url,username=username,password=pwd,driver=driver,s_key=s_key)
if s_key in result:
    print("搜索结果正确！用例执行通过！")
else:
    print("查询结果错误，用例不通过！")

# 关闭浏览器：
driver.close()


