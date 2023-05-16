class Pilot:
    def __init__(self, f_name, l_name, age, country,team):
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
        self.country=country
        self.team=team
    
    def printPilot(self):
        print("First Name: ", self.f_name)
        print("Last Name: ", self.l_name)
        print("Age: ", self.age)
        print("Country: ", self.country)
        print("Team: ", self.team)


        