from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_course_and_retrieve_it_later(self):
            
#Kamau has heard about a cool way of learning entrepreneurship.
#He decides to check out the homepage of this site.
        self.browser.get('http://localhost:8000')

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
         
#When he hits enter, the page updates, and now the page says 
#welcome Kamau.
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('sign_in_form')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                        any(row.text == 'Kamau' for row in rows),
                        "Kamau did not appear in table the text is\n%s"%(
                                                                         table.text,)
                        )        
#He also notices that the page has courses with a short text
#description listed on the page.The courses spread all the
#way to the footer of the page.
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Courses', header_text)

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
        self.fail('Finish test')

#Kamau feels tired and retires for the day.
if __name__=='__main__':
    unittest.main(warnings='ignore')