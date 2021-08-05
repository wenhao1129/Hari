#coding=utf-8
import time
from selenium import webdriver
from logger.logger import Logger
import win32gui
import win32con
from selenium.webdriver.common.keys import Keys
import configparser
config = configparser.ConfigParser()
config.read("../config/config.ini", encoding="utf-8-sig")


class TestMyLog(object):
     def print_log(self,robot_sn, detail_SN, IMEI):
         rdp_url = config.get("urlName", "url_RDP")
         url_rdp_login_user = config.get("url_login", "url_rdp_user")
         url_rdp_login_passwd = config.get("url_login", "url_rdp_passwd")
         url_hari_customer_code = config.get("url_input_info", "hari_customer_code")
         mylogger = Logger(logger='TestMyLog').getlog()
         robot_sn_internet = robot_sn
         SN_internet = detail_SN
         IMEI_internet = IMEI
         mylogger.info("开始RDP页面配置")
         mylogger.info("打开浏览器")
         chrome_browser = webdriver.Chrome()
         time.sleep(0.5)
         mylogger.info("最大化窗口")
         chrome_browser.maximize_window()
         ####登录页面
         chrome_browser.implicitly_wait(90)
         mylogger.info("进入harix os界面")
         chrome_browser.get("%s" % rdp_url)
         time.sleep(30)
         mylogger.info("在Hari os界面点击登录")
         chrome_browser.find_element_by_xpath("/html/body/app-root/app-index/div/header/div/div[2]/a[1]").click()
         time.sleep(3)
         mylogger.info("Harix os登录界面输入账号")
         chrome_browser.find_element_by_css_selector("[placeholder='请输入登录账号']").send_keys(
             "%s" % url_rdp_login_user)
         mylogger.info("Harix os登录界面输入密码")
         chrome_browser.find_element_by_css_selector("[placeholder='请输入登录密码']").send_keys(
             "%s" % url_rdp_login_passwd)
         mylogger.info("Harix os登录界面输入企业编码")
         chrome_browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-login-model/div/div/div/form/nz-form-item[3]/nz-form-control/div/span/input").send_keys(
             "%s" % url_hari_customer_code)
         mylogger.info("Harix os登录界面确认登录")
         chrome_browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-login-model/div/div/div/form/button").click()
         mylogger.info("进行资源管理配置")
         #####资源管理
         mylogger.info("点击资源管理")
         chrome_browser.find_element_by_xpath("/html/body/app-root/layout-default/layout-header/div/app-nav/ul[1]/div[3]").click()
         time.sleep(1)
         mylogger.info("点击技能管理")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/layout-header/div/app-nav/ul[2]/li[2]").click()
         time.sleep(1)
         mylogger.info("点击新增技能")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/app-blueprint-list/nz-card/div/div[1]/button").click()
         time.sleep(1)
         mylogger.info("进入新增技能子页面")
         mylogger.info("新增技能子页面输入技能名称")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-blueprint-add/form/nz-form-item[1]/nz-form-control/div/span/input").send_keys("蓝图")
         time.sleep(0.5)
         mylogger.info("新增技能子页面在技能类型选择框点击回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-blueprint-add/form/nz-form-item[2]/nz-form-control/div/span/nz-select/div/div/div").click()
         time.sleep(0.5)
         mylogger.info("新增技能子页面在技能类型选择框选择技能蓝图")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[5]/div/div/div/ul/li[1]").click()
         time.sleep(0.5)
         mylogger.info("新增技能子页面在分类标识选择框点击回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-blueprint-add/form/nz-form-item[3]/nz-form-control/div/span/nz-select/div/div/div").click()
         time.sleep(0.5)
         mylogger.info("新增技能子页面在分类标识选择框选择客户端")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[5]/div/div/div/ul/li[1]").click()
         time.sleep(0.5)
         mylogger.info("新增技能子页面在平台选择框点击回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-blueprint-add/form/nz-form-item[5]/nz-form-control/div/span/nz-select/div/div/div").click()
         mylogger.info("新增技能子页面在平台选择框选择linux")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[5]/div/div/div/ul/li[2]").click()
         mylogger.info("新增技能子页面在技能标识框输入蓝图")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-blueprint-add/form/nz-form-item[7]/nz-form-control/div/span/input").send_keys("蓝图")
         time.sleep(0.5)
         mylogger.info("新增技能子页面在标签选择框点击回车")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-blueprint-add/form/nz-form-item[8]/nz-form-control/div/span/nz-select/div/div/div").click()
         time.sleep(0.5)
         mylogger.info("新增技能子页面在标签选择框输入动作")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-blueprint-add/form/nz-form-item[8]/nz-form-control/div/span/nz-select/div/div/ul/li/input").send_keys("动作")
         time.sleep(0.5)
         mylogger.info("新增技能子页面在标签选择框选择动作")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[5]/div/div/div/ul").click()
         time.sleep(2)
         mylogger.info("新增技能子页面在标签选择框缩回选项")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[5]/div/div/div/ul").send_keys(Keys.ESCAPE)
         time.sleep(3)
         mylogger.info("新增技能子页面点击上传技能")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-blueprint-add/form/nz-form-item[9]/nz-form-control/div/span/nz-upload/div/div/button").click()
         time.sleep(1)
         dialog = win32gui.FindWindow("#32770", "打开")
         # 向下传递
         ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
         comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
         # 编辑按钮
         edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
         # 打开按钮
         button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
         # 输入文件的绝对路径，点击“打开”按钮
         win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, "D:\Web_python_add_log\ATOM\ACom_TaiBao210517.pak")  # 发送文件路径
         win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
         time.sleep(5)
         mylogger.info("新增技能子页面点击取消")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-blueprint-add/div[3]/button[1]").click()
         #mylogger.info("新增技能子页面点击保存")
         #chrome_browser.find_element_by_xpath(
         #    "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-blueprint-add/div[3]/button[2]").click()
         mylogger.info("添加角色")
         mylogger.info("在资源管理里面点击角色管理")
         time.sleep(0.5)
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/layout-header/div/app-nav/ul[2]/li[1]").click()
         time.sleep(0.5)
         mylogger.info("在资源管理里面点击添加角色")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/app-character-list/nz-card/div/div/button").click()
         time.sleep(0.5)
         mylogger.info("在添加角色子页面输入角色名称")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-character-add/form/nz-form-item[1]/nz-form-control/div/span/input").send_keys("%s" % robot_sn_internet)
         time.sleep(0.5)
         mylogger.info("在添加角色子页面点击选择技能")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-character-add/form/div[1]/nz-card/div/div/button").click()
         time.sleep(1)
         mylogger.info("在选择技能子页面勾选技能")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[3]/div/nz-modal/div/div[2]/div/div/div/app-select-blueprint/div[2]/nz-table/nz-spin/div/div/div/div/table/tbody/tr[5]/td[1]/label/span[1]/input").click()
         time.sleep(1)
         mylogger.info("在选择技能子页面勾选技能后点击确定")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[3]/div/nz-modal/div/div[2]/div/div/div/app-select-blueprint/div[3]/button[2]").click()
         time.sleep(1)
         mylogger.info("在添加角色子页面点击 取消")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-character-add/form/div[2]/button[1]").click()
         #time.sleep(1)
         #mylogger.info("在添加角色子页面点击 保存")
         #chrome_browser.find_element_by_xpath(
         #    "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-character-add/form/div[2]/button[2]").click()
         mylogger.info("设备管理")
         time.sleep(0.5)
         mylogger.info("在设备管理里面点击设备管理")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/layout-header/div/app-nav/ul[1]/div[1]").click()
         time.sleep(0.5)
         mylogger.info("在设备管理里面点击添加机器人")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/app-myrobots-list/nz-card/div/div[2]/button[3]").click()
         time.sleep(1)
         mylogger.info("在添加机器人子页面硬件类型框点击")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-myrobots-add/form/div[1]/nz-form-item[1]/nz-form-control/div/span/nz-select/div/div/div").click()
         time.sleep(0.5)
         mylogger.info("在添加机器人子页面硬件类型框选择机器人")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[4]/div/div/div/ul/li[1]").click()
         time.sleep(0.5)
         mylogger.info("在添加机器人子页面机器人账号框输入机器人SN")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-myrobots-add/form/div[1]/nz-form-item[2]/nz-form-control/div/span/input").send_keys("%s" % robot_sn_internet)
         time.sleep(0.5)
         mylogger.info("在添加机器人子页面密码框输入密码")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-myrobots-add/form/div[1]/nz-form-item[3]/nz-form-control/div/span/input").send_keys("123456")
         mylogger.info("在添加机器人子页面输入验证码")
         time.sleep(1)
         mylogger.info("在添加角色子页面点击 取消")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-myrobots-add/form/div[2]/button[1]").click()
         #time.sleep(1)
         #mylogger.info("在添加角色子页面点击 保存")
         #chrome_browser.find_element_by_xpath(
         #    "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-myrobots-add/form/div[2]/button[2]").click()
         mylogger.info("进入设置资源页面")
         #####设置资源
         mylogger.info("设置资源页面搜索框输入机器号码")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/app-myrobots-list/nz-card/div/div[1]/form/nz-row/nz-col[1]/nz-form-item/nz-form-control/div/span/input").send_keys(
             "EVT3-06")
         time.sleep(0.5)
         ####点击搜索
         mylogger.info("设置资源页面点击搜索")
         chrome_browser.find_element_by_xpath("/html/body/app-root/layout-default/section/app-myrobots-list/nz-card/div/div[1]/form/nz-row/nz-col[2]/button[1]").click()
         time.sleep(2)
         #####勾选到搜索到的机器
         mylogger.info("勾选到搜索到的机器")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/app-myrobots-list/nz-card/div/nz-table/nz-spin/div/div/div/div/table/tbody/tr/td[1]/label/span[1]/input").click()
         time.sleep(1)
         #####设置资源
         mylogger.info("点击设置资源")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/section/app-myrobots-list/nz-card/div/div[2]/button[1]").click()
         time.sleep(2)
         mylogger.info("设置资源子页面")
         ###取消按钮
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-set-resource/form/div[2]/button[1]").click()
         # time.sleep(0.5)
         ###提交按钮
         # chrome_browser.find_element_by_xpath(
         #    "/html/body/div[2]/div[2]/div/nz-modal/div/div[2]/div/div/div/app-set-resource/form/div[2]/button[2]").click()
         time.sleep(0.5)
         mylogger.info("点击用户图像")
         chrome_browser.find_element_by_xpath(
             "/html/body/app-root/layout-default/layout-header/header/div/div[2]/ul/li[2]/header-user/div/div/nz-avatar/img").click()
         time.sleep(0.5)
         mylogger.info("点击退出登录")
         chrome_browser.find_element_by_xpath(
             "/html/body/div[2]/div[3]/div/div/div/div/div[3]").click()
         time.sleep(0.5)
         mylogger.info("关闭并退出浏览器")
         chrome_browser.quit()
         mylogger.info("结束RDP页面配置")

