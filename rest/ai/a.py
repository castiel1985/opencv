# coding: utf-8
#导入所需要的模块
from selenium import webdriver
import time

#生成一个driver变量
driver = webdriver.Firefox()

#浏览器最大化
# driver.maximize_window()
#自定义浏览器的宽和高
# driver.set_window_size(666,555)

url = "https://www.dingdiann.com/ddk38807/2519173.html"
#打开url链接
driver.get(url)
time.sleep(5)
#打印打开页面的title
print("网站title",driver.title)

#截图并保存为1.png
driver.get_screenshot_as_file("1.png")

#刷新当前页面
driver.refresh()

time.sleep(3)
driver.get("http://www.baidu.com")
print("网站的title",driver.title)

driver.back()    #后退
driver.forward()#前进

driver.close()     #关闭页面，进程还在
# driver.quit()   #关闭浏览器，进程杀死