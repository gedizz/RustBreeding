from seed import Seed

class SeedManager():
    def __init__(self):
        self.seeds = []


    def add_seed(self):
        id = len(self.seeds)
        newSeed = Seed(id)
        primary = input("Enter the primary seed genes: ")
        newSeed.primary = primary.upper()
        numGenes = input("How many genes would you like to add to this seed: ")
        for x in range(1, int(numGenes) + 1):
            neighbor = input("Enter a neighbor gene: ")
            newSeed.neighbors.append(neighbor.upper())
        self.seeds.append(newSeed)

    def remove_seed(self, seed):
        for x in self.seeds:
            if seed == x:
                self.seeds.remove(x)

    def print_seeds(self):
        for seed in self.seeds:
            self.print_single_seed(seed)
        print("\n\n\n")
            

    def modify_seed(self, seed):
        print("Seed to modify: ")
        self.print_single_seed(seed)
        print("1) Modify primary")
        print("2) Modify neighbor")
        print("0) Go back to menu")
        userInput = input("\nEnter a command: ")
        if userInput == "1":
            newPrimary = input("Enter new primary genes: ")
            seed.primary = newPrimary.upper()
        if userInput == "2":
            neighbor = input("Which neighbor would you like to edit: ")
            if seed.neighbors[int(neighbor)]:

                newNeighbor = input("Enter new gene: ")
                seed.neighbors[int(neighbor)] = newNeighbor.upper()
            else:
                print("invalid neighbor index")


    def print_single_seed(self, seed):
        print("----------------")
        print(f"Seed #{seed.id}")
        print("----------------")
        print(f"Primary: {seed.primary}")
        print("----------------")
        for i in range(0, len(seed.neighbors)):
            print(f" Neighbor {i}: {seed.neighbors[i]}")
        print("-------------------------------\n")