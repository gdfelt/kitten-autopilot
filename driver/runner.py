# from page import game_page
import page
from selenium import webdriver
import time

def main():
    print('initalizing game...')

    driver = webdriver.Firefox(executable_path=r'./geckodriver')
    driver.implicitly_wait(20)

    driver.get('http://kittensgame.com/web/#')

    time.sleep(10)

    gamepage = page.game_page(driver)

    gamepage.click_gather_catnip()

    time.sleep(2)

    gamepage.click_gather_catnip()

    time.sleep(2)

    gamepage.click_gather_catnip()

    time.sleep(30)



if __name__ == '__main__':
    main()

