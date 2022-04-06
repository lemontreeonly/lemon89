# @Project: Lemon85
# @Auth ： 柠檬班-土豆
# @Time ： 2021/10/28 21:35
# @E-mail ：121313927@qq.com
# @Company：湖南省零檬信息技术有限公司
# @Site: http://www.lemonban.com
# @Forum: http://testingpai.com


from selenium import webdriver
import time


# 打开网页
def open_url(url,driver):
    driver.get(url)
    driver.maximize_window()

# 登录
def login(username,password,driver):
    driver.find_element_by_id("username").send_keys(username)  # 输入用户名
    driver.find_element_by_id("password").send_keys(password)    # 输入密码
    driver.find_element_by_id("btnSubmit").click()   # 点击登录


# 查询零售出库，封装函数
def search_key(url,username,password,driver,s_key):
    open_url(url,driver)   # 打开网页
    login(username,password,driver)  # 登录

    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@src='/pages/materials/retail_out_list.html']"))

    # 输入查询内容，点击搜索按钮
    driver.find_element_by_id("searchNumber").send_keys(s_key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(3)

    # 设置搜索结果为返回值
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']/td[@field = 'number']/div").text
    return num






