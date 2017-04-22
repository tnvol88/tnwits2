from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    intervention = input('Enter "1" for face-to-face and "4" for sap')
    while intervention not in ('1,4'):
        print('Invalid Entry: enter a "1" or "4".')
        intervention = input('Enter "1" for face-to-face and "4" for sap')
    if intervention == '1':
        intervention = 'Intervention #1'
    else:
        intervention = 'Intervention #4'
    return intervention


    
intervention_var = get_intervention()
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

username_field = driver.find_element_by_id('Identifier')
username_field.send_keys('')

password_field = driver.find_element_by_id('Password')
password_field.send_keys('')

pin_field = driver.find_element_by_id('Pin')
pin_field.send_keys('')

submit_button = driver.find_element_by_xpath("//button[@type='submit']")
submit_button.click()

agency_dropdown = driver.find_element_by_xpath("//div[@data-event-postback='Administration']")
agency_dropdown.click()

prevention_link = driver.find_element_by_xpath("//div[@data-event-postback='Prevention']")
prevention_link.click()

community_measure_link = driver.find_element_by_xpath("//div[@data-event-postback='CoalitionCommunityMeasure']")
community_measure_link.click()

date_field = driver.find_element_by_id('MeasureDate')
date_field.send_keys(date)

##go_button = driver.find_element_by_id('QueryButton')
##go_button.click()

driver.implicitly_wait(10)
WebDriverWait(driver, 20)

add_new_button = driver.find_element_by_xpath("//a[@id='NewCommunityMeasure']")
add_new_button.click()

contract_select = driver.find_element_by_id('s2id_ContractId')
contract_select.click()
contract_search = driver.find_element_by_id('s2id_autogen1_search')
contract_search.send_keys('2017 Frontier SBL-ARY')
contract_search.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

goal = driver.find_element_by_id('s2id_CoalitionGoalId')
goal.click()
goal_search = driver.find_element_by_id('s2id_autogen3_search')
goal_search.send_keys('A')
goal_search.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

###This will change based on type of intervention
intervening_variable = driver.find_element_by_id('s2id_CoalitionVariableId')
intervening_variable.click()
intervening_search = driver.find_element_by_id('s2id_autogen4_search')
intervening_search.send_keys(intervention_var)
intervening_search.send_keys(Keys.RETURN)

name_field = driver.find_element_by_id('Name')
name_field.send_keys('SHHS')

### This will change based on date
date_field = driver.find_element_by_id('MeasureDate')
date_field.send_keys(date)

### This will change based on duration
duration_field = driver.find_element_by_id('MeasureDuration')
duration_field.send_keys(duration)

duration_type = driver.find_element_by_id('s2id_MeasureDurationTypeCode')
duration_type.click()
duration_type_search = driver.find_element_by_id('s2id_autogen7_search')
duration_type_search.send_keys('Min')
duration_type_search.send_keys(Keys.RETURN)

location = driver.find_element_by_id('s2id_CdCommunityMeasureLocationId')
location.click()
location_search = driver.find_element_by_id('s2id_autogen2_search')
location_search.send_keys('Schools')
location_search.send_keys(Keys.RETURN)

evidence_based = driver.find_element_by_id('s2id_CdStrategyCriterionId')
evidence_based.click()
evidence_search = driver.find_element_by_id('s2id_autogen5_search')
evidence_search.send_keys('HIV - Cognitive')
evidence_search.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

intervention_type = driver.find_element_by_id('s2id_CdInterventionTypeId')
intervention_type.click()
intervention_search = driver.find_element_by_id('s2id_autogen6_search')
intervention_search.send_keys('Indicated')
intervention_search.send_keys(Keys.RETURN)

other_time = driver.find_element_by_id('AdditionalDuration')
other_time.send_keys('0')

other_duration = driver.find_element_by_id('s2id_AdditionalDurationTypeCode')
other_duration.click()
other_search = driver.find_element_by_id('s2id_autogen8_search')
other_search.send_keys('Min')
other_search.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

activity = driver.find_element_by_id('s2id_CdCsapActivityId')
activity.click()
activity_search = driver.find_element_by_id('s2id_autogen9_search')
activity_search.send_keys('st')
activity_search.send_keys(Keys.RETURN)

substance = driver.find_element_by_id('s2id_SubstanceCode')
substance.click()
substance_search = driver.find_element_by_id('s2id_autogen10_search')
substance_search.send_keys('s')
substance_search.send_keys(Keys.RETURN)

risk_categories = driver.find_element_by_id('RiskCategories_FullListBox')
actions= ActionChains(driver)
##actions.key_down(Keys.CONTROL)
risk_categories.click()
##risk_categories.send_keys(Keys.UP)
##risk_categories.send_keys(Keys.UP)
##risk_categories.click()
##actions.key_up(Keys.CONTROL)
##actions.perform()
subs = driver.find_element_by_xpath("//select[@name='RiskCategories_FullListBox']//option[@value='9']")
econ_disadvantaged = driver.find_element_by_xpath("//select[@name='RiskCategories_FullListBox']//option[@value='6']")
seekingbx = driver.find_element_by_xpath("//option[@value='1025']")
lack_enforcement = driver.find_element_by_xpath("//select[@name='RiskCategories_FullListBox']//option[@value='16']")
violent = driver.find_element_by_xpath("//select[@name='RiskCategories_FullListBox']//option[@value='4']")
actions.key_down(Keys.CONTROL)
actions.click(subs)
actions.click(seekingbx)
actions.click(lack_enforcement)
actions.click(violent)
actions.key_up(Keys.CONTROL)
actions.perform()

add_to_column = driver.find_element_by_id('AddRiskCategory')
add_to_column.click()

driver.implicitly_wait(10)
WebDriverWait(driver, 20)

loop_count = 0
while True:
    if loop_count < 10:
        try:
            travel_cost = driver.find_element_by_id('ApproximateTravelAmount')
            travel_cost.send_keys('0')
            break
        except:
            loop_count += 1
            pass
    else:
        print('Stale Element Error: Timed Out')
        break

travel_earned = driver.find_element_by_id('EarnedTravelAmount')
travel_earned.send_keys('0')

travel_other = driver.find_element_by_id('OtherTravelAmount')
travel_other.send_keys('0')

material_cost = driver.find_element_by_id('ApproximateMaterialAmount')
material_cost.send_keys('0')

material_earned = driver.find_element_by_id('EarnedMaterialAmount')
material_earned.send_keys('0')

material_other = driver.find_element_by_id('OtherMaterialAmount')
material_other.send_keys('0')

space_cost = driver.find_element_by_id('ApproximateSpaceAmount')
space_cost.send_keys('0')

space_earned = driver.find_element_by_id('EarnedSpaceAmount')
space_earned.send_keys('0')

space_other = driver.find_element_by_id('OtherSpaceAmount')
space_other.send_keys('0')

media_cost = driver.find_element_by_id('ApproximateMediaAmount')
media_cost.send_keys('0')

media_earned = driver.find_element_by_id('EarnedMediaAmount')
media_earned.send_keys('0')

media_other = driver.find_element_by_id('OtherMediaAmount')
media_other.send_keys('0')

labor_cost = driver.find_element_by_id('ApproximateLaborAmount')
labor_cost.send_keys('0')

labor_earned = driver.find_element_by_id('EarnedLaborAmount')
labor_earned.send_keys('0')

labor_other = driver.find_element_by_id('OtherLaborAmount')
labor_other.send_keys('0')

next_page_button = driver.find_element_by_id('Next')
next_page_button.click()

### This should take variable each time
total_participants = driver.find_element_by_id('PreventionDemographics_TotalParticipantCount')
total_participants.send_keys(Keys.DELETE)
total_participants.send_keys(total_participant_amount)
total_participants.send_keys(Keys.RETURN)

driver.implicitly_wait(10)
WebDriverWait(driver,20)

### Should take a variable each time
male_total = driver.find_element_by_id('PreventionDemographics_MaleParticipantCount')
male_total.send_keys(Keys.DELETE)
male_total.send_keys(total_male_amount)

### Should take variable each time
female_total = driver.find_element_by_id('PreventionDemographics_FemaleParticipantCount')
female_total.send_keys(total_female_amount)

### Should take a variable
twelve_fourteen = driver.find_element_by_id('PreventionDemographics_Age12To14ParticipantCount')
twelve_fourteen.send_keys(fourteen)

### Should take variable
fifteen_seventeen = driver.find_element_by_id('PreventionDemographics_Age15To17ParticipantCount')
fifteen_seventeen.send_keys(fifteen)

### Should take variable
eighteen_twenty = driver.find_element_by_id('PreventionDemographics_Age18To20ParticipantCount')
eighteen_twenty.send_keys(eighteen)

### Should take variable
twentyfive_fortyfour = driver.find_element_by_id('PreventionDemographics_Age25To44ParticipantCount')
twentyfive_fortyfour.send_keys(twentyfour)

### should take variable
fortyfive_sixtyfour = driver.find_element_by_id('PreventionDemographics_Age45To64ParticipantCount')
fortyfive_sixtyfour.send_keys(older)

### should take variable
hispanic = driver.find_element_by_id('PreventionDemographics_HispanicLatinoParticipantCount')
hispanic.send_keys(hispanic_amount)

### should take variable
not_hispanic = driver.find_element_by_id('PreventionDemographics_NotHispanicLatinoParticipantCount')
not_hispanic.send_keys(not_hispanic_amount)

### should take variable
white = driver.find_element_by_id('PreventionDemographics_WhiteParticipantCount')
white.send_keys(white_amount)

### variable
asian = driver.find_element_by_id('PreventionDemographics_AsianParticipantCount')
asian.send_keys(asian_amount)

### variable
black = driver.find_element_by_id('PreventionDemographics_BlackParticipantCount')
black.send_keys(black_amount)

third_page = driver.find_element_by_id('Next')
third_page.click()

lead_staff = driver.find_element_by_id('s2id_LeadStaffMemberKey')
lead_staff.click()
lead_staff_search = driver.find_element_by_id('s2id_autogen1_search')
lead_staff_search.send_keys('be')
lead_staff_search.send_keys(Keys.RETURN)

### variable
youth = driver.find_element_by_id('YouthParticipantCount')
if intervention_var == 'Intervention #1':
    youth.send_keys('0')
else:
    youth.send_keys(total_participant_amount)

### variable
law_enforcement = driver.find_element_by_id('LawEnforcementParticipantCount')
law_enforcement.send_keys('1')

### variable
parents = driver.find_element_by_id('ParentParticipantCount')
parents.send_keys('1')

### variable
fraternal = driver.find_element_by_id('ReligiousParticipantCount')
fraternal.send_keys('0')

###variable
business = driver.find_element_by_id('BusinessParticipantCount')
business.send_keys('0')

### variable
civic = driver.find_element_by_id('VolunteerGroupParticipantCount')
civic.send_keys('0')

### variable
media = driver.find_element_by_id('MediaParticipantCount')
media.send_keys('0')

### variable
health = driver.find_element_by_id('HealthProfessionalParticipantCount')
health.send_keys('1')

school = driver.find_element_by_id('SchoolParticipantCount')
school.send_keys('1')

tribal = driver.find_element_by_id('GovernmentParticipantCount')
tribal.send_keys('0')

### variable
youth_organization = driver.find_element_by_id('YouthOrganizationParticipantCount')
youth_organization.send_keys('0')

other = driver.find_element_by_id('OtherParticipantCount')
other.send_keys('0')

funding_source = driver.find_element_by_id('s2id_CdCommunityMeasureFundingSourceId')
funding_source.click()
funding_source_search = driver.find_element_by_id('s2id_autogen2_search')
funding_source_search.send_keys('b')
funding_source_search.send_keys(Keys.RETURN)

### variable
note = driver.find_element_by_id('Note')
note.click()
note.send_keys(note_text)

##finish = driver.find_element_by_id('ct102')
##finish.click()










