from selenium import webdriver
import traceback

from selenium.webdriver.chrome.options import Options
import time
import os

from selenium.webdriver.common.action_chains import ActionChains
# to type `stuff etc`, press entere etc
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import datetime
import os
from selenium.webdriver.support.ui import WebDriverWait

import logging

logging.basicConfig(filename='app.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger()

# Loads chrome with default settings
opt = Options()
opt.add_argument("start-maximized")  # maximizing the screen
opt.add_argument("--disable-extensions")  # not allowing extensions to load up

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

# Gives path to chrome WebDriverWait.driver and loads classroom webpage
# driver = WebDriverWait.driver.Edge(PATH)
# driver.get('https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession')


class Main:
    def __init__(self):
        '''initializes variables and opens up the browser'''
        logger.info("Opening up browser")

        self.PATH = "C:\\Users\\devi\Desktop\\Rahul\PythonCoding\\Learn\Python\Selenium__\\msedgedriver_older.exe"

        self.driver = webdriver.Edge(self.PATH)

        # Gives path to chrome WebDriverWait.driver and loads classroom webpage
        self.driver.get('https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession')

    def log_into_gmail(self):
        '''logs into my email account'''

        try:
            logger.info("Giving my email address")

            # giving the email
            email_input = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "identifierId"))
            )

            email_input.send_keys(os.environ.get("gmail_email"))
            self.driver.find_element_by_id("identifierNext").click()

        except Exception as err:
            logging.error(f"Error occurred: {err}")
            traceback.print_exc()

        try:
            logger.info("Giving my password")

            time.sleep(5)
            # giving the password
            password_input = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )

            password_input.send_keys(os.environ.get("gmail_pass"))

            # clicking sign in
            self.driver.find_element_by_id("passwordNext").click()

        except Exception as err:
            logging.critical(f"Error occurred: {err}")
            traceback.print_exc()

        else:
            return self.which_class()

    def which_class(self):
        '''Finds out what class i have and joins it'''
        logging.info(f"Finding out which class to join")

        localtime = time.localtime()
        time_now = f"{localtime.tm_hour}:{localtime.tm_min}"
        # to tind out what day it is
        day = datetime.datetime.now().strftime("%A")
        self.class_time = 45*60

        if day == "Monday":
            logger.info("It is Monday")
            # bot would join 5 mins early
            self.join_Math()

            self.join_Eng()
            self.join_Comp()

            # break
            time.sleep(25*60)

            self.join_Chem()
            self.join_Chem()

            # break
            time.sleep(25*60)

            self.join_Physics()
            self.join_Spanish()

        if day == "Tuesday":
            logger.info("It is Tuesday")

            self.join_chemistry()
            self.join_Math()

            self.join_Physics()
            self.join_Physics()

            time.sleep(25*60)

            self.join_Acc()
            self.join_Acc()

            time.sleep(25*60)

            self.join_Spanish()
            self.join_Eng()

        if day == "Wednesday":
            logger.info("It is Wednesday")

            self.join_Eng()
            self.join_Spanish()

            self.join_Acc()
            self.join_Eng()

            time.sleep(60*25)

            self.join_Math()
            self.join_Eng()

            time.sleep(60*25)

            self.join_Chem()
            self.join_Comp()

        if day == "Thursday":
            logger.info("It is Thursday")

            self.join_chemistry()
            self.join_Acc()

            self.join_Comp()
            self.join_Math()

            time.sleep(25*60)

            self.join_Physics()
            self.join_Spanish()

            time.sleep(25*60)

            self.join_Eng()
            self.join_Math()

        if day == "Friday":
            logger.info("It is Friday")

            self.join_Comp()
            self.join_Comp()

            self.join_Spanish()
            self.join_Math()

            time.sleep(25*60)

            self.join_Acc()
            self.join_Physics()

            time.sleep(25*60)
            self.join_Eng()

        logger.info("School os over or there is no school")
        # to sign out
        Sign_Out(self.driver, 5)

    def join_class_room(self, class_number):
        '''finds the classroom and clicks it'''
        logger.info("Going to the classroom")

        # Finds the classroom   assessing CS
        classroom = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class, 'YVvGBb csjh4b')]"))
        )[class_number]

        classroom.click()

    def join_meet_switch_tabs(self):
        '''goes to the next tab, and joins the meet'''
        logger.info("Switching tabs")

        # Switches the tab
        # self.driver.switch_to.window(self.driver.window_handles[1])
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
        except Exception as err:
            pass
        return self.join_meet()

    def join_Comp(self):
        '''joins my Computer Science class room'''
        logger.info("Going to Computer Science")

        self.join_class_room(3)
        # clicks on the meet link
        link = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "https://meet.google.com/lookup/gtsn2d5uvg"))
        )

        link.click()
        return self.join_meet_switch_tabs()

    def join_Eng(self):
        '''joins my English classroom'''
        logger.info("Going to English")

        self.join_class_room(6)
        # clicks on the meet link
        link = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "https://meet.google.com/lookup/hdo7g4uwfi"))
        )

        link.click()
        return self.join_meet_switch_tabs()

    def join_Chem(self):
        '''joins my Chemistry classroom'''
        logger.info("Going to Chemistry")

        self.join_class_room(5)
        # clicks on the meet link
        link = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "https://meet.google.com/lookup/bf6lbncayn"))
        )

        link.click()
        return self.join_meet_switch_tabs()

    def join_Acc(self):
        '''joins my Accounting class'''
        logger.info("Joining Accounting class")
        time.sleep(45*60)

    def join_Math(self):
        '''joins my Math class'''
        logger.info("Joining Maths class")

        self.join_class_room(0)
        # clicks on the meet link
        link = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "https://meet.google.com/lookup/bf6lbncayn"))
        )
        return self.join_meet_switch_tabs()

    def join_Physics(self):
        '''joins my Physics class'''
        logger.info("Joining Physics class")
        time.sleep(45*60)

    def join_Spanish(self):
        '''joins my Spanish class'''
        logger.info("Joining Spanish class")
        time.sleep(45*60)

    def join_meet(self):
        '''turns of mic, camera, and joins the meet'''
        logger.warning("Joining the meet")

        turn_off_mic_action = ActionChains(self.driver)
        #                               ctrl + d --> turns of mic
        turn_off_mic_action.key_down(Keys.CONTROL).send_keys(
            "d").key_up(Keys.CONTROL).perform()

        # turns of my camera
        turn_off_camera_action = ActionChains(self.driver)
        #                               ctrl + e --> turns of camera
        turn_off_camera_action.key_down(Keys.CONTROL).send_keys(
            "e").key_up(Keys.CONTROL).perform()

        # joining the meet
        join = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Join now')]"))
        )
        join.click()

        print("Joined")
        time.sleep(self.class_time)
        return self.leave_call()

    def leave_call(self):
        '''leaves the meet'''
        logger.warning("Leaving the call")

        self.driver.close()

        try:
            current_tab = self.driver.window_handles[0]
            self.driver.switch_to.window(self.driver.window_handles[0])
        except Exception as err:
            logging.error(f"Error occurred: {err}")

        print("Left")

        # goes back a page
        self.driver.back()


# to sign out
class Sign_Out:
    def __init__(self, driver: object, time_: int = 10):
        '''to sign out'''
        logger.warning("Signing out")

        driver.get(
            "https://accounts.google.com/SignOutOptions?hl=en&continue=https://mail.google.com/mail&service=mail")

        driver.find_element_by_xpath(
            '//button[normalize-space()="Sign out"]').click()

        time.sleep(time_)
        # closing the tab
        driver.quit()

        exit()


Main().log_into_gmail()
