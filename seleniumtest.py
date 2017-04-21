from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tnwits_functions
import tnwits_gui

### FUNCTIONS TO BE USED WITHIN PROGRAM ####

def is_valid_word(text):
    for i in text:
        if i not in ('0,1,2,3,4,5,6,7,8,9'):
            print('Must enter numbers only')
            return False
        else:
            pass
    return True

def test(string):
    value = str(input(string))
    while not is_valid_word(value):
        print('Invalid Entry: must enter a number.')
        value = str(input(string))
    return str(value)

def get_intervention():
    intervention = list(input('Enter "1" for face-to-face and "4" for sap'))
##    truth = True
##    while truth:
##        for i in intervention:
##            if i not in ('1,3,4'):
##                print('Invalid Entry: enter a "1" or "4".')
##                intervention = list(input('Enter "1" for face-to-face and "4" for sap'))
##            else:
##                true = False
    return intervention

app = tnwits_gui.app
values = app.get_values()
print('values is: ', values)

date = '2/24/17'
print('running for date ', date)
               
total_students_amount = '18'
total_teachers_amount = '5'
duration = str(int(total_students_amount)*30)
               
total_male_amount = '7'
male_teachers = '1'
               
female_teachers = str(abs(int(total_teachers_amount)-int(male_teachers)))
total_female_amount =str(abs(int(total_students_amount)-int(total_male_amount)))
fourteen = '4'
               
fifteen = '11'
eighteen = '3'
twentyfour = '2'
older = '3'
               
hispanic_amount = '1'
hispanic_teachers = '0'
not_hispanic_amount = str(int(total_students_amount)-int(hispanic_amount))
               
black_amount = '1'
black_teachers_amount = '1'
asian_amount = '0'
asian_teachers_amount = '0'
white_amount = str(int(total_students_amount)-(int(black_amount)+int(asian_amount)))
               
parents = '0'

note_text = """Met with students for individual counseling sessions to address anger management, anxiety, depression, peer conflict, family relational problems,
academic concerns, suicidal ideation, and substance use. Discussed appropriate coping strategies and practiced these during sessions. Addressed suicidal ideation by
creating safety plans and communicated with support systems for these safety plans."""

administration_note_text = """Met with school staff and administration to discuss concerns related to student behaviors and emotional/mental health. Reviewed behavior patterns
and discussed intervention strategies. Reviewed previous interventions and disussed follow up with these students. Recieved new referrals and information regarding concerns
for these students. Discussed alternative school placement for students as well as strategies for students at risk of failing or being charged with truancy."""

intervention_list = get_intervention()

for i in intervention_list:
    if i == '1':
        intervention_var = 'Intervention #1'
    elif i == '3':
        intervention_var = 'Intervention #3'
    else:
        intervention_var = 'Intervention #4'


    if intervention_var == 'Intervention #1':
        duration = str(int(total_teachers_amount)*15)
        total_participant_amount = total_teachers_amount
        total_male_amount = male_teachers
        total_female_amount = str(abs(int(total_teachers_amount)-int(total_male_amount)))
        fourteen = '0'
        fifteen = '0'
        eighteen = '0'
        hispanic_amount = hispanic_teachers
        not_hispanic_amount = str(int(total_teachers_amount)-int(hispanic_teachers))
        black_amount = black_teachers_amount
        asian_amount = asian_teachers_amount
        white_amount = str(int(total_teachers_amount)-(int(black_amount)+int(asian_amount)))
        note_text = administration_note_text
    else:
        twentyfour = '0'
        older = '0'
        total_participant_amount = total_students_amount
        
        
    driver = webdriver.Chrome()

    driver.get('https://tn.witsweb.org/Public/')

    enter_button = driver.find_element_by_id('Agree')
    enter_button.send_keys(Keys.RETURN)

    tnwits_functions.loginPage(driver)
    tnwits_functions.pageOne(driver,date,intervention_var, duration)
    tnwits_functions.pageTwo(driver,total_participant_amount, total_male_amount, total_female_amount, fourteen, fifteen,
            eighteen, twentyfour, older, hispanic_amount, not_hispanic_amount, white_amount, asian_amount,
            black_amount)
    tnwits_functions.pageThree(driver,total_participant_amount, parents, note_text,intervention_var)
    
    next_entry = input('Click Finish on webpage and then press enter to continue:')
    driver.quit()
