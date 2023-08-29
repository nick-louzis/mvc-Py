
import sqlite3

class Model:
    def __init__(self):
        # self.controller= controller
        self.studets = [
            ('Nikos', 'Louzis', 4465 , 'Architecture'),
            ('Giannis', 'Keramas', 4534, 'Economics')
        ]

        self.lectures = [
            ('C #', 2, 3423 , 'Architecture'),
            ('Java', 3, 1134, 'Economics')
        ]

        self.conn = sqlite3.connect("Students.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY , name TEXT, lastname TEXT, serial INTEGER, university TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS lectures (id INTEGER PRIMARY KEY , lecture_ame TEXT, semester INTEGER, lecture_id INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS grades (id INTEGER PRIMARY KEY , lecture_id TEXT, student_id, grade INTEGER )")
        

    def insert_student(self, *students_data):
        student_rows =  self.cur.execute("SELECT * FROM students WHERE serial=?",(students_data[4]))

        print(student_rows)
        # self.cur.execute("INSERT INTO students VALUES(NULL,?,?,?,?)", (students_data[0], students_data[1], students_data[2],students_data[3]))
        # self.cur.execute("SELECT * FROM students")
        # row = self.cur.fetchall()
        # self.conn.commit()
        # print(row)
        
    def show_all_students(self):
        res = self.cur.execute("SELECT * FROM students")
        self.conn.commit(res)
        return res
        
    def show_all_lectures(self):
        res = self.cur.execute("SELECT * FROM lectures")
        self.conn.commit(res)
        return res
    
    def show_all_grades(self):
        res = self.cur.execute("SELECT * FROM grades")
        self.conn.commit(res)
        return res

    def update_student(self,*students_data):
        # self.cur.execute("UPDATE students SET VALUES(NULL,?,?,?,?)",(students_data[0], students_data[1], students_data[2],students_data[3]))
        # self.conn.commit()
        student_rows =  self.cur.execute("SELECT * FROM students WHERE serial=?",(students_data[4],))
        self.conn.commit()
        print(student_rows)

        print(students_data)

    def delete_student(self,*students_data):
        self.conn.execute("DELETE * FROM students WHERE serrial=?",(students_data[2],))
        self.conn.commit()
        pass
    
    # def insert_student(self):
    #     print('Inserting student')

