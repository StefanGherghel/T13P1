from functional import seq
from collections import namedtuple
import datetime

class Person():
    def __init__(self, firstName, lastName, dateOfBirth, emailAdress):
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.emailAdress = emailAdress

    def printare(self):
        print(self.firstName)
        print(self.lastName)
        print(self.dateOfBirth)
        print(self.emailAdress)

if __name__ == "__main__":



    print("Incepem programul")

    lista_de_persoane = [Person("John", "Doe", datetime.datetime(1960, 11, 3),     "jdoe@example.com"),
                         Person("Ellen", "Smith", datetime.datetime(1992, 5, 13),  "ellensmith@example.com"),
                         Person("Jane", "White", datetime.datetime(1986, 2, 1),    "janewhite@example.com"),
                         Person("Bill", "Jackson", datetime.datetime(1999, 11, 6), "bjackson@example.com"),
                         Person("John", "Smith", datetime.datetime(1975, 7, 14),   "johnsmith@example.com"),
                         Person("Jack", "Williams", datetime.datetime(2005, 5, 28), "")]

    print("The youngest")
    youngest = (seq(lista_de_persoane).sorted(key=lambda item: item.dateOfBirth).last())
    youngest.printare()
    print()

    print("The oldest")
    oldest = (seq(lista_de_persoane).sorted(key=lambda item: item.dateOfBirth).first())
    oldest.printare()
    print()

    print("Majorii sunt")
    astazi = datetime.datetime.now().year

    underage = list(seq(lista_de_persoane).filter(lambda persoana: astazi - persoana.dateOfBirth.year  > 18))
    for person in underage:
        person.printare()

    emails = list(seq(lista_de_persoane).map(lambda persoana: persoana.emailAdress))
    print(emails)

    emailsMap = list(seq(lista_de_persoane).map(lambda persoana: (persoana.firstName + " " + persoana.lastName, persoana.emailAdress)))
    print(emailsMap)

    emailPersonMap = list(seq(lista_de_persoane).map(lambda persoana: (persoana.emailAdress, persoana)))
    for element in emailPersonMap:
        print(element[0])
        element[1].printare()

    peopleToCelebrateEachMonth = list(seq(lista_de_persoane).group_by(lambda persoana: persoana.dateOfBirth.month))
    print("birthdays each month")
    print(peopleToCelebrateEachMonth)

    mapByBirthYear = list(seq(lista_de_persoane).partition(lambda persoana: persoana.dateOfBirth.year <= 1980))
    print("Born before / after 1980")

    averageAge = seq(lista_de_persoane).map(lambda persoana: astazi - persoana.dateOfBirth.year).average()
    print("Average age")
    print(averageAge)

    smiths = seq(lista_de_persoane).count(lambda persoana: persoana.lastName == "Smith")
    print("Number of people named Smith")
    print(smiths)

    searchResult = seq(lista_de_persoane).filter(lambda persoana: persoana.firstName == "Thomas").map(lambda obj: obj.lastName)
    if(searchResult.empty()):
        print("Nu exista numele Thomas")
