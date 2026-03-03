# -*- coding:utf-8 -*-

class SolarFirstPage:
    def __init__(self, driver):
        self.driver = driver

    def open_solar_first_page(self):
        self.driver.get("http://example.com/solar_first_page")
        self.driver.implicitly_wait(10)
        print("Solar first page opened successfully.")