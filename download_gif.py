import time
import urllib

import os

import shutil

import pyautogui
from selenium import webdriver
import autoit
import cv2


def download_gif(delay=0.5):
    start_time = time.time()

    driver = webdriver.Chrome('./chrome_driver/chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(10000)
    driver.get('http://depthy.me/#/')
    print(driver.title)
    # time.sleep(8)
    # driver.quit()
    #####################

    driver.find_element_by_css_selector('div.button-open.btn.btn-lg.btn-success.center-block').click()
    # driver.find_element_by_css_selector('div.button-open.btn.btn-lg.btn-success.center-block').send_keys('G:/GP/DeeperDepth/left_scene.jpg')
    print("OPen Photo is found")
    time.sleep(delay)
    # autoit.run('autopopup.exe')
    # subprocess.call(['./autopopup.exe'])
    # os.system('"autopopup.exe"')
    '''
    autoit.win_wait_active("[CLASS:#32770]", 3)
    autoit.control_focus("[Class:#32770]", "Edit1")
    autoit.control_set_text("[Class:#32770]", "Edit1", "G:\GP\DeeperDepth\left_scene.jpg")
    autoit.control_click("[Class:#32770]", "Button1")
    '''
    pyautogui.click(206, 654)
    pyautogui.typewrite('G:\GP\DeeperDepth\left_scene.jpg')
    pyautogui.click(1181, 698)

    time.sleep(delay)

    driver.find_element_by_xpath('//*[@id="viewer"]/div[1]/div/div[2]/div/div[1]').click()
    print("Upload depth map is found")
    time.sleep(delay)

    driver.find_element_by_xpath('/html/body/div[4]/div/div/span/div[2]/div[2]/button').click()
    print("Open depth map is found")
    # autoit.run('autopopup2.exe')
    autoit.win_wait_active("[CLASS:#32770]", 3)
    autoit.control_focus("[Class:#32770]", "Edit1")
    autoit.control_set_text("[Class:#32770]", "Edit1", "G:\GP\DeeperDepth\depth_scaled_mr.png")
    autoit.control_click("[Class:#32770]", "Button1")
    time.sleep(delay)

    element = driver.find_element_by_xpath('//*[@id="viewer"]/div[3]/div/button[1]')
    driver.execute_script("arguments[0].click();", element)
    print('Share is found')
    time.sleep(delay)
    # click create GIF
    element = driver.find_element_by_xpath('//*[@id="popup"]/div[2]/div[1]/div[2]/div[1]')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(delay)
    # click do it
    element = driver.find_element_by_xpath('//*[@id="popup"]/div[2]/div[3]/div/div[1]')
    driver.execute_script("arguments[0].click();", element)
    #
    # time.sleep(30)
    print("loading is finished")

    visible = False
    i = 1
    while not visible:
        time.sleep(1)
        print(i)
        i += 1
        try:
            element = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/a/img')
            if element.is_displayed():
                visible = True
                src = element.get_attribute('src')
                print(src)
                element.click()
                while not os.path.exists('C:/Users/pc/Downloads/left_scene.gif'):
                    time.sleep(1)
                shutil.move("C:/Users/pc/Downloads/left_scene.gif", "./scene.gif")
        except:
            print("Error : ")
    print("--- %s seconds ---" % (time.time() - start_time))


def get_list(path, ext):
    list = []
    for root, dirs, files in os.walk(path):
        if files:
            for name in files:
                if name.endswith(ext):
                    list.append(os.path.join(root, name))
    return list


def resize_img_depth_pairs(pairs_path='C:\\Users\\pc\\Desktop\\Sharpened Depth - Samples'):
    images_list = get_list(pairs_path, 'jpg')
    depth_list = get_list(pairs_path, 'png')
    image_depth_pairs = list(zip(images_list, depth_list))

    for img, depth in image_depth_pairs:
        L = cv2.imread(img)
        L = cv2.cvtColor(L, cv2.COLOR_BGR2RGB)
        H, W, _ = L.shape
        Z = cv2.imread(depth, 0)
        Z = cv2.resize(Z, (W, H))
        cv2.imwrite(depth, Z)


def download_gif_from_pair(driver, pair_paths, delay=0.5):
    driver.get('http://depthy.me/#/')
    print(driver.title)
    # time.sleep(8)
    # driver.quit()
    #####################

    driver.find_element_by_css_selector('div.button-open.btn.btn-lg.btn-success.center-block').click()
    # driver.find_element_by_css_selector('div.button-open.btn.btn-lg.btn-success.center-block').send_keys('G:/GP/DeeperDepth/left_scene.jpg')
    print("OPen Photo is found")
    time.sleep(delay)
    # autoit.run('autopopup.exe')
    # subprocess.call(['./autopopup.exe'])
    # os.system('"autopopup.exe"')
    autoit.win_wait_active("[CLASS:#32770]", 3)
    autoit.control_focus("[Class:#32770]", "Edit1")
    autoit.control_set_text("[Class:#32770]", "Edit1", pair_paths[0])
    autoit.control_click("[Class:#32770]", "Button1")
    time.sleep(delay)

    driver.find_element_by_xpath('//*[@id="viewer"]/div[1]/div/div[2]/div/div[1]').click()
    print("Upload depth map is found")
    time.sleep(delay)

    driver.find_element_by_xpath('/html/body/div[4]/div/div/span/div[2]/div[2]/button').click()
    print("Open depth map is found")
    # autoit.run('autopopup2.exe')
    autoit.win_wait_active("[CLASS:#32770]", 3)
    autoit.control_focus("[Class:#32770]", "Edit1")
    autoit.control_set_text("[Class:#32770]", "Edit1", pair_paths[1])
    autoit.control_click("[Class:#32770]", "Button1")
    time.sleep(delay)

    element = driver.find_element_by_xpath('//*[@id="viewer"]/div[3]/div/button[1]')
    driver.execute_script("arguments[0].click();", element)
    print('Share is found')
    time.sleep(delay)
    # click create GIF
    element = driver.find_element_by_xpath('//*[@id="popup"]/div[2]/div[1]/div[2]/div[1]')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(delay)

    # click customize
    # element = driver.find_element_by_xpath('//*[@id="popup"]/div[2]/div[2]/div[3]/div')
    # driver.execute_script("arguments[0].click();", element)
    # time.sleep(delay)
    # click Horizontal
    #
    # //*[@id="popup"]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]
    # driver.find_element_by_xpath('//*[@id="popup"]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]').click()
    # driver.execute_script("arguments[0].click();", element)
    # time.sleep(3)

    # click do it
    element = driver.find_element_by_xpath('//*[@id="popup"]/div[2]/div[3]/div/div[1]')
    driver.execute_script("arguments[0].click();", element)
    #
    # time.sleep(30)
    print("loading is finished")

    visible = False
    i = 1
    while not visible:
        time.sleep(1)
        print(i)
        i += 1
        try:
            element = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/a/img')
            if element.is_displayed():
                visible = True
                src = element.get_attribute('src')
                print(src)
                element.click()
                pair_dir_path, filename_w_ext = os.path.split(pair_paths[0])
                filename, _ = os.path.splitext(filename_w_ext)
                gif_download_path = 'C:/Users/pc/Downloads/' + filename + '.gif'
                gif_mave_to_path = os.path.join(pair_dir_path, filename + '.gif')
                while not os.path.exists(gif_download_path):
                    time.sleep(1)
                shutil.move(gif_download_path, gif_mave_to_path)
        except:
            print("Error : ")


def download_all_pairs(driver, pairs_path='C:\\Users\\pc\\Desktop\\Sharpened Depth - Samples'):
    images_list = get_list(pairs_path, 'jpg')
    depth_list = get_list(pairs_path, 'png')
    image_depth_pairs = list(zip(images_list, depth_list))

    for pair in image_depth_pairs[0:1]:
        download_gif_from_pair(driver, pair)
        print("FINSHED PAIRS")
        time.sleep(1)

# resize_img_depth_pairs()
'''
driver = webdriver.Chrome('./chrome_driver/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10000)
start_time = time.time()
download_all_pairs(driver)
print("--- %s seconds ---" % (time.time() - start_time))
'''
download_gif()