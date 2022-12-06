# Create a JSON file (employee.json) containing employee information of minimum
# 5 employees. Each employee information consists of Name, DOB, Height, City, State.
# Write a python program that reads this information from the JSON file and saves 
# the information into a list of objects of Employee class. Finally print the list 
# of the Employee objects.

# For creating a json file of 5 employees and print objects of Employee class in list-->
import json
class Employee:
    def __init__(self):
        self.emp_dic={}
    def creat_JSON(self):
        for i in range(5):
            name = input("Enter your name: ")
            dob = input('Enter your DOB: ')
            height = input('Enter your height: ')
            city = input('Enter your city: ')
            state = input('Enter your state: ')
            emp={'name':name,'dob':dob,'height':height,'city':city,'state':state}
            emp_id = len(self.emp_dic)+1
            self.emp_dic[emp_id]=emp
        with open("emps.json",'w') as f:
            json.dump(self.emp_dic,f)

    def data_print(self):
        with open("emps.json","r") as f:
            data = json.load(f)
        for i in data.values():
            l1 = []
            l1.append(i)
            print(l1)   

x =Employee()            
x.creat_JSON()
print("--------------------------------------------------")
x.data_print()  

# Output
# Enter your name: Madhusudan
# Enter your DOB: 23-11-1998
# Enter your height: 5.1
# Enter your city: Kota
# Enter your state: Rajasthan
# Enter your name: Abhishek
# Enter your DOB: 12-7-1992
# Enter your height: 5.2
# Enter your city: Jaipur
# Enter your state: Rajasthan
# Enter your name: Sonu
# Enter your DOB: 19-11-1995
# Enter your height: 4.9
# Enter your city: Jodhpur
# Enter your state: Rajasthan
# Enter your name: Hrishika
# Enter your DOB: 23-1-1997
# Enter your height: 4.8
# Enter your city: Ajmer
# Enter your state: Rajasthan
# Enter your name: Daksh
# Enter your DOB: 29-10-1998
# Enter your height: 4.9
# Enter your city: Udaipur
# Enter your state: Rajasthan
# --------------------------------------------------
# [{'name': 'Madhusudan', 'dob': '23-11-1998', 'height': '5.1', 'city': 'Kota', 'state': 'Rajasthan'}]
# [{'name': 'Abhishek', 'dob': '12-7-1992', 'height': '5.2', 'city': 'Jaipur', 'state': 'Rajasthan'}]
# [{'name': 'Sonu', 'dob': '19-11-1995', 'height': '4.9', 'city': 'Jodhpur', 'state': 'Rajasthan'}]
# [{'name': 'Hrishika', 'dob': '23-1-1997', 'height': '4.8', 'city': 'Ajmer', 'state': 'Rajasthan'}]
# [{'name': 'Daksh', 'dob': '29-10-1998', 'height': '4.9', 'city': 'Udaipur', 'state': 'Rajasthan'}]

