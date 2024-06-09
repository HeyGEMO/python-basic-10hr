class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi,",self.name,"you marks is:",sum/3)

s1=student("oho boi",[99,88,77])
s1.get_avg()
s1.name="ba haa"
s1.get_avg()