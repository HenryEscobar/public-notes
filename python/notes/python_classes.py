
# bad sources: https://www.youtube.com/watch?v=apACNr7DC_s - silly video
# filename should match class name
# https://docs.python.org/3/tutorial/classes.html
# https://www.tutorialsteacher.com/python/property-decorator 

import datetime


class User: # capitalize name of class
    """ doc string shown when do help(Users)"""
    def __init__(self,fullname,birthday):   # constructor
        self.name = fullname
        self.birthday = birthday  # yyyymmdd
        name_split = fullname.split(" ")
        self.first_name = name_split[0]
        self.lastname = name_split[-1]


    def age(self):
        """ show age of user in years"""
        today = datetime.date.today()
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        date_of_birth = datetime.date(yyyy,mm,dd) 
        age_in_days = ( today - date_of_birth).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

# Class decorators:
#  @property: declears a method as a property
#       @<property-name>.setter -> Specifiy setter method
#       @<property-name>.deleter: spec method to delete property

# need to dig into this more
class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name=value
    
    @name.deleter   #property-name.deleter decorator
    def name(self, value):
        print('Deleting..')
        del self.__name



if __name__ == '__main__':
    henry=User("Henry J. Escobar", "19741222")
    print(henry.age())

    print("-" * 80)
    print("playing with class decorators")
    s=Student('Henry')
    print(s.name)
    s.name('fred')
    print(s.name)
    del s.name     # del is a keyword that can be evoked w/ that deleter if set
