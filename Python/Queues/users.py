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
            while True:    
                id = input("Ident number: ")
                count = 0
                i = 0
                while i < len (ids):
                     if id == ids[i]:
                        print("Identification number already exists!")
                        count += 1
                        break
                if count == 0:
                    break         
                
                firstname = input("Firstname: ")
                lastname = input("Lastname: ")
            
            while True:
                mobil_phone= input("Mobile Phone: ")
                countP = 0
                e = 0
                while e < len(phn):
                    if mobil_phone == phn[e]:
                        print("Numbre phone already exists!")
                        countP += 1
                        break
                if countP == 0:
                    break    

            
            while True:    
                email = input("E-mail: ")
                countE = 0
                a = 0
                while a < len (emi):
                    if email == emi[a]:
                        print ("Identifacation email already exists!")
                        break
                if countE == 0:
                    break
                
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

