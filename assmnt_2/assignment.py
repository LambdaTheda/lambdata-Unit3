# athlete.py 

class Athlete():
    def __init__(self, is_person, has_gear, health_status, skill_level): # Init is a CONSTRUCTOR; Def __init__() helps initialize a class
        self.person = is_person  # self keyword helps instantiate? here? 
        self.has_gear = has_gear
        self.health_status = health_status
        self.skill_level = skill_level
    
    def eats_well(self): # parameter     
        print("Eats vegan organic food")

    def sleeps_plenty(self):
        print(f'Sleeps {num} hours')

class Rock_Climber(Athlete):
   def __init__(self, elf, is_person, has_gear, health_status, skill_level):
       super().__init__(is_person, has_gear, health_status, skill_level) # super keyword means? these are the attributes this child class inherits from parent ?
       self.elf = elf
    
   def climb(self):
       print(f'Eats vegan organic and climbs {num} hours weekly')

# WILL RUN BELOW IN COMMAND LINE:

if __name__ == "__main__":
    num = print("Please input a number: ")
    
    fit_human = Athlete("Maybe", "Yes", "Above average, 4/5", "Experienced, 5 Years") 
    
    print(fit_human.is_person, fit_human.has_gear)
    
    fit_human.eats_well()
    fit_human.sleeps_plenty()

    climber = Rock_Climber("No, DEFINITELY NOT!", "More than Enough!", "Mental Questionable 3/5", "Superior Skills, 18 Years")
    climber.eats_well()
    climber.sleeps_plenty()
