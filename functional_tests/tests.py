from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)
        
    def tearDown(self):
        self.browser.quit()
        
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('sign_in_form')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [rw.text for rw in rows])        
        
    def test_can_start_course_and_retrieve_it_later(self):
            
#Kamau has heard about a cool way of learning entrepreneurship.
#He decides to check out the homepage of this site.
        self.browser.get(self.live_server_url)

#He notices the page title and it says learn interactively.
        self.assertIn('Learn Interactively', self.browser.title)      
        

#In the body  he sees a banner that says rise
        carousel = self.browser.find_element_by_id('carousel').text
        self.assertIn('rise', carousel)
#There is a field set that invites him to log in so that he can 
#save his progress.
#The login offers logging in with facebook, twitter
#and google+ or using form to create an account
#which asks him for username, email, phone number 
#and password.
        inputbox = self.browser.find_element_by_id('id_user_name')
        self.assertEqual(
                        inputbox.get_attribute('placeholder'),
                        'Enter your name'
                        )
#He types his username, ##email, phone number and password will
##be tested later.
        inputbox.send_keys('Kamau')
        
         
#When he hits enter, he is taken to a new url,
#the page updates, and now the page says 
#welcome Kamau.
        inputbox.send_keys(Keys.ENTER)
        kamau_list_url = self.browser.current_url
        self.assertRegex(kamau_list_url, '/sections/.+')        
        self.check_for_row_in_list_table('Kamau')
        
        inputbox = self.browser.find_element_by_id('id_user_name')
        inputbox.send_keys('second item ya kamau')
        inputbox.send_keys(Keys.ENTER)
        kamau_list_url = self.browser.current_url
        self.assertRegex(kamau_list_url, '/sections/.+')
        self.check_for_row_in_list_table('Kamau')
        self.check_for_row_in_list_table('second item ya kamau')
        
        
        #self.check_for_row_in_list_table('Kamau')
        
#He also notices that the page has courses with a short text
#description listed on the page.The courses spread all the
#way to the footer of the page.
        header_text = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Courses', header_text)
        
        #course_list = self.browser.find_elements_by_tag_name('h2').text
        #self.assertIn('Industries Performance', course_list)

#He clicks on one of the titles and it refreshes with a new Page
#that has a start button and sections listing below it.
#He clicks ons start and is immediately taken to an
#interactive learning console. On the left is the section body 
#text. On the right he there is a question listed 
#multiple choice answers.
#Below the multiple choice answers he sees two buttons. One says
#submit while the other says reset.
#At the top he also sees two links. One link says Discuss while the 
#other says full chapter glossary.


#He reads the section hurriedly, reads the QUESTION
#and selects an answer and clicks on submit.

#The page flashes a green message that says well done and loads the 
#next question. He answers the question and hits submit again.
#After the fifth question. The page displays a 
#badge of completion and loads a new section to start
#the process again.
        #self.fail('Finish test')
        
#Now a new user, Francis, comes along to the site

##We use a new browxer session to make sure that no information of Kamau is coming 
##though from sessions, cookies etc

        self.browser.quit()
        self.browser = webdriver.Firefox()

#Francis visits the home page. There is no sign  of Kamau's list.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Kamau', page_text)
        self.assertNotIn('second item ya', page_text)
        
#Francis starts a new list by entering a new item.
        inputbox = self.browser.find_element_by_id('id_user_name')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        
#Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/sections/.+')
        self.assertNotEqual(francis_list_url, kamau_list_url)
        
#Again, there is no trace of Kamau's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Kamau', page_text)
        self.assertIn('Buy milk', page_text)                


#Satisfied, they both feel tired and go to sleep.
