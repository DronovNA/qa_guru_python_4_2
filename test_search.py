import pyautogui as pyautogui
from selene.support.shared import browser
from selene import be, have


def test_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).type('weiourjw[c577wc13@!#').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу weiourjw[c577wc13@!# ничего не найдено.'))


def test_form(open_browser_form):
    pyautogui.click()
    pyautogui.scroll(-1000)
    browser.element('[id="firstName"]').should(be.blank).type('Test').press_enter()
    browser.element('[id="lastName"]').should(be.blank).type('Testovich')
    browser.element('[id="userEmail"]').should(be.blank).type('Test@example.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('89997589856')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-container"]').click()
    browser.element('[id="subjectsInput"]').type('I').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[id="uploadPicture"]').send_keys('C:\\Users\\DronovNA\\Desktop\\txt.txt')
    browser.element('[id="currentAddress"]').should(be.blank).type('Test test test')
    browser.element('[id="state"]').click()
    browser.element('//div[text()="NCR"]').click()
    browser.element('[id="city"]').click()
    browser.element('//div[text()="Delhi"]').click()
    browser.element('#submit').submit()
    browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
