from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
driver.find_element_by_id('email').send_keys('test1@wp.pl')
driver.find_element_by_id('passwd').send_keys('Pwd123#')
driver.find_element_by_id('SubmitLogin').click()
driver.find_element_by_id('search_query_top').click()
driver.find_element_by_id('search_query_top').send_keys('dress')
driver.find_element_by_class_name('button-search').click()
driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[2]/div/div[1]/div/a[1]/img').click()
driver.find_element_by_xpath('//*[@id="add_to_cart"]/button/span').click()
driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a').click()
driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]').click()
driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button').click()
driver.find_element_by_id('cgv').click()
driver.find_element_by_xpath('//*[@id="form"]/p/button').click()

price_str = driver.find_element_by_xpath('//td[contains(@class, "cart_total")]//span[contains(@class, "price")]').get_attribute('textContent')
price_stripped = price_str.strip()
price = price_stripped[1:]
price_float = float(price)

ship_str = driver.find_element_by_xpath('//*[@id="total_shipping"]').get_attribute('textContent')
ship = ship_str[1:]
ship_float = float(ship)

tax_str = driver.find_element_by_xpath('//*[@id="total_tax"]').get_attribute('textContent')
tax = tax_str[1:]
tax_float = float(tax)

total_str = driver.find_element_by_xpath('//*[@id="total_price"]').get_attribute('textContent')
total = total_str[1:]
total_float = float(total)

final = price_float + ship_float + tax_float
assert total_float == final

print(price_float)
print(ship_float)
print(tax_float)
print(total_float)
print(price_float + ship_float + tax_float)
# print(type(price_float))
sleep(3)





# ac = driver.find_element_by_class_name('account').get_attribute('textContent')
# usr = driver.find_element_by_class_name('page-heading').get_attribute('textContent')
# if usr == 'My account':
#     assert ac == 'Roman Kowalski'
#     print('OK')
# else:
#     print('nope')
#
# print(ac)
# print(usr)
