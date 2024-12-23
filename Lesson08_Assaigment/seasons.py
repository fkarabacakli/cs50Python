import datetime
from sys import exit
from re import search
from operator import sub
import inflect

class Seasons:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        p = inflect.engine()
        birthday = datetime.date(self.year,self.month,self.day)
        today = datetime.date.today()
        result = sub(today,birthday)
        result = int(datetime.timedelta.total_seconds(result) /60)
        words = p.number_to_words((result))
        return words
        
        
    @classmethod
    def get(cls):
        birthday = input("Date of Birth: ").strip()
        result = search(r"^([12][0-9][0-9][0-9])-([0-9]|[0][0-9]|[1][012])-([0][0-9]|[0-9]|[12][0-9]|[3][01])$",birthday)
        if result:
            year = int(result.group(1))
            month = int(result.group(2))
            day = int(result.group(3))
            return cls(year,month,day)
        else:
            exit("Invalid Date Type")



def main():
    print(Seasons.get())



if __name__ == "__main__":
    main()