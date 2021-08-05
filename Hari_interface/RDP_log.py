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
         rdp_url = config.get("urlName_interface", "url_RDP")
         url_rdp_login_user = config.get("url_login", "url_rdp_user")
         url_rdp_login_passwd = config.get("url_login", "url_rdp_passwd")
         url_hari_customer_code = config.get("url_input_info", "hari_customer_code")
         url_upload_acomfile = config.get("uploadfile", "Acomfilename")
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
         time.sleep(5)
         mylogger.info("展开接口界面操作第一列")
         chrome_browser.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[1]/div/div/button").click()
         time.sleep(1)
         mylogger.info("点击Try it out")
         chrome_browser.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[1]/div/div[2]/div/div[1]/div[1]/div[2]/button").click()
         #mylogger.info("点击选择文件")
         #chrome_browser.find_element_by_xpath(
         #    "/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[1]/div/div[2]/div/div[1]/div[3]/div[2]/div/table/tbody/tr/td[2]/div/input").click()
         mylogger.info("选择文件")
         chrome_browser.find_element_by_xpath(
             "/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[1]/div/div[2]/div/div[1]/div[3]/div[2]/div/table/tbody/tr/td[2]/div/input").send_keys(
             "%s" % url_upload_acomfile)
         #chrome_browser.find_element_by_xpath(
         #    "/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[1]/div/div[2]/div/div[1]/div[3]/div[2]/div/table/tbody/tr/td[2]/div/input").send_keys(
         #    "D:\UI_Hari_setup\ATOM\ACom_TaiBao210517.pak")
         time.sleep(2)
         mylogger.info("点击执行")
         chrome_browser.find_element_by_xpath(
             "/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[1]/div/div[2]/div/div[2]/button").click()
         mylogger.info("收起接口界面操作第一列")
         time.sleep(3)
         chrome_browser.find_element_by_xpath(
             "/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[1]/div/div[1]/button").click()
         time.sleep(1)
         mylogger.info("展开接口界面操作第二列")
         chrome_browser.find_element_by_xpath(
             "/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[2]/div/div/button").click()
         time.sleep(0.5)
         mylogger.info("点击Try it out")
         chrome_browser.find_element_by_xpath(
             "/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[2]/div/div[2]/div/div[1]/div[1]/div[2]/button").click()
         time.sleep(1)
         #mylogger.info("填写134环境")
         #chrome_browser.find_element_by_xpath(
         #    "/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[2]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/input").send_keys("134")
         #time.sleep(0.5)
         mylogger.info("robot_user_code框清除")
         chrome_browser.find_element_by_xpath(
             "/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[2]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/input").clear()
         time.sleep(0.5)
         mylogger.info("robot_user_code框填写SN")
         chrome_browser.find_element_by_xpath(
             "/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[2]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/input").send_keys("%s" % robot_sn_internet)
         time.sleep(1)
         mylogger.info("点击执行")
         chrome_browser.find_element_by_xpath(
             "/html/body/div/div/div[2]/div[3]/section/div/span/div/div/div/span[2]/div/div[2]/div/div[2]/button").click()
         time.sleep(5)
         mylogger.info("关闭并退出浏览器")
         chrome_browser.quit()
         mylogger.info("结束RDP页面配置")

