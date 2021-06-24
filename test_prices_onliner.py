from Base import Base
from selenium.webdriver.common.by import By


class Locators:
    catalog = (By.XPATH, "/html//div[@id='container']/div[@class='g-container-outer']//"
                         "nav[@class='b-top-navigation']/ul[@class='b-main-navigation']//"
                         "a[@href='https://catalog.onliner.by/']")
    section_auto = (By.XPATH, "/html//div[@id='container']/div[@class='g-container-outer']//"
                              "div[@class='g-middle-i']/div[1]/ul/li[7]")
    section_disc = (By.XPATH, "/html//div[@id='container']/div[@class='g-container-outer']//div[@class='g-middle-i']/"
                              "div[1]/div[3]/div/div[6]/div[1]/div/div[1]/"
                              "div[@class='catalog-navigation-list__aside-title']")
    section_disc_choose = (By.XPATH, "/html//div[@id='container']/div[@class='g-container-outer']/"
                              "div[@class='l-gradient-wrapper']//div[@class='g-middle-i']/"
                              "div[1]/div[3]/div/div[6]/div[1]//a[@href='https://catalog.onliner.by/wheel']")
    disc_name = (By.XPATH, "//div[@id='schema-products']/div[1]/div[@class='schema-product']//div[3]//div[2]//div[1]")
    disc_price = (By.XPATH, "//div[@id='schema-products']/div[1]/div[@class='schema-product']//div[3]//div[1]//div[1]//"
                            "div[1]//div[1]//a//span")
    search_field = (By.XPATH, "//div[@id='fast-search']/form[@action='//catalog.onliner.by/search/']/"
                              "input[@name='query']")
    frame = "/html//div[@id='fast-search-modal']//iframe[@class='modal-iframe']"
    frame_price = (By.XPATH, "//*[@id='search-page']/div[2]/ul/li/div/div/div[1]/div/div/a/span")


class Test_onliner_prices:

    def test_price(self, browser):
        page = Base(browser)
        page.go_to_site()
        catalog = page.find_element(Locators.catalog)
        catalog.click()
        section = page.find_element(Locators.section_auto)
        section.click()
        section_disc = page.find_element(Locators.section_disc)
        section_disc.click()
        section_disc_choose = page.find_element(Locators.section_disc_choose)
        section_disc_choose.click()
        choose_disk_name = page.find_element(Locators.disc_name).text
        choose_disk_price = page.find_element(Locators.disc_price).text
        search_disk = page.find_element(Locators.search_field).send_keys(choose_disk_name)
        page.switch_to_frame(Locators.frame)
        price_from_frame = page.find_element(Locators.frame_price).text
        assert choose_disk_price == price_from_frame

