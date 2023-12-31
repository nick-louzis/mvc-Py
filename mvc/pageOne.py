import tkinter as tk
# from tkinter import ttk 
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview


class PageOne(tk.Frame):
    def __init__(self,parent, controller):
        self.deaprtments= [
            "Civil Engineering",
            "Architecture",
            "Planning and Regional Development",
            "Mechanical Engineering",
            "Electrical and Computer Engineering",
            "Economics",            
            "Business Administration"
        ]
        tk.Frame.__init__(self,parent)

        self.entrys_holder = tk.Frame(self)
        self.entrys_holder.pack(side='top',fill='both', expand=True)

        self.controller= controller
        label = tk.Label(self.entrys_holder, text="1")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self.entrys_holder, text="Επόμενη σελίδα",
                            command=lambda: self.controller.go_to_second_page() ) #acts as a onClick event
        button.pack(pady=10, padx=10)
        self.name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.serial_tag = tk.IntVar()
        self.university = tk.StringVar()
        
        self.students = self.controller.students
        self._make_all_entrys()

        

        def _get_student_(e):
            iid= self.students_list.view.selection()
            value = self.students_list.view.item(iid,'values')
            # print(value)
            self.load_entrys(value)
            self.get_university(value[3])
            self.uni_entry_menu.config(text=value[3])
            self.controller.get_entrys(self.name.get(), self.last_name.get(), self.serial_tag.get(), self.university.get())

        self.list_frame = tk.Frame(self)
        self.list_frame.pack(padx=10,pady=10,side='bottom')
        self.columns=['Name', 'Last Name', 'AM', 'Department']
        self.students_list = Tableview(self.list_frame, coldata=self.columns, rowdata = self.students, searchable=True, paginated=True)
        self.students_list.pack()
        


        self.students_list.view.bind('<<TreeviewSelect>>', _get_student_)
    
    
    def load_entrys(self,values):
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, values[0])
            self.last_name_entry.delete(0,tk.END)
            self.last_name_entry.insert(0,values[1])
            self.serial_tag_entry.delete(0, tk.END)
            self.serial_tag_entry.insert(0,values[2])
            self.uni_entry.setvar(values[3])
            
        
        

        
    def _make_all_entrys(self):
        self._make_name_entrys()
        self._make_lastname_entrys()
        self._make_serial_tag_entry()
        self._make_university_entrys()
        # self._makes_students_list(self.students)

    def _make_name_entrys(self):
        self.name_label = tk.Label(self.entrys_holder, text="Όνομα :")
        self.name_label.pack(pady=10, padx=10, side='left')

        self.name_entry = ttk.Entry(self.entrys_holder, textvariable=self.name) 
        self.name_entry.pack(pady=10, padx=10, side='left')

        self.name_button = ttk.Button(self.entrys_holder, text='print', command=lambda: self.controller.get_entrys(self.name.get(), self.last_name.get()))
        self.name_button.pack(pady=10, padx=10, side='left')

    def _make_lastname_entrys(self):
        self.last_name_label = tk.Label(self.entrys_holder, text="Επώνυμο :")
        self.last_name_label.pack(pady=10, padx=10, side='left')

        self.last_name_entry = ttk.Entry(self.entrys_holder, textvariable=self.last_name) 
        self.last_name_entry.pack(pady=10, padx=10, side='left')
    
    def _make_serial_tag_entry(self):
        self.serial_tag_label = tk.Label(self.entrys_holder, text= "Αριθμός Μητρώου :")
        self.serial_tag_label.pack(pady=10, padx=10, side='left')

        self.serial_tag_entry = ttk.Entry(self.entrys_holder, textvariable=self.serial_tag)
        self.serial_tag_entry.pack(pady=10, padx=10, side='left')
    
    def get_university(self,value):
        self.uni_entry.config(text=value)
        
        self.university = value
        self.uni_entry_menu
        
    

    def _make_university_entrys(self):
        self.uni_label = tk.Label(self.entrys_holder, text="Σχολή :")
        self.uni_label.pack(pady=10, padx=10, side='left')

        self.uni_entry = ttk.Menubutton(self.entrys_holder, text= "Επιλέξτε") 
        self.uni_entry.pack(pady=10, padx=10, side='left')

        self.uni_entry_menu= tk.Menu(self.uni_entry)

        self.uni_value= tk.StringVar()
        x=0
        for department in self.deaprtments:
            self.uni_entry_menu.insert_radiobutton(index=x, label=department, 
                                                variable=self.uni_value, 
                                                command= lambda value=department : self.get_university(value))
                                                 # with value = department we dont need to bind
            x+=1
        
        self.uni_entry['menu'] = self.uni_entry_menu
        print(self.uni_entry.state())
        

   

    
        

        
