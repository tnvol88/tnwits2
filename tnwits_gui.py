import tkinter as tk
from tkinter.ttk import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tnwits_functions

class app(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_text_boxes()

    def create_text_boxes(self):
        self.date_label=tk.Label(self, text='Date')
        self.date_label.grid(row=0,column=0)
        self.date_entry=tk.Entry(self, width=15)
        self.date_entry.grid(row=0,column=1)

        self.intervention_label=tk.Label(self, text='Intervention')
        self.intervention_label.grid(row=1,column=0)

        self.intervention_listbox = tk.Listbox(self, selectmode='multiple',
                                               width=20,height=4)
        interventions = ['Face-to-Face','Student Assistance','Group']
        num = 0
        for i in interventions:
            self.intervention_listbox.insert(num, i)
            num+=1
        self.intervention_listbox.grid(row=1,column=1)

        self.students_label=tk.Label(self, text='Students')
        self.students_label.grid(row=2, column=0)
        self.students_entry = tk.Entry(self, width=15)
        self.students_entry.grid(row=2,column=1)

        self.teachers_label = tk.Label(self, text='Teachers')
        self.teachers_label.grid(row = 4, column = 0)
        self.teachers_entry=tk.Entry(self, width=15)
        self.teachers_entry.grid(row=4, column=1)

        self.male_students_label = tk.Label(self, text = 'Male Students')
        self.male_students_label.grid(row = 6, column =0)
        self.male_students_entry = tk.Entry(self, width=15)
        self.male_students_entry.grid(row = 6, column =1)

        self.male_teachers_label = tk.Label(self, text = 'Male Teachers')
        self.male_teachers_label.grid(row = 8, column =0)
        self.male_teachers_entry = tk.Entry(self, width=15)
        self.male_teachers_entry.grid(row = 8, column =1)

        self.parents_label = tk.Label(self, text = 'Parents')
        self.parents_label.grid(row = 10, column =0)
        self.parents_entry = tk.Entry(self, width=15)
        self.parents_entry.grid(row = 10, column =1)

        self.fourteen_label = tk.Label(self, text = 'Fourteen')
        self.fourteen_label.grid(row = 12, column =0)
        self.fourteen_entry = tk.Entry(self, width=15)
        self.fourteen_entry.grid(row = 12, column =1)

        self.fifteen_label = tk.Label(self, text = 'Fifteen')
        self.fifteen_label.grid(row = 14, column =0)
        self.fifteen_entry = tk.Entry(self, width=15)
        self.fifteen_entry.grid(row = 14, column =1)

        self.eighteen_label = tk.Label(self, text = 'Eighteeen')
        self.eighteen_label.grid(row = 2, column =2)
        self.eighteen_entry = tk.Entry(self, width=15)
        self.eighteen_entry.grid(row = 2, column =3)

        self.twentyfour_label = tk.Label(self, text = 'Twentyfour')
        self.twentyfour_label.grid(row = 4, column =2)
        self.twentyfour_entry = tk.Entry(self, width=15)
        self.twentyfour_entry.grid(row = 4, column =3)

        self.older_label = tk.Label(self, text = 'Older')
        self.older_label.grid(row = 6, column =2)
        self.older_entry = tk.Entry(self, width=15)
        self.older_entry.grid(row = 6, column =3)

        self.black_students_label = tk.Label(self, text = 'Black Students')
        self.black_students_label.grid(row = 8, column =2)
        self.black_students_entry = tk.Entry(self, width=15)
        self.black_students_entry.grid(row = 8, column =3)

        self.black_teachers_label = tk.Label(self, text = 'Black Teachers')
        self.black_teachers_label.grid(row = 10, column =2)
        self.black_teachers_entry = tk.Entry(self, width=15)
        self.black_teachers_entry.grid(row = 10, column =3)

        self.hispanic_students_label = tk.Label(self, text = 'Hispanic Students')
        self.hispanic_students_label.grid(row = 12, column =2)
        self.hispanic_students_entry = tk.Entry(self, width=15)
        self.hispanic_students_entry.grid(row = 12, column =3)

        self.hispanic_teachers_label = tk.Label(self, text = 'Hispanic Teachers')
        self.hispanic_teachers_label.grid(row = 14, column =2)
        self.hispanic_teachers_entry = tk.Entry(self, width=15)
        self.hispanic_teachers_entry.grid(row = 14, column =3)

        self.asian_students_label = tk.Label(self, text = 'Asian Students')
        self.asian_students_label.grid(row = 16, column =2)
        self.asian_students_entry = tk.Entry(self, width=15)
        self.asian_students_entry.grid(row = 16, column =3)

        self.asian_teachers_label = tk.Label(self, text = 'Asian Teachers')
        self.asian_teachers_label.grid(row = 18, column =2)
        self.asian_teachers_entry = tk.Entry(self, width=15)
        self.asian_teachers_entry.grid(row = 18, column =3)

        self.students_note_label = tk.Label(self, text='Student Note')
        self.students_note_label.grid(row = 32, column=0)
        self.students_note_entry = tk.Text(self,height=10, width=25,wrap='word')
        self.students_note_entry.grid(row=32, column=1)

        self.teachers_note_label = tk.Label(self, text='Teachers Note')
        self.teachers_note_label.grid(row = 34, column=0)
        self.teachers_note_entry = tk.Text(self,height=10, width=25, wrap='word')
        self.teachers_note_entry.grid(row=34, column=1)

        self.submit_button = tk.Button(self, text='Submit', command = lambda: self.submit_form())
        self.submit_button.grid(row=32, column=4)

        self.quit = tk.Button(self, text='Quit',fg='red',
                              command= root.destroy)
        self.quit.grid(row=32,column=3)

    def get_values(self):
        values_dict = {}
        values_dict['date']=str(self.date_entry.get())
        values_dict['students']=str(self.students_entry.get())
        values_dict['teachers']=str(self.teachers_entry.get())
        values_dict['male students']=str(self.male_students_entry.get())
        values_dict['male teachers']=str(self.male_teachers_entry.get())
        values_dict['parents']=str(self.parents_entry.get())
        values_dict['fourteen']=str(self.fourteen_entry.get())
        values_dict['fifteen']=str(self.fifteen_entry.get())
        values_dict['eighteen']=str(self.eighteen_entry.get())
        values_dict['twentyfour']=str(self.twentyfour_entry.get())
        values_dict['older']=str(self.older_entry.get())
        values_dict['black students']=str(self.black_students_entry.get())
        values_dict['black teachers']=str(self.black_teachers_entry.get())
        values_dict['hispanic students']=str(self.hispanic_students_entry.get())
        values_dict['hispanic teachers']=str(self.hispanic_teachers_entry.get())
        values_dict['asian students']=str(self.asian_students_entry.get())
        values_dict['asian teachers']=str(self.asian_teachers_entry.get())
        values_dict['students note']=self.students_note_entry.get('1.0','end')
        values_dict['teachers note']=self.teachers_note_entry.get('1.0','end')
        return values_dict

    def submit_form(self):
        interventions = self.intervention_listbox.curselection()
        values = self.get_values()
        for i in interventions:
            driver = webdriver.Chrome()
            driver.get('https://tn.witsweb.org/Public/')

            enter_button = driver.find_element_by_id('Agree')
            enter_button.send_keys(Keys.RETURN)

            tnwits_functions.loginPage(driver)
            if i == 0:
                intervention='Intervention #4' #student assistance
                values['twentyfour']=0
                values['older']=0
                values['parents']=0
                values['female students']=int(values['students'])-int(values['male students'])
                duration = int(values['students'])*30
                tnwits_functions.pageOne(driver,values['date'],intervention, duration)
                tnwits_functions.pageTwo(driver,values['students'], values['male students'], values['female students'], values['fourteen'],
                        values['fifteen'], values['eighteen'], values['twentyfour'], values['older'], values['hispanic students'],
                        int(values['students'])-int(values['hispanic students']), int(values['students'])-int(values['black students']),
                        values['asian students'], values['black students'])
                tnwits_functions.pageThree(driver, values['students'],values['parents'],values['students note'],i)
            else:
                intervention = 'Intervention #1'
                values_copy = values.copy()
                values_copy['eighteen']=0
                values_copy['fourteen']=0
                values_copy['fifteen']=0
                values_copy['female teachers']=int(values_copy['teachers'])-int(values_copy['male teachers'])
                duration = int(values_copy['teachers'])*15
                tnwits_functions.pageOne(driver,values_copy['date'],intervention, duration)
                tnwits_functions.pageTwo(driver,values_copy['teachers'], values_copy['male teachers'], values_copy['female teachers'], values_copy['fourteen'],
                        values_copy['fifteen'], values_copy['eighteen'], values_copy['twentyfour'], values_copy['older'], values_copy['hispanic teachers'],
                        int(values_copy['teachers'])-int(values_copy['hispanic teachers']), int(values_copy['teachers'])-int(values_copy['black teachers']),
                        values_copy['asian teachers'], values_copy['black teachers'])
                tnwits_functions.pageThree(driver,values_copy['teachers'], values_copy['parents'], values_copy['teachers note'],i)
	
            next_entry = input('Click Finish on webpage and then press enter to continue:')
            driver.quit()

root=tk.Tk()
app = app(master=root)
app.mainloop()
