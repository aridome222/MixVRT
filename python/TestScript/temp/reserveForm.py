# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

class TestA():
  def setup_method(self, method):
    options = Options()
    # options.add_argument('--headless')  # ヘッドレスモードでブラウザを起動
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    self.driver = webdriver.Remote(command_executor='http://chrome:4444/wd/hub', options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_a(self):
    self.driver.get("http://example.selenium.jp/reserveApp_Renewal/")
    self.driver.set_window_size(1463, 1039)
    self.driver.find_element(By.ID, "datePick").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .day:nth-child(2)").click()
    self.driver.find_element(By.ID, "reserve_term").click()
    dropdown = self.driver.find_element(By.ID, "reserve_term")
    dropdown.find_element(By.XPATH, "//option[. = '3']").click()
    self.driver.find_element(By.ID, "headcount").click()
    dropdown = self.driver.find_element(By.ID, "headcount")
    dropdown.find_element(By.XPATH, "//option[. = '5']").click()
    self.driver.find_element(By.ID, "breakfast_off").click()
    self.driver.find_element(By.ID, "plan_a").click()
    self.driver.find_element(By.ID, "plan_b").click()
    self.driver.find_element(By.ID, "plan_b").click()
    self.driver.find_element(By.LINK_TEXT, "各プランの詳細").click()
    assert self.driver.switch_to.alert.text == "未実装"
    # アラートが表示される可能性があるので、accept() を呼ぶ
    self.driver.switch_to.alert.accept()
    self.driver.find_element(By.ID, "guestname").click()
    self.driver.find_element(By.ID, "guestname").send_keys("czfd")
    self.driver.find_element(By.ID, "disagree").click()
    assert self.driver.switch_to.alert.text == "未実装"
    # アラートが表示される可能性があるので、accept() を呼ぶ
    self.driver.switch_to.alert.accept()
    self.driver.find_element(By.ID, "agree_and_goto_next").click()
    self.driver.find_element(By.ID, "returnto_index").click()
    self.driver.find_element(By.ID, "datePick").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) > .day:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, "h3:nth-child(9)").click()
    self.driver.find_element(By.ID, "agree_and_goto_next").click()
    self.driver.find_element(By.ID, "commit").click()
    self.driver.find_element(By.ID, "returnto_checkInfo").click()
