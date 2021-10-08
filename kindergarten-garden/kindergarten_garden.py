class Garden:
    plant_names = ['Clover','Grass', 'Radishes', 'Violets']
    def __init__(self, plants, students='Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry'.split()):
        self.plant_rows = plants.split('\n')
        self.students = sorted(students)
    def plants(self, student_name):
        student_index = self.students.index(student_name)
        student_plants = slice(student_index*2, (student_index+1)*2)
        plant_letter_to_name = {name[0]: name for name in self.plant_names}
        return [plant_letter_to_name[p] for plant_row in self.plant_rows for p in plant_row[student_plants]]
