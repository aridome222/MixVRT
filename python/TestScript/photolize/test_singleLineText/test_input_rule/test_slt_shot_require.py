# 単一行テキスト
# 編集画面で入力後、ビュー画面スクショ（設定を変えた時に実行すべきファイル）
# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.keys import Keys
import json
import os
from datetime import datetime
import difflib


class Test_slt_input_addShot():
  def setup_method(self, method):
    options = Options()
    # options.add_argument('--headless')  # ヘッドレスモードでブラウザを起動
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    self.driver = webdriver.Remote(command_executor='http://chrome:4444/wd/hub', options=options)
    self.driver.implicitly_wait(10) # 10秒まで待機する
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_singlelinetext(self):    
    # photolizeにログインする
    self.driver.get("https://saruya:saruya@staging-user.photolize.jp/login/basic_auth")
    self.driver.get("https://staging-user.photolize.jp/login")
    self.driver.set_window_size(1463, 1032)
    self.driver.find_element(By.ID, "input-7").click()
    self.driver.find_element(By.ID, "input-7").send_keys("company_code26")
    self.driver.find_element(By.CSS_SELECTOR, ".v-btn__content").click()
    self.driver.find_element(By.ID, "input-11").send_keys("aridome")
    self.driver.find_element(By.ID, "input-14").send_keys("aridome")
    self.driver.find_element(By.CSS_SELECTOR, ".btn > .v-btn__content").click()
    # # 有留アプリテストを選択
    # self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/main/div/div[2]/div[2]/div/div[15]/a/div/div/div[2]/div").click()
    # time.sleep(100)
    # 直接飛ぶ
    self.driver.get("https://staging-user.photolize.jp/appli/index?app_id=151")
    # 新規レコードを選択
    self.driver.find_element(By.CSS_SELECTOR, "#appli-layout > div.appli-template-foot > a").click()
    # 必須入力
    self.driver.find_element(By.CSS_SELECTOR, ".plz-elm:nth-child(8) > .disp-wrap").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(10) .v-card__actions .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "input-367").send_keys("テスト")
    self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(10) .v-card__actions .v-btn__content").click()
    # 半角英数のみ
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".plz-elm:nth-child(30) > .disp-wrap").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(31) .v-card__actions .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "input-508").send_keys("test")
    self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(31) .v-card__actions .v-btn__content").click()
    # メールアドレス入力
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".plz-elm:nth-child(25) > .disp-wrap").click()
    self.driver.find_element(By.ID, "input-475").send_keys("a@test.com")
    self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(26) .v-card__actions > .v-btn").click()
    # URL入力
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".plz-elm:nth-child(9) > .disp-wrap").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(11) .v-card__actions .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "input-373").send_keys("https://test")
    self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(11) .v-card__actions .v-btn__content").click()
    # 重複禁止
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".plz-elm:nth-child(21) > .disp-wrap").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(22) .v-card__actions .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "input-449").send_keys("テスト")
    self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(22) .v-card__actions .v-btn__content").click()
    # 編集不可
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".plz-elm:nth-child(31) > .disp-wrap").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(32) .v-icon")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(32) .v-icon").click()
    # 最大文字数（３文字）
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".plz-elm:nth-child(22) > .disp-wrap").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(23) .v-card__actions .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "input-456").send_keys("テスト")
    self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(23) .v-card__actions .v-btn__content").click()
    # 最小文字数（３文字）
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".plz-elm:nth-child(19) > .disp-wrap").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(20) .v-card__actions .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "input-437").send_keys("テスト")
    self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(20) .v-card__actions .v-btn__content").click()
    # 新規レコードを保存
    self.driver.find_element(By.CSS_SELECTOR, ".fa-floppy-disk > path").click()
    # element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".theme--light:nth-child(2) > .v-btn__content")))
    # element.click()
    time.sleep(3)
    # スクリーンショットをとる
    save_screenShot(self)

    # # 最新のビューを選択
    # self.driver.find_element(By.CSS_SELECTOR, ".ag-row-even:nth-child(1) .mr-1:nth-child(2) .v-icon").click()
    # # スクリーンショットをとる
    # save_screenShot(self)
    # time.sleep(3) # 目視確認
    # # ログアウトする
    # self.driver.find_element(By.CSS_SELECTOR, ".v-avatar > img").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".v-btn--text > .v-btn__content").click()
    # 画面を閉じる
    self.driver.close()

def save_screenShot(self):
  # 保存先ディレクトリを指定
  output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img/")
  # フォルダが存在しない場合は作成
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)
  # 現在の日付を取得してフォーマット
  current_date = datetime.now().strftime("%m-%d_%H-%M-%S")
  # ファイル名を生成
  output_file_name = f"SLT_view_af_{current_date}.png"

  # ファイルパスを作成
  output_file_path = os.path.join(output_dir, output_file_name)
  
  # スクロールバーが表示されないようにサイズを設定
  self.driver.set_window_size(1050, 1150) # 幅×高さ

  # 追加: ここでフルページのスクリーンショットを取る
  self.driver.save_screenshot(output_file_path)

  print("")
  print(f"単一行テキストの配置画像を{output_file_path}に保存しました")
