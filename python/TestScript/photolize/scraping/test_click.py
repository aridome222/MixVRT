# data属性による指定＋HTMLから一致する要素を取得し保存
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
import regex
from selenium.webdriver.common.keys import Keys
import json
import os
from datetime import datetime
import difflib
import subprocess


class TestClick():
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
  
  def test_addNewRecord(self):
    # photolizeにログインする
    self.driver.get("https://saruya:saruya@staging-user.photolize.jp/login/basic_auth")
    self.driver.get("https://staging-user.photolize.jp/login")
    self.driver.set_window_size(1463, 1032)
    self.driver.find_element(By.ID, "input-7").click()
    self.driver.find_element(By.ID, "input-7").send_keys("company_code26")
    # クリックした要素を取得
    element = self.driver.switch_to.active_element
    # 属性値を取得
    id = element.get_attribute("id")
    value = element.get_attribute("value")
    print("")
    print("")
    print("＜取得した情報＞")
    print(id)
    print(value)
    # self.driver.find_element(By.CSS_SELECTOR, ".v-btn__content").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-btn__content")
    # element.click()
    # coordinate_click(self, element)
    loc = element.location
    x, y = loc['x'], loc['y']
    # print(x)
    # print(y)
    actions = ActionChains(self.driver)
    actions.move_by_offset(x, y)
    # actions.move_to_element_with_offset(self.driver.find_element(By.TAG_NAME, 'body'), x, y)
    actions.click()
    time.sleep(1)
    actions.perform()
    time.sleep(1)
    self.driver.find_element(By.ID, "input-11").send_keys("aridome")
    self.driver.find_element(By.ID, "input-14").send_keys("aridome")
    # self.driver.find_element(By.CSS_SELECTOR, ".btn > .v-btn__content").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn > .v-btn__content")
    loc = element.location
    x, y = loc['x'], loc['y']
    print(x)
    print(y)
    actions = ActionChains(self.driver)
    actions.move_by_offset(x, y)
    time.sleep(1)
    
    # ## 有留アプリテストを選択
    # # 直接飛ぶ
    # self.driver.get("https://staging-user.photolize.jp/appli/index?app_id=151")
    # # 新規レコードの編集を選択
    # self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/a/span/i").click()

    # actions = ActionChains(self.driver)
    # actions.move_to_element_with_offset(self.driver.find_element_by_tag_name('body'), 100, 200).click().perform()

    # # 指定した座標にある要素を取得
    # x = 100
    # y = 200
    # element = self.driver.execute_script(f"return document.elementFromPoint({x}, {y});")

    # # 取得した要素を操作したり、プリントしたり
    # print(element)

    # # ラベルの入力欄を選択
    # element = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/main/div/div[2]/div/div/div[3]/div[10]/div[1]")
    # element.click()

    # # # 少し待つ
    # # time.sleep(1)

    # # HTMLデータからbody部分を取得
    # page_source = self.driver.page_source

    # # BeautifulSoupを使ってbody部分のみを抽出
    # soup = BeautifulSoup(page_source, 'html.parser')
    # body_content = soup.body

    # # 特定の条件に一致する<div>要素を取得
    # pattern = regex.compile(r'[\p{Script=Hiragana}\p{Script=Katakana}\p{Script=Han}\p{Z}ー、。，。]', regex.UNICODE) # regex.compile関数と\p{Z}を使う

    # # <div>要素内のテキストを検索
    # div_elements = body_content.find_all('div', string=pattern)

    # # 取得したdiv要素を出力
    # for div in div_elements:
    #     print(div.text)

    # 画面を閉じる
    self.driver.close()
  
def coordinate_click(self, element):
  ### 要素の（x, y）座標をActionChainsを使用してクリックする ###
  loc = element.location
  x, y = loc['x'], loc['y']
  print(x)
  print(y)
  actions = ActionChains(self.driver)
  actions.move_to_element_with_offset(self.driver.find_element(By.TAG_NAME, 'body'), x, y)
  actions.click().perform()
  # actions.move_by_offset(x, y)
  # actions.click().perform()

def get_id_from_body(self, keyWord):
  ### HTMLのbody部分から一致した要素をtxtファイルに出力する ###

  # ページソースを取得
  page_source = self.driver.page_source

  # BeautifulSoupを使ってbody部分のみを抽出
  soup = BeautifulSoup(page_source, 'html.parser')
  body_content = soup.body

  # 特定のclass属性を持つdiv要素を取得
  div_elements = body_content.find_all('div', class_='my-div')

  # 取得したdiv要素を出力
  for div in div_elements:
      print(div.text)

  # 正規表現オブジェクトを作成
  pattern = re.compile(keyWord)

  # bodyから正規表現に一致するテキストを含む要素をすべて取得
  matches = body_content.find_all(name=pattern)

  # 一致する要素を取得できたかどうかで異なる処理を行う
  if matches: # 取得できた場合
      print("一致する要素が見つかりました")
      # 一致する要素をtxtファイルに保存
      save_matching_elements_to_txt(matches)
      # 一致する要素をjsonファイルに保存
      save_matching_elements_to_json(matches)
      return
  else: # 取得できなかった場合
      print("一致する要素が見つかりませんでした")
  
def save_matching_elements_to_txt(matches):
  ### 一致した要素をtxtファイルに出力する ###

  # 保存先ディレクトリを指定
  output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "txt/")
  # フォルダが存在しない場合は作成
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)
      command = f"sudo chown -R aridome:aridome {output_dir}"
      # コマンドを実行
      subprocess.call(command, shell=True)
      
  # 現在の日付を取得してフォーマット
  current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  # ファイル名を生成
  output_file_name = f"matching_elements_{current_date}.txt"
  
  # txtファイルに出力
  output_file_path = os.path.join(output_dir, output_file_name)
  with open(output_file_path, 'w', encoding='utf-8') as f:
      for match in matches:
          f.write(str(match) + '\n')
  
  print(f"一致した要素を{output_file_path}に保存しました")
  return output_file_path

def save_matching_elements_to_json(matches):
  ### 一致した要素をjsonファイルに出力する ###

  # 保存先ディレクトリを指定
  output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "json/")
  # フォルダが存在しない場合は作成
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)
      command = f"sudo chown -R aridome:aridome {output_dir}"
      # コマンドを実行
      subprocess.call(command, shell=True)

  # 現在の日付を取得してフォーマット
  current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  # ファイル名を生成
  output_file_name = f"matching_elements_{current_date}.json"

  # 一致する要素をリストに格納
  matching_elements = []
  for match in matches:
      matching_elements.append(str(match))
  
  # JSONファイルに出力
  output_file_path = os.path.join(output_dir, output_file_name)
  with open(output_file_path, 'w', encoding='utf-8') as f:
      json.dump(matching_elements, f, ensure_ascii=False, indent=4)
  
  print(f"一致する要素を{output_file_path}に保存しました")

def save_html_data(file_name, html_data):
  ### HTMLデータをhtmlファイルに出力する ###

  # 保存先ディレクトリを指定
  output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html_data/")
  # フォルダが存在しない場合は作成
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)
      command = f"sudo chown -R aridome:aridome {output_dir}"
      # コマンドを実行
      subprocess.call(command, shell=True)
      
  # 現在の日付を取得してフォーマット
  current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  # ファイル名を生成
  output_file_name = f"{file_name}_{current_date}.html"
  
  # ファイルにHTMLデータを出力
  output_file_path = os.path.join(output_dir, output_file_name)
  with open(output_file_path, "w", encoding="utf-8") as f:
      f.write(html_data)

  print(f"HTMLデータを{output_file_path}に保存しました")

def save_diff_html_data(html_data_file, html_data_file_2):
  ### ２つのHTMLデータの差分をtxtファイルに出力する ###

  # 保存先ディレクトリを指定
  output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html_diff/")
  # フォルダが存在しない場合は作成
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)
      command = f"sudo chown -R aridome:aridome {output_dir}"
      # コマンドを実行
      subprocess.call(command, shell=True)

  # 現在の日付を取得してフォーマット
  current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  # ファイル名を生成
  output_file_name = f"diff_{current_date}.txt"

  # 差異を別ファイルに出力
  differ = difflib.Differ()
  diff = differ.compare(html_data_file.splitlines(), html_data_file_2.splitlines())

  output_file_path = os.path.join(output_dir, output_file_name)
  with open(output_file_path, "w", encoding="utf-8") as f:
      f.write("\n".join(diff))

  print(f"2つのHTMLデータの差異を{output_file_path}に保存しました")

def save_diff_id(txt_file_path, txt_file_path_2):
  ### 2つのHTMLテキストデータの差分をtxtファイルに出力する ###

  # 保存先ディレクトリを指定
  output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diff_id/")
  # フォルダが存在しない場合は作成
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)
      command = f"sudo chown -R aridome:aridome {output_dir}"
      # コマンドを実行
      subprocess.call(command, shell=True)

  # 現在の日付を取得してフォーマット
  current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  # ファイル名を生成
  output_file_name = f"diff_id_{current_date}.txt"

  # ファイルを読み込んで内容を取得
  with open(txt_file_path, "r", encoding="utf-8") as f:
      txt_data = f.read()

  with open(txt_file_path_2, "r", encoding="utf-8") as f:
      txt_data_2 = f.read()

  # 差異を別ファイルに出力
  differ = difflib.Differ()
  diff = differ.compare(txt_data.splitlines(), txt_data_2.splitlines())

  output_file_path = os.path.join(output_dir, output_file_name)
  with open(output_file_path, "w", encoding="utf-8") as f:
      f.write("\n".join(diff))

  print(f"2つのHTMLテキストデータの差異を{output_file_path}に保存しました")
