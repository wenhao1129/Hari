#coding=utf-8
import time
from selenium import webdriver
from logger.logger import Logger
import configparser
config = configparser.ConfigParser()
config.read("../config/config.ini", encoding="utf-8-sig")

class TestMyLog(object):
     def print_log(self,robot_sn, detail_SN, IMEI):
         boss_url = config.get("urlName", "url_BOSS")
         boss_138_url = config.get("urlName", "usr_BOSS_138")
         url_boss_login_user = config.get("url_login", "url_boss_user")
         url_boss_login_passwd = config.get("url_login", "url_boss_passwd")
         url_boss_pay_tenant = config.get("url_input_info", "boss_pay_tenant")
         url_boss_pay_contact = config.get("url_input_info", "boss_pay_contact")
         url_boss_pay_contact_pn = config.get("url_input_info", "boss_pay_contact_pn")
         url_boss_detail_address = config.get("url_input_info", "boss_pay_detail_address")
         mylogger = Logger(logger='TestMyLog').getlog()
         robot_sn_internet = robot_sn
         SN_internet = detail_SN
         IMEI_internet = IMEI
         mylogger.info("开始BOSS页面配置")
         mylogger.info("打开浏览器")
         chrome_browser = webdriver.Chrome()
         time.sleep(0.5)
         mylogger.info("最大化窗口")
         chrome_browser.maximize_window()
         time.sleep(1)
         ####登录页面
         mylogger.info("进入BOSS登录界面")
         chrome_browser.get("%s" % boss_url)
         chrome_browser.implicitly_wait(60)
         mylogger.info("BOSS登录界面输入账号")
         chrome_browser.find_element_by_css_selector("[placeholder='账号']").send_keys("%s" % url_boss_login_user)
         mylogger.info("BOSS登录界面输入密码")
         chrome_browser.find_element_by_css_selector("[placeholder='密码']").send_keys("%s" % url_boss_login_passwd)
         mylogger.info("勾选记住密码")
         chrome_browser.find_element_by_css_selector("[class='el-checkbox']").click()
         mylogger.info("确认登录")
         chrome_browser.find_element_by_css_selector("[type='submit']").click()
         mylogger.info("进入资产管理登录页面")
         #####资产管理
         chrome_browser.find_element_by_xpath("/html/body/div[1]/section/div/div/ul/li[4]").click()
         ####确认进入新增机器
         mylogger.info("确认进入新增机器页面")
         chrome_browser.find_element_by_xpath("/html/body/div/section/div/div/ul/li[4]/div[3]/a").click()
         #####新增机器
         mylogger.info("新增机器页面点击新增机器按钮")
         chrome_browser.find_element_by_class_name("fa-plus").click()
         #####资产编号
         mylogger.info("新增机器页面输入资产编号")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div/div[2]/div/input").send_keys(
             "%s" % robot_sn_internet)
         ####资产类型
         mylogger.info("新增机器页面选择资产类型输入回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div/div[2]/div/div[1]/input").click()
         time.sleep(0.5)
         mylogger.info("新增机器页面选择资产类型选择达闼固资")
         chrome_browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[1]/span").click()
         time.sleep(0.5)
         #####机器人名称
         mylogger.info("新增机器页面输入机器人名称")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[3]/div/div[2]/div[1]/input").send_keys(
             "%s" % robot_sn_internet)
         ####机器人唯一标识
         mylogger.info("新增机器页面输入机器人唯一标识")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[4]/div/div[2]/div[1]/input").send_keys(
             "%s" % SN_internet)
         time.sleep(0.5)
         #####产品系列
         mylogger.info("新增机器页面选择产品系列框按回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[5]/div/div[2]/div/div/input").click()
         time.sleep(0.5)
         mylogger.info("新增机器页面选择产品系列选择CloudGinger云端服务机器人")
         chrome_browser.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[4]/span").click()
         time.sleep(0.5)
         #####型号名称
         mylogger.info("新增机器页面选择型号名称框按回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[6]/div/div[2]/div/div[1]/input").click()
         time.sleep(0.5)
         mylogger.info("新增机器页面选择型号名称选择Ginger")
         chrome_browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[1]/span").click()
         time.sleep(0.5)
         ####产品型号
         mylogger.info("新增机器页面选择型号框按回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[7]/div/div[2]/div/div[1]/input").click()
         time.sleep(0.5)
         mylogger.info("新增机器页面选择型号框选择XR-1")
         chrome_browser.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li/span").click()
         time.sleep(0.5)
         ####PN或SKU
         mylogger.info("新增机器页面选择PN或SKU框按回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[8]/div/div[2]/div/div[1]/input").click()
         time.sleep(0.5)
         mylogger.info("新增机器页面选择PN或SKU框选择XR-1")
         chrome_browser.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[1]/span").click()
         time.sleep(0.5)
         ####供应商
         mylogger.info("新增机器页面选择供应商框按回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[9]/div/div[2]/div/div[1]/input").click()
         time.sleep(0.5)
         mylogger.info("新增机器页面选择供应商框选择达闼")
         chrome_browser.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[7]/span").click()
         time.sleep(0.5)
         ####生产日期
         mylogger.info("新增机器页面选择生产日期框按回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[13]/div/div[2]/div/input").click()
         # chrome_browser.implicitly_wait(2)
         time.sleep(0.5)
         mylogger.info("新增机器页面选择生产日期框选择当天")
         chrome_browser.find_element_by_css_selector("[class='available today']").click()
         # chrome_browser.implicitly_wait(3)
         time.sleep(0.5)
         #####取消
         mylogger.info("新增机器页面填写完成 按 取消 按钮")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[3]/button[1]/span").click()
         # time.sleep(0.5)
         #####确认提交
         #mylogger.info("新增机器页面填写完成 按 提交 按钮")
         # chrome_browser.find_element_by_xpath("/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[3]/button[2]/span").click()
         time.sleep(0.5)
         mylogger.info("退出浏览器")
         chrome_browser.quit()
         time.sleep(1)
         mylogger.info("重新打开浏览器")
         chrome_browser = webdriver.Chrome()
         mylogger.info("最大化窗口")
         chrome_browser.maximize_window()
         time.sleep(1)
         ####登录页面
         mylogger.info("进入BOSS登录界面")
         #chrome_browser.get("https://boss-sit138.harix.iamidata.com/asms/#/master/deviceList")
         chrome_browser.get("%s" % boss_138_url)
         time.sleep(0.5)
         mylogger.info("BOSS登录界面输入账号")
         #chrome_browser.find_element_by_css_selector("[placeholder='账号']").send_keys("admin")
         chrome_browser.find_element_by_css_selector("[placeholder='账号']").send_keys("%s" % url_boss_login_user)
         time.sleep(0.5)
         mylogger.info("BOSS登录界面输入密码")
         #chrome_browser.find_element_by_css_selector("[placeholder='密码']").send_keys("123456")
         chrome_browser.find_element_by_css_selector("[placeholder='密码']").send_keys("%s" % url_boss_login_passwd)
         time.sleep(0.5)
         mylogger.info("BOSS登录界面勾选记住密码")
         chrome_browser.find_element_by_css_selector("[class='el-checkbox']").click()
         time.sleep(0.5)
         mylogger.info("BOSS登录界面确认登录")
         chrome_browser.find_element_by_css_selector("[type='submit']").click()
         time.sleep(1)
         ####新增RCU管理
         #####运营
         mylogger.info("进入运行选择界面在界面选择 运营")
         chrome_browser.find_element_by_xpath("/html/body/div/section/div/div/ul/li[1]/div[1]").click()
         time.sleep(0.5)
         ####确认进入RCU管理页面
         mylogger.info("进入运行选择界面在界面点击 进入")
         chrome_browser.find_element_by_xpath("/html/body/div[1]/section/div/div/ul/li[1]/div[3]/a").click()
         time.sleep(0.5)
         ####RCU管理
         mylogger.info("进入新增RCU页面在左边栏点击 RCU管理")
         chrome_browser.find_element_by_xpath("/html/body/div[1]/section/section/div/ul/li[1]/ul/li[5]/span").click()
         ####新增RCU
         mylogger.info("进入新增RCU页面在中间点击 新增RCU")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/form/div[5]/div/button/span").click()
         ####RCU名称
         mylogger.info("进入新增RCU子页面在RCU名称框输入RCU名称")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div/div[2]/div[1]/input").send_keys(
             "%s" % robot_sn_internet)
         ####RCU唯一标识
         mylogger.info("进入新增RCU子页面在RCU唯一标识框输入RCU标识")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div/div[2]/div[1]/input").send_keys(
             "%s" % IMEI_internet)
         #####取消
         mylogger.info("进入新增RCU子页面信息填写完毕点击 取消")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[3]/button[1]/span").click()
         #####确认提交
         #mylogger.info("进入新增RCU子页面信息填写完毕点击 提交")
         # chrome_browser.find_element_by_xpath("/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[3]/button[2]/span").click()
         #####新增交付订单
         #####订单管理
         mylogger.info("进入新增RCU页面在左边栏点击 订单管理")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/div/ul/li[1]/ul/li[3]/span").click()
         time.sleep(0.5)
         #####新增交付订单
         mylogger.info("进入新增RCU页面在中间点击 新增交付订单")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/form/div[9]/div/button/span").click()
         time.sleep(1)
         #####订单名称
         mylogger.info("新增交付订单子页面在订单名称框中输入机器SN")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div/div[2]/div[1]/input").send_keys(
             "%s" % robot_sn_internet)
         time.sleep(0.5)
         ####销售日期
         mylogger.info("新增交付订单子页面在销售日期框按回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[3]/div/div[2]/div/input").click()
         time.sleep(0.5)
         mylogger.info("新增交付订单子页面在销售日期框选择当天")
         chrome_browser.find_element_by_css_selector("[class='available today']").click()
         time.sleep(0.5)
         ####租户名称
         mylogger.info("新增交付订单子页面在租户名称框输入NPI138")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[5]/div/div[2]/div/div/input").send_keys(
             "%s" % url_boss_pay_tenant)
         time.sleep(1)
         mylogger.info("新增交付订单子页面在租户名称框选择NPI138")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[4]/div[1]/div[1]/ul/li[3]/span").click()
         # chrome_browser.implicitly_wait(2)
         ####联系人
         mylogger.info("新增交付订单子页面在联系人框输入NPI138")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[6]/div/div[2]/div[1]/input").send_keys(
             "%s" % url_boss_pay_contact)
         ####联系电话
         mylogger.info("新增交付订单子页面在联系人电话框输入电话号码")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[7]/div/div[2]/div/input").send_keys(
             "%s" % url_boss_pay_contact_pn)
         time.sleep(0.5)
         ####服务地址
         mylogger.info("新增交付订单子页面在服务地址框输入闵行")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[8]/div/div[2]/div/div/input").send_keys(
             "闵行")
         time.sleep(0.5)
         mylogger.info("新增交付订单子页面在服务地址框点击回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[5]/div[2]/div[1]/ul/li/span").click()
         mylogger.info("新增交付订单子页面在具体地址框输入地址")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[2]/form/div/div[9]/div/div[2]/div/input").send_keys(
             "%s" % url_boss_detail_address)
         time.sleep(0.5)
         ###取消按钮
         mylogger.info("新增交付订单子页面填写完毕 取消")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[3]/button[1]/span").click()
         # time.sleep(0.5)
         ###提交按钮
         #mylogger.info("新增交付订单子页面填写完毕 提交")
         # chrome_browser.find_element_by_xpath(
         #    "/html/body/div[1]/section/section/main/div[2]/div/div[2]/div/div[3]/button[2]/span").click()
         time.sleep(0.5)
         mylogger.info("关闭并退出浏览器")
         chrome_browser.quit()
         mylogger.info("结束BOSS页面配置")

