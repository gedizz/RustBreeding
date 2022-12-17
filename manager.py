from seed import Seed

class SeedManager():
    def __init__(self):
        self.seeds = []


    def add_seed(self):
        id = len(self.seeds)
        newSeed = Seed(id)
        primary = input("Enter the primary seed genes: ")
        newSeed.primary = primary
        numGenes = input("How many genes would you like to add to this seed?")
        for x in range(1, int(numGenes) + 1):
            neighbor = input("Enter a neighbor gene: ")
            newSeed.neighbors.append(neighbor)
        self.seeds.append(newSeed)

    def remove_seed(self, seed):
        for x in self.seeds:
            if seed == x:
                self.seeds.remove(x)

    def print_seeds(self):
        for seed in self.seeds:
            print("----------------")
            print(f"Seed #{seed.id}")
            print("----------------")
            print(f"Primary: {seed.primary}")
            print("----------------")
            for i in range(0, len(seed.neighbors)):
                print(f" Neighbor {i}: {seed.neighbors[i]}")
            print("-------------------------------")