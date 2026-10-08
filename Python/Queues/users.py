import OS

#Functions
def mainMenu():
    print(":::Main menu:::")
    print("[1].Register a new ")
    print("[2].List all users")
    print("[3].Search users")
    print("[4].Delete users")
    print("[5].Update user")
    print("[6].Show active users")
    print("[7].Show inactive users")
    print("[8].Exit")

#Main
while True:
    os.system('clear')   
    mainMenu()
    opt = input("Press any option[1-8]: ")


    match opt:
        case'1':
            os.system('clear')
            print(":::Registrer form:::")
            id = input("Ident number: ")
            firstname = input("Firstname: ")
            lastname = input("Lastname: ")
            mobil_phone= input("Mobile Phone: ")
            email = input("E-mail: ")
            gender = input("Gender: [M/F/O] ")
            
            ids.append(id)
            firstnames.append(firstname)
            lastnames.append(lastname)
            mobil_phones.append(mobil_phone)
            emails.append(email)
            statuses.append(True)
            genders.append(gender)
            Create_at.append(data.today())
            print("user has been Created Succesfully!!")
            any_Key = input("Press any key to back to Main Menu")

        case '2':
            print(":::List alll registererd users:::")



            any_Key = input("Press any Key")
        case '8':
            print("")

            any_Key = input("Bye, bye. Press any Key")    
            break
        case _:
            any_Key= input("Invalid option. Press any Key to try again")

