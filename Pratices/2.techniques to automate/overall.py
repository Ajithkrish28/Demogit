''''

1. static drop down - is this HTML code in Select class, so, use Select class and create object and find the element

2. dynamic drop down - it's not like a static drop down. we give some input and show option, but these options are change after sometimes,
                        so, we save all option in one variable,( find_elements it' return a list, so we save in variable ).

3. print dynamic value - we use get_attribute("value"), we can't use text method, text method only for predefine text.

4. check box  - it's also change , so, we store all element in one variable and use loop and condition.

5. radio button  - we have unique locator so we directly access the element
                    or all element we save in one variable and give index value(EX: button[2] )  or use loop, condition and click.

6 . alert or popup - pop, it's not use in HTML code, so, we change to alert mode and create object ( alert = driver.switch_to.alert )
                    after switch we can access alert,
                    alert.text - access the text
                    alert.accept - it's ok button,  and alert.dismiss - cancel


is_checked() , is_displayed() these are used to check

 assert  - it's use for validation

'''