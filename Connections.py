# Robert Guise
# Drive Capital interview
import sys
from Person import *
from typing import Dict, List, Any

class Connection:
    companies : List[str]
    contacts : Dict[str ,List[Any]]

    def __init__(self, infile):
        self.infile = infile
        self.companies = ["Drive Capital"]
        self.contacts = {}
        self.processFile()

    def addCompany(self, name: str) -> None:
        # Will add a company to the list of known companies
        self.companies.append(name)

    def addEmployee(self, name: str, company: str) -> None:
        # Will add an employee to the specified company
        self.contacts[name] = [company, Person(name)]

    def addContact(self, outside: str, inside: str) -> None:
        # adds strength to the Drive Capital employee based on the outside employee contacted
        self.contacts[inside][1].addConnection(self.contacts[outside][0])

    def processFile(self) -> None:
        # Goes through each line of the file and separates the command from the parameters
        with open(self.infile, "r") as file:
            for line in file:
                line = line.strip().split(" ")
                command = line[0]
                # Command logic
                if command == "Partner":
                    self.addEmployee(line[1], "Drive Capital")

                elif command == "Company":
                    self.addCompany(line[1])

                elif command == "Employee":
                    self.addEmployee(line[1], line[2])

                elif command == "Contact":
                    # Only accepts valid contact forms
                    if line[3] in ["email", "call", "coffee"]:
                        self.addContact(line[1], line[2])
                else:
                    print("invalid command")
            # Free the memory
            file.close()

    def bestStrength(self, company: str) -> str:
        # Goes and finds the Capital Drive employee with the greatest strength at company
        best = 0
        bestEmployee = ""
        for employee in self.contacts:
            if self.contacts[employee][0] == "Drive Capital":
                if company in self.contacts[employee][1].strength:
                    if self.contacts[employee][1].strength[company] > best:
                        best = self.contacts[employee][1].strength[company]
                        bestEmployee = employee
        if best == 0:
            return "No current relationship"
        else:
            return f"{bestEmployee} ({str(best)})"

    def __str__(self) -> str:
        # Creates the list of companies and the Capital Drive employee with the highest strength for that company
        finalSTR = ""
        self.companies.sort()
        for company in self.companies:
            if company != "Drive Capital":
                finalSTR += f"{company}: {self.bestStrength(company)}\n"
        return finalSTR

def main():

    if len(sys.argv) != 2:
        infile = input("please enter input file name: ")
    else:
        infile = sys.argv[1]

    connectionDict = Connection(infile)
    print(connectionDict)

if __name__ == '__main__':
    main()