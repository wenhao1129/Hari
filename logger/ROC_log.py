#coding=utf-8
import time
from selenium import webdriver
from logger.logger import Logger
import configparser
config = configparser.ConfigParser()
config.read("../config/config.ini", encoding="utf-8-sig")


class TestMyLog(object):
     def print_log(self,robot_sn, detail_SN, IMEI):
         roc_url = config.get("urlName", "url_ROC")
         url_roc_login_user = config.get("url_login", "url_roc_user")
         url_roc_login_passwd = config.get("url_login", "url_roc_passwd")
         url_roc_customer_code = config.get("url_input_info", "roc_customer_code")
         url_roc_add_ID_passwd = config.get("url_input_info", "roc_add_ID_passwd")
         url_roc_add_ID_service_code = config.get("url_input_info", "roc_add_ID_service_code")
         mylogger = Logger(logger='TestMyLog').getlog()
         robot_sn_internet = robot_sn
         SN_internet = detail_SN
         IMEI_internet = IMEI
         mylogger.info("开始ROC页面配置")
         mylogger.info("打开浏览器")
         chrome_browser = webdriver.Chrome()
         time.sleep(0.5)
         mylogger.info("最大化窗口")
         chrome_browser.maximize_window()
         time.sleep(0.5)
         ####登录页面
         mylogger.info("进入ROC登录界面")
         chrome_browser.get("%s" % roc_url)
         chrome_browser.implicitly_wait(60)
         mylogger.info("ROC登录界面输入账号")
         #chrome_browser.find_element_by_css_selector("[placeholder='请输入管理员编码']").send_keys("liyang")
         chrome_browser.find_element_by_css_selector("[placeholder='请输入管理员编码']").send_keys("%s" % url_roc_login_user)
         mylogger.info("ROC登录界面输入密码")
         chrome_browser.find_element_by_css_selector("[placeholder='请输入登录密码']").send_keys("%s" % url_roc_login_passwd)
         mylogger.info("ROC登录界面点击登录确认登录")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/passport-login/div/div/div[2]/div/form/nz-form-item[3]/nz-form-control/div/span/button").click()
         #####机器人账号管理
         mylogger.info("ROC界面左边栏点击机器人账号管理下拉菜单")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/layout-sidebar/div/app-sidebar-menu/ul/li[9]/div/span[2]/span").click()
         #####账号管理
         mylogger.info("ROC界面左边栏点击账号管理")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/layout-sidebar/div/app-sidebar-menu/ul/li[9]/ul/ul/li[1]").click()
         #####添加账号
         mylogger.info("ROC界面点击添加账号")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/div[2]/app-list/nz-card/div/div[1]/div/button[1]").click()
         #####客户编码
         time.sleep(1)
         mylogger.info("添加账号子页面单机客户编码框")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-account/form/div[1]/nz-form-item[1]/nz-form-control/div/span/app-select-customer/nz-select/div/div/div[1]").click()
         mylogger.info("添加账号子页面客户编码框中输入NPItest")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-account/form/div[1]/nz-form-item[1]/nz-form-control/div/span/app-select-customer/nz-select/div/div/div[2]/div/input").send_keys(
             "%s" % url_roc_customer_code)
         mylogger.info("添加账号子页面客户编码框中选择NPItest")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/ul/li").click()
         #####账号
         mylogger.info("添加账号子页面账号框中输入账号")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-account/form/div[1]/nz-form-item[2]/nz-form-control/div/span/input").send_keys(
             "%s" % robot_sn)
         #####密码
         mylogger.info("添加账号子页面密码框中输入密码")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-account/form/div[1]/nz-form-item[3]/nz-form-control/div/span/input").send_keys(
             "%s" % url_roc_add_ID_passwd)
         #####密码确认
         mylogger.info("添加账号子页面确认密码框中再次输入密码")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-account/form/div[1]/nz-form-item[4]/nz-form-control/div/span/input").send_keys(
             "%s" % url_roc_login_passwd)
         #####姓名
         mylogger.info("添加账号子页面姓名框中输入姓名")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-account/form/div[1]/nz-form-item[5]/nz-form-control/div/span/input").send_keys(
             "%s" % robot_sn)
         #####服务编码
         mylogger.info("添加账号子页面服务编码框中点击回车")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-account/form/div[1]/nz-form-item[6]/nz-form-control/div/span/nz-select/div/div/div[1]").click()
         mylogger.info("添加账号子页面服务编码框中输入CloudGinger")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-account/form/div[1]/nz-form-item[6]/nz-form-control/div/span/nz-select/div/div/div[2]/div/input").send_keys(
             "%s" % url_roc_add_ID_service_code)
         mylogger.info("添加账号子页面服务编码框中选择CloudGinger")
         time.sleep(1)
         chrome_browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/ul/li[1]").click()
         #####环境
         mylogger.info("添加账号子页面环境框中点击回车")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-account/form/div[1]/nz-form-item[7]/nz-form-control/div/span/app-select-resource/nz-select/div/div/div[1]").click()
         mylogger.info("添加账号子页面环境框中选择134环境")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[4]/div/div/div/ul/li[2]").click()
         #####Robot类型
         mylogger.info("添加账号子页面Robot类型框中点击回车")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-account/form/div[1]/nz-form-item[19]/nz-form-control/div/span/app-select-robot-type/nz-select/div/div/div").click()
         mylogger.info("添加账号子页面Robot类型框选择cloudGinger")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[4]/div/div/div/ul/li[2]").click()
         #####取消
         mylogger.info("添加账号子页面填写完毕 取消")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-account/form/div[2]/button[1]").click()
         # time.sleep(0.5)
         #####确认保存
         #mylogger.info("添加账号子页面填写完毕 保存")
         # chrome_browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-account/form/div[2]/button[2]").click()
         #####正式运行的时候需要用参数
         mylogger.info("机器人账号管理主页面搜索栏输入机器人账号")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/div[2]/app-list/nz-card/div/div[1]/form/nz-row/nz-col[1]/nz-form-item/nz-form-control/div/span/input").send_keys(
             "EVT1-03")
         #chrome_browser.find_element_by_xpath(
         #    "/html/body/app-root/layout-default/section/div[2]/app-list/nz-card/div/div[1]/form/nz-row/nz-col[1]/nz-form-item/nz-form-control/div/span/input").send_keys(
         #    "%s" % robot_sn)
         mylogger.info("机器人账号管理主页面搜索栏输入机器人账号后点击搜索")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/div[2]/app-list/nz-card/div/div[1]/form/nz-row/nz-col[2]/button[1]").click()
         mylogger.info("机器人账号管理主页面点击搜到到的机器人账号")
         time.sleep(1)
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/div[2]/app-list/nz-card/div/nz-table/nz-spin/div/div/div/div/table/tbody/tr[1]/td[1]/label/span[1]/input").click()
         mylogger.info("机器人账号管理主页面点击绑定机器人")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/div[2]/app-list/nz-card/div/div[2]/button[1]").click()
         ####RCU唯一标识
         mylogger.info("绑定机器人子页面点击RCU唯一标识")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-bind-robot/div[2]/form/nz-form-item[3]/nz-form-control/div/span/nz-select/div/div/div[1]").click()
         mylogger.info("绑定机器人子页面点击RCU唯一标识框输入RCU的IMEI")
         time.sleep(1)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-bind-robot/div[2]/form/nz-form-item[3]/nz-form-control/div/span/nz-select/div/div/div[2]/div/input").send_keys(
             "%s" % IMEI_internet)
         mylogger.info("绑定机器人子页面点击RCU唯一标识框选择RCU的IMEI")
         time.sleep(1)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[4]/div/div/div/ul/li").click()
         ####Robot唯一标识
         mylogger.info("绑定机器人子页面点击Robot唯一标识")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-bind-robot/div[2]/form/nz-form-item[4]/nz-form-control/div/span/nz-select/div/div").click()
         mylogger.info("绑定机器人子页面点击Robot唯一标识框输入robot SN")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-bind-robot/div[2]/form/nz-form-item[4]/nz-form-control/div/span/nz-select/div/div/div[2]/div/input").send_keys(
             "%s" % SN_internet)
         mylogger.info("绑定机器人子页面选择Robot唯一标识")
         time.sleep(1)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[4]/div/div/div/ul/li[1]").click()
         #####取消
         mylogger.info("绑定机器人子页面填写完毕 取消")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-bind-robot/div[3]/button[1]").click()
         # time.sleep(0.5)
         #####确认保存
         #mylogger.info("绑定机器人子页面填写完毕 保存")
         # chrome_browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-bind-robot/div[3]/button[2]").click()
         ####展开安全管控
         mylogger.info("机器人账号管理页面左边栏展开安全管控")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/layout-sidebar/div/app-sidebar-menu/ul/li[12]").click()
         ####策略管理
         mylogger.info("机器人账号管理页面左边栏展开安全管控后点击策略管理")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/layout-sidebar/div/app-sidebar-menu/ul/li[12]/ul/ul/li[2]").click()
         ####添加策略
         mylogger.info("机器人账号管理页面点击添加策略按钮")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/div[2]/app-policy-list/nz-card/div/div[1]/div/button").click()
         ####客户编码
         mylogger.info("添加策略子页面在客户编码框按回车")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-policy-add/div[2]/form/nz-tabset/div[2]/div[1]/div/nz-form-item[1]/nz-form-control/div/span/app-select-customer/nz-select/div/div").click()
         mylogger.info("添加策略子页面在客户编码框输入NPItest")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-policy-add/div[2]/form/nz-tabset/div[2]/div[1]/div/nz-form-item[1]/nz-form-control/div/span/app-select-customer/nz-select/div/div/div[2]/div/input").send_keys(
             "%s" % url_roc_customer_code)
         mylogger.info("添加策略子页面在客户编码框选择NPItest")
         time.sleep(1)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[4]/div/div/div/ul/li").click()
         ####策略名称
         mylogger.info("添加策略子页面在策略名称框输入策略名称")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-policy-add/div[2]/form/nz-tabset/div[2]/div[1]/div/nz-form-item[2]/nz-form-control/div/span/input").send_keys(
             "%s" % robot_sn)
         ####机器人类型
         mylogger.info("添加策略子页面在机器人类型框按回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-policy-add/div[2]/form/nz-tabset/div[2]/div[1]/div/nz-form-item[3]/nz-form-control/div/span/nz-select/div/div").click()
         mylogger.info("添加策略子页面在机器人类型框选择机器人类型")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[4]/div/div/div/ul/li[2]").click()
         #####关闭
         mylogger.info("添加策略子页面填写完毕 取消")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-policy-add/div[2]/form/div/button[1]").click()
         # time.sleep(0.5)
         #####确认保存
         #mylogger.info("添加策略子页面填写完毕 保存")
         # chrome_browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-policy-add/div[2]/form/div/button[2]").click()
         ####推送策略 正式运行的时候需要用参数
         mylogger.info("在策略管理搜索栏输入机器人SN")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/div[2]/app-policy-list/nz-card/div/div[1]/form/nz-row/nz-col[1]/nz-form-item/nz-form-control/div/span/input").send_keys(
             "%s" % robot_sn)
         ####点击搜索
         mylogger.info("在策略管理搜索栏输入机器人SN后点击搜索")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/div[2]/app-policy-list/nz-card/div/div[1]/form/nz-row/nz-col[4]/button[1]").click()
         ####选择机器
         mylogger.info("在策略管理搜索栏搜索到的机器前面勾选机器")
         time.sleep(1)
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/div[2]/app-policy-list/nz-card/div/nz-table/nz-spin/div/div/div/div/table/tbody/tr/td[1]/label/span[1]/input").click()
         ####点击推送
         mylogger.info("在策略管理搜索栏搜索到的机器前面勾选机器后点击推送")
         time.sleep(1)
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/div[2]/app-policy-list/nz-card/div/div[2]/button[1]").click()
         ####推送名称
         mylogger.info("在推送策略子页面推送名称框里面输入机器人SN")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-push/form/nz-form-item[1]/nz-form-control/div/span/input").send_keys(
             "%s" % robot_sn_internet)
         #####关闭
         mylogger.info("推送策略子页面填写完毕后 关闭")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-push/form/div/button[1]").click()
         # time.sleep(0.5)
         #####确认保存
         #mylogger.info("推送策略子页面填写完毕后 关闭")
         # chrome_browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-add-push/form/div/button[1]").click()
         chrome_browser.quit()
         mylogger.info("关闭并退出浏览器。")
         mylogger.info("结束ROC页面配置")


#testlog = TestMyLog()
#testlog.print_log(self,)