import unittest
from time import sleep

from django.test import LiveServerTestCase

from selenium.webdriver.firefox.webdriver import WebDriver


class MyTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.selenium.quit()

    def test_enter_url(self):
        input_url = 'http://www.20minutes.fr/monde/1804995-20160312-tunisie-appelle-dons-lutter-contre-terrorisme'
        language = 'French'

        self.selenium.get(self.live_server_url)

        input_element = self.selenium.find_element_by_id('input-url')
        language_element = self.selenium.find_element_by_name('dest_lang')
        study_element = self.selenium.find_element_by_class_name('btn-default')

        input_element.send_keys(input_url)
        language_element.send_keys(language)
        study_element.click()
