from starwars import list_of_swapi, detail_profile
if __name__ == '__main__':
    choice = int(input("enter option"))
    while choice != 6:
        if choice == 1:
            choice1 = int(input("enter choice\n1.Starwars people list\n2.Starwars planets list\n3.Starwars films list\n"
                                "4.Starwars species list\n5.Starwars vehicles list\n6.Starwars starships list\n"))
            if choice1 == 1:
                list2 = list(list_of_swapi(site="https://swapi.co/api/people/?page=", name="name"))
                for i in list2:
                    print(i)
            elif choice1 == 2:
                list2 = list(list_of_swapi(site="https://swapi.co/api/planets/?page=", name="name"))
                for i in list2:
                    print(i)
            elif choice1 == 3:
                list2 = list(list_of_swapi(site="https://swapi.co/api/films/?page=", name="title"))
                for i in list2:
                    print(i)
            elif choice1 == 4:
                list2 = list(list_of_swapi(site="https://swapi.co/api/species/?page=", name="name"))
                for i in list2:
                    print(i)
            elif choice1 == 5:
                list2 = list(list_of_swapi(site="https://swapi.co/api/vehicles/?page=", name="name"))
                for i in list2:
                    print(i)
            elif choice1 == 6:
                list2 = list(list_of_swapi(site="https://swapi.co/api/starships/?page=", name="name"))
                for i in list2:
                    print(i)
            else:
                print("enter a valid option")

        elif choice == 2:
            name_person = "name"
            string = input("enter name of the person to show details")
            site = "https://swapi.co/api/people/?page="
            dict1 = dict(detail_profile(site, string, name_person))
            for key, value in dict1.items():
                print(key, value)
        elif choice == 4:
            name_person = "name"
            string = input("enter name of the personpassword"
                           ""
                           " to show details")
            site = "https://swapi.co/api/people/?page="
            dict1 = dict(detail_profile(site, string, name_person))
            for key, value in dict1.items():
                print(key, value)
