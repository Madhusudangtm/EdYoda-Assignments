# 2. Create a dictionary of any 7 Indian states and their capitals.
# Write this into a JSON file.

import json
class State_Capital:
    def __init__(self):
        self.st_cap={}
    def creat_JSON(self):
        for i in range(7):
            s_name = input("Enter state name: ")
            c_name = input("Enter capital name: ")
            print("-------------------")
            SC_dict={s_name:c_name}
            self.st_cap.update(SC_dict)
        with open("state_capital.json",'w') as f:
            json.dump(self.st_cap,f)

    def print_JSON(self):
        with open("state_capital.json",'r') as f:  
            data = json.load(f)
        for i,j in data.items():
            print('State:'+ i + '  Capital:'+ j)    


x = State_Capital()
x.creat_JSON()
x.print_JSON()    

# Output
# Enter state name: Rajasthan
# Enter capital name: Jaipur
# -------------------
# Enter state name: Gujrat
# Enter capital name: Gandhinagar
# -------------------
# Enter state name: UP
# Enter capital name: Lucknow
# -------------------
# Enter state name: MP
# Enter capital name: Bhopal
# -------------------
# Enter state name: Bihar
# Enter capital name: Patna
# -------------------
# Enter state name: Punjab
# Enter capital name: Chandigarh
# -------------------
# Enter state name: Maharashtra
# Enter capital name: Mumbai
# -------------------
# State:Rajasthan  Capital:Jaipur
# State:Gujrat  Capital:Gandhinagar
# State:UP  Capital:Lucknow
# State:MP  Capital:Bhopal
# State:Bihar  Capital:Patna
# State:Punjab  Capital:Chandigarh
# State:Maharashtra  Capital:Mumbai
