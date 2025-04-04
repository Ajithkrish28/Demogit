'''
By is used to access, what we give command or code.


Locator is used to find the element and access and there are:

NAME
    By.NAME, "what they define that content"

ID
  By.ID, "what they define that content"

Class Name
    By.CLASS_NAME, "class defined"  -- we give one class name( some time have many class name so we give one class value)

Link text
    it's a used to webpage in any link that one access.first  we find and confirm is this link. in HTML is link is defined strat with <a
    By.LINK_TEXT, "link in behind text"

XPATH
    we put on path
    //tag name[@attribute = 'attribute value']  -we use ' ' in square bracket
    (//tag name[@attribute = 'attribute value'])[2]   - 2 is find element

    is this used for no unique attribute value ot no locator, that we use.(some ways is there)

    find the element parent to child
    //page(parent) tag/child tag/ child tag      EX: //form/div/input
    //page(parent) tag/child tag[no of element]/ child tag      EX: //form/div[2]/input - some to we used number because of find the element

    Special feature if XPATH:(like text link)
        access the element in text basses
        //tag[text()='what text in element']  EX : //button[text()='save password']

CSS Selector
    we put on path
    tag name[attribute='attribute value']   -we use ' ' in square bracket

    this on also used for no unique attribute value ot no locator, that we use.(some ways is there)

    find the element parent to child
    pagetag(parent) childtag childtag       EX: form div input
    pagetag(parent) childtag:nth(no of element) childtag       EX: form div:nth(2) input  - found the element,we used number

    Special feature:
        access to ID:
            #ID value  (not give attribute)

        access to Class name:
            .class value    (not give attribute)


Regular Expression:

XPATH:
    //tag[contains(@attribute, 'attribute value')]

CSS_SELECTOR:
    tag[attribute*='attribute value'] - a[class*='btn-primary']

'''
'''
testing practices pages:

https://rahulshettyacademy.com/angularpractice/shop

https://rahulshettyacademy.com/client/auth/login

https://rahulshettyacademy.com/angularpractice/

https://rahulshettyacademy.com/dropdownsPractise/

https://rahulshettyacademy.com/AutomationPractice/

https://rahulshettyacademy.com/seleniumPractise/#/

https://the-internet.herokuapp.com/windows


'''