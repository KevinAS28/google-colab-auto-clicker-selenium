class_names = {
    "ytb_ad_msg_container": ".ytp-ad-preview-container",
    "ytb_video_element": "html5-main-video",
    "ad_msg": ".ytp-ad-preview-text",
    "skip_ad_button": "//button[contains(@class, 'ytp-ad-skip-button ytp-button')]",
    "you_there_button": "//paper-button[contains(@class, 'style-scope yt-button-renderer style-blue-text') and @id='button' and @aria-label='Yes']",
    "title": "//yt-formatted-string[contains(@class, 'title style-scope ytmusic-player-bar')]",
    "like": "//paper-icon-button[contains(@class, 'like style-scope ytmusic-like-button-renderer') and @aria-label='Like']",
    "next": "//paper-icon-button[contains(@class, 'next-button style-scope ytmusic-player-bar')]"
    }

import os, time, math
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def next_vid(driver):
    def __next_vid():
        driver.find_element_by_xpath(class_names["next"]).click()
    __next_vid()
    
def set_seek_video(driver, seek=0):
    print(f"Video seek set to {seek}")
    driver.execute_script(f'document.getElementsByClassName("{class_names["ytb_video_element"]}")[0].currentTime = {seek};')    

def get_seek_video(driver ):
    return driver.execute_script(f'return document.getElementsByClassName("{class_names["ytb_video_element"]}")[0].currentTime;')    

def get_duration_video(driver ):
    return driver.execute_script(f'return document.getElementsByClassName("{class_names["ytb_video_element"]}")[0].duration;')    


def exp(driver: webdriver.Chrome):
    import traceback

    try:
        
        os.system("clear")

        while True:
            random_code_cell = driver.find_elements_by_class_name('cell')
            for cell in random_code_cell:
                try:
                    cell.click()
                except Exception as e:
                    print(f'{str(e)}: {str(cell)} cannot be clicked')
                # cell.send_keys(Keys.ENTER)
                try:
                    time.sleep(2)
                except KeyboardInterrupt:
                    input('Press anything to continue')

            # code_cell = driver.find_element_by_id('cell-4SB9ss3mGfNi')
            # code_cell.click()
            # code_cell.send_keys(Keys.ENTER)

        
        
        
    except:
        traceback.print_exc()
