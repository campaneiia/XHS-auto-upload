"""
Copyright (C) 2023 musicnbrain.org

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import Config
import Cookie
import Init
import Create


def select_user():
    while Config.UserList:
        for i, v in enumerate(Config.UserList):
            print(f"{i + 1}.{v}", end="\t")
        select = input("\nSelect account (Enter 'n' to log in by phone number)：")
        if select == 'n':
            # log in by phone num
            Config.login_status = True
            return
        try:
            Config.CurrentUser = Config.UserList[int(select) - 1]
            return
        except (ValueError, IndexError):
            print("Invalid number")


def login_successful():
    # get ID
    name_content = WebDriverWait(Config.Browser, 10, 0.2).until(
        lambda x: x.find_element(By.CSS_SELECTOR, ".name-box")).text
    print(f"Hello {name_content}, log in successful")
    Config.Browser.get("https://creator.xiaohongshu.com/publish/publish")
    Config.CurrentUser = name_content
    
    Cookie.get_new_cookie()
    Cookie.save_cookie()


def cookie_login():
    Cookie.set_cookie()
    try:
        WebDriverWait(Config.Browser, 10, 0.2).until(
            lambda x: x.find_element(By.CSS_SELECTOR, ".name-box")).text
    except TimeoutException:
        Config.login_status = True
        return
    login_successful()


def login():
    Config.Browser.get("https://creator.xiaohongshu.com/login")
    if not Config.login_status:
        if Cookie.check_cookie_expiry():
            cookie_login()
            return
        else:
            Config.login_status = True
    
    while True:
        phone = input("Enter your phone number (China Mainland):")
        if len(phone) == 11:
            break
        print("Invalid phone number")
    
    # send verification
    input_phone = Config.Browser.find_element(By.CSS_SELECTOR,"input[placeholder='手机号']")
    input_phone.send_keys(phone)

    send_code_button = Config.Browser.find_element(By.XPATH, "//*[contains(text(), '发送验证码')]")
    send_code_button.click()

    code = input("Verification code:")
    # back to previous menu
    if code.lower() == 'back':
        return login() 
    
    while len(code) != 6:
        print("Verification code must be 6 digits, please try again")
        code = input("Verification code:")

    code_input = Config.Browser.find_element(By.CSS_SELECTOR, "input[placeholder='验证码']")
    code_input.send_keys(code)

    login_button = Config.Browser.find_element(By.CSS_SELECTOR, "button.css-1jgt0wa.css-kyhkf6")
    login_button.click()

    login_successful()


def switch_users():
    print("Logging out...")
    Config.Browser.delete_all_cookies()
    select_user()
    login()


def Quit():
    Cookie.save_cookie()
    print("Script exiting...")
    Config.Browser.quit()
    sys.exit(0)


def select_create():
    while True:
        if Config.Browser.current_url != "https://creator.xiaohongshu.com/publish/publish":
            Config.Browser.get("https://creator.xiaohongshu.com/publish/publish")
        print("1.Video Upload 2.Image Upload 3.Switch User 4.Exit")
        select = input("Select function:")
        match select:
            case '1':
                Create.create_video()
                return
            case '2':
                Create.create_image()
                return
            case '3':
                switch_users()
                return
            case '4':
                Quit()
                return
            case default:
                print("Invalid number")


def start():
    try:
        # initialize
        print("Welcome to the XHS auto-uploading helper, at any time, \n use 'ctrl+c' to exit this script, \n and enter 'back' to go back to the previous menu")
        Init.init()
        select_user()
        login()
        while True:
            # select function
            select_create()
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error happened：\n{e}")
