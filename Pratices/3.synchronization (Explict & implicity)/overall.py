'''
1 . driver.find_elements - selenium return list of all element and store in some variable and use loop and condition for click

2. chain element - store all element in variable( locator ),again locator continue from variable
    EX : //input[@type='search'] this locator store in variable and div/button this locator continue from variable it,s using a for loop

3. implicitly wait - it's helps to wait some second(5) all element waiting for get element it's use globally(whole element)
    implicitly wait except from find_elements, because it's return a list of elements
    ( implicitly wait for single element )
    list of element are we used to time.sleep ( some time take time for load )

4. explicitly wait - it's use for some particularly target element, because some time take time for loaded, that we use
                    create object for WebDriverWait(driver,10) class, and we give global driver and what time wait that second
                    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))  ,
                    wait = object
                    expected_conditions - it is a package we need importfrom selenium
                    presence_of_element_located - what type locator is there (like : element or virtual)

'''