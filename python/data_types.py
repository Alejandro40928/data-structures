print ("hola")
personal_info = [
'Alejandro', 
'Bravo',
'18',
False,
'3128886049',
'Pasto',
["Ana", 22], 
'Malala'
]

print("Name son:", personal_info[6][0])
new_age = input("add new age of Ana")
personal_info[6][1] = new_age
print("Age Ana:", personal_info[6][1])

user_data = ('Savach', '12', 'Ubakistan')
print(user_data)

conuntries_info = {
    'country_name' : 'Colombia',
    'Capital' : 'Bogota',
    'Abbrev' : 'CO',
    "Code" : 123456
}
print(conuntries_info)