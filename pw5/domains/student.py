import math
import numpy as np

class Student:
    def __init__(self, s_id, name, dob):
        self.s_id = s_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def add_mark(self, course_id, mark):
        self.marks[course_id] = math.floor(mark * 10) / 10.0

    def calculate_gpa(self, courses_dict):
        if not self.marks:
            self.gpa = 0.0
            return
        
        marks_arr = []
        credits_arr = []
        
        for c_id, mark in self.marks.items():
            if c_id in courses_dict:
                marks_arr.append(mark)
                credits_arr.append(courses_dict[c_id].credits)
                
        if marks_arr:
            np_marks = np.array(marks_arr)
            np_credits = np.array(credits_arr)
            self.gpa = np.average(np_marks, weights=np_credits)