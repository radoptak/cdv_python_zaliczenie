from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
driver.find_element_by_id('email').send_keys('test1@wp.pl')
driver.find_element_by_id('passwd').send_keys('Pwd123#')
driver.find_element_by_id('SubmitLogin').click()
ac = driver.find_element_by_class_name('account').get_attribute('textContent')
usr = driver.find_element_by_class_name('page-heading').get_attribute('textContent')

if usr == 'My account':
    assert ac == 'Roman Kowalski'
    print('OK')
else:
    print('nope')

print(ac)
print(usr)
