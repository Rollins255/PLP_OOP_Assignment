class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print("The persons details are:")
        print("Name:" ,self.name)
        print("Age: " ,self.age)
        print("Gender: " ,self.age)
        #instanciating the person class
employee1 = person("John", 28, "male")
employee2 = person("Ann", 32, "female")
#function call
employee1.introduce()
employee2.introduce()