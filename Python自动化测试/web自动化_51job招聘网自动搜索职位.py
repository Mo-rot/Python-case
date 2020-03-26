# 实例：自动化打开浏览器，进入51job招聘网站，搜索职位招聘信息和选择职位地区

from selenium import webdriver

# 打开Chrome浏览器，然后进入网站
driver = webdriver.Chrome(r"D:\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://jobs.51job.com/")

# 定位到输入框，然后输入搜索内容
driver02 = driver.find_element_by_id("kwdselectid")
driver02.send_keys("自动化测试工程师")

# 点击“工作地点”,进入到“选择地区”界面
driver03 = driver.find_element_by_id("work_position_input")
driver03.click()

# 这里用了css表达式：#代表某个标签的id，em[class=on] 表示 em标签下的class属性
driver04 = driver.find_elements_by_css_selector("#work_position_click_center_right_list_000000 em[class=on]")

# 在“选择地区”页面中取消选择已经选中的城市
for driver05 in driver04:
    driver05.click()

# 点击选择地区页面的“当前定位城市”的城市
driver.find_element_by_id("work_position_click_ip_location_000000_020000").click()
# 点击选择地区页面的“确定”
driver.find_element_by_id("work_position_click_bottom_save").click()
# 点击搜索按钮
driver.find_element_by_css_selector("#searchForm button").click()

# 关闭浏览器
# driver.quit()
