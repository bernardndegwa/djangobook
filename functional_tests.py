from selenium import webdriver
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

#He notices the page title and it says learn.
        self.assertIn('Learn Interactively', self.browser.title)
        self.fail('Finish test!')

#In the body  he sees a banner that says rise.
#There is a field set that invites him to log in so that he can 
#save his progress.
#The login offers logging in with facebook, twitter
#and google+ or using form to create an account
#which asks him for username, email, phone number 
#and password.
#He also notices that the page has courses with a short text 
#description listed on the page.The courses spread all the
#way to the footer of the page.


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

#Kamau feels tired and retires for the day.
if __name__=='__main__':
    unittest.main(warnings='ignore')