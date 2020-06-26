import allure
from allure_commons.types import AttachmentType


class AddressPage:

    def __init__(self, driver):
        self.driver = driver
        self.additional_msg_textarea_name = 'message'
        self.proceed_checkout_further2_name = 'processAddress'
        self.additional_message_textarea_xpath = '//*[@id="ordermsg"]/textarea'

    @allure.step('Przejście dalej')
    def proceed_checkout_3(self):
        self.driver.find_element_by_name(self.proceed_checkout_further2_name).click()

    @allure.step('Wiadomość do sprzedawcy')
    def additional_message(self, message):
        self.driver.find_element_by_xpath(self.additional_message_textarea_xpath).click()
        self.driver.find_element_by_xpath(self.additional_message_textarea_xpath).send_keys(message)
        allure.attach(self.driver.get_screenshot_as_png(), name='wpisywanie wiadomości', attachment_type=AttachmentType.PNG)
