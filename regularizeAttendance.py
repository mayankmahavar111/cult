import time
from selenium import webdriver




def clickElement(path,driver):
    element =  driver.find_element_by_xpath(path)
    if type(element) is list:
        element = element[-1]
    element.click()

def login(driver):
    driver.get('http://cure.fit/')
    time.sleep(5)

    clickElement('//*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/div',driver)
    time.sleep(5) 

    clickElement('//*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div/ul[2]/li/div/div/div',driver)
    time.sleep(5) 

    clickElement('//*[@id="phoneloginModal"]/div/div/div/div/div[2]/div[4]/div/div/img[1]',driver)
    time.sleep(5)

    clickElement('//*[@id="loginModal"]/div/div/div/div/div[2]/div/div[3]/button',driver)
    time.sleep(15)

    search_box = driver.find_element_by_xpath('//*[@id="loginModal"]/div/div/div/div/form/input[1]')
    search_box.send_keys('mayankmahavarofficial@gmail.com')

    search_box = driver.find_element_by_xpath('//*[@id="loginModal"]/div/div/div/div/form/input[2]')
    search_box.send_keys('Alwar@1234')

    clickElement('//*[@id="loginModal"]/div/div/div/div/form/div/input',driver)
    time.sleep(5)

def chooseCenter(driver):
    # clickElement('//*[@id="root"]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/div',driver)
    # time.sleep(5) 


    driver.get('https://www.cure.fit/cult/gym')
    time.sleep(5) 

    search_box = driver.find_elements_by_class_name('location-container')[-1]
    # print(search_box)
    search_box.click()
    time.sleep(5) 

    search_box = driver.find_element_by_xpath('//*[@id="centre-selection-modal"]/div/div/div[2]/div[1]/input')
    search_box.send_keys('tfd')
    time.sleep(5)

    search_box = driver.find_elements_by_class_name('location')[0]
    # print(search_box)
    search_box.click()
    time.sleep(5) 

def bookClassButton(driver):
    search_box = driver.find_elements_by_class_name('book-button')[-1]
    # print(search_box)
    search_box.click()
    time.sleep(5) 

def chooseFilter(driver,filterName):
    search_box = driver.find_elements_by_class_name('filter-dropdown')[-1]
    # print(search_box)
    search_box.click()
    time.sleep(5)

    search_box = driver.find_elements_by_class_name('workout-option-li')
    for x in search_box:
        if x.text == filterName:
            x.click()
            print(x.text)
            break
    time.sleep(5)

def getElementsList(driver,className):
    search_box =  driver.find_elements_by_class_name(className)
    temp= []
    for x in search_box:
        temp.append(x)
    return temp


if __name__ == "__main__":
    driver = webdriver.Chrome('D:\\projects\\cult\\chromedriver') 
    login(driver)
    chooseCenter(driver)
    bookClassButton(driver)
    # chooseFilter(driver,'CrossFit')
    dates = getElementsList(driver,'text-container')
    
    filterApplied = False

    for date in dates:
        date.click()
        time.sleep(2)
        if filterApplied == False:
            chooseFilter(driver,'HRX Workout')
            filterApplied =  True
        time.sleep(2)
        bookingCells =  getElementsList(driver,'booking-time-row-cell')

        for cell  in bookingCells:

            if cell.find_elements_by_class_name('time-text')[-1].text == "08:00 AM":

                tempElement= cell.find_elements_by_class_name('class-cell')[-1]
                classes =  tempElement.get_attribute('class')

                if 'available-theme' in classes and 'unavailable-theme' not in classes:
                    try :
                        tempElement.click()
                        time.sleep(2)
                        popupElements = getElementsList(driver,'action-button')
                        if popupElements[-1].text == "Proceed":
                            popupElements[-1].click()
                            time.sleep(2)
                            print("Inside proceed complete")
                            confirmPopUp =  getElementsList(driver,'done-button')
                            print("Inside confirm pop up ")
                            confirmPopUp[-1].click()
                            time.sleep(2)
                            chooseCenter(driver)
                            bookClassButton(driver)
                        else:
                            popupElements[-1].click()
                    except Exception as e :
                        print(e)
                        time.sleep(2)
                        chooseCenter(driver)
                        bookClassButton(driver)
                break




    driver.quit()



