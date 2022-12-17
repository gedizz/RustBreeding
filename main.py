from manager import SeedManager



seed_manager = SeedManager()
running = True

while running:
    print("Welcome to the Breeding Manager")
    print("-------------------------------")
    print("1) Add a seed")
    print("2) Modify a seed")
    print("3) Display all seeds")
    print("4) Calculate value for a seed")
    print("0) Exit (Will delete all progress)")
    print("-------------------------------")
    userInput = input("Enter a command: ")
    if userInput == "1":
        seed_manager.add_seed()
    elif userInput == "2":
        seed_manager.print_seeds()
        idx = input("Which seed do you want to modify: ")
        seed_manager.modify_seed(seed_manager.seeds[int(idx)])
    elif userInput == "3":
        seed_manager.print_seeds()
    elif userInput == "4":
        seedToCalc = input("Which seed to calculate: ")
        seed_manager.seeds[int(seedToCalc)].calculate_result()
    elif userInput == "0":
        running = False
    else:
        print("You entered in invalid command")