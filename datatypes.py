class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
s1=student("prathi",90)
s2=student("koushi",98)
s1.display()