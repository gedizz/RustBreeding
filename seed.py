class Seed:
    def __init__(self, id):
        self.primary = None
        self.id = id
        self.neighbors = []
        self.result = []

    def add_primary(self):
        pass

    def add_neighbors(self):
        pass

    def change_gene(self, newGene):
        pass

    def calculate_result(self):
        result = {
            0: {
                "G": 0.0,
                "H": 0.0,
                "Y": 0.0,
                "X": 0.0,
                "W": 0.0
            },
            1: {
                "G": 0.0,
                "H": 0.0,
                "Y": 0.0,
                "X": 0.0,
                "W": 0.0
            },
            2: {
                "G": 0.0,
                "H": 0.0,
                "Y": 0.0,
                "X": 0.0,
                "W": 0.0
            },
            3: {
                "G": 0.0,
                "H": 0.0,
                "Y": 0.0,
                "X": 0.0,
                "W": 0.0
            },
            4: {
                "G": 0.0,
                "H": 0.0,
                "Y": 0.0,
                "X": 0.0,
                "W": 0.0
            },
            5: {
                "G": 0.0,
                "H": 0.0,
                "Y": 0.0,
                "X": 0.0,
                "W": 0.0
            }
        }
        for neighbor in self.neighbors:
            for i in range(0, len(result)):
                if neighbor[i] == "G":
                    result[i]["G"] += 0.6
                elif neighbor[i] == "H":
                    result[i]["H"] += 0.6
                elif neighbor[i] == "Y":
                    result[i]["Y"] += 0.6
                elif neighbor[i] == "X":
                    result[i]["X"] += 1.0
                elif neighbor[i] == "W":
                    result[i]["W"] += 1.0
                else:
                    print("Something is fucked up")
                    quit(1)

        print("RESULT: ", end="", flush=True)
        for num in result:
            print(max(result[num], key=result[num].get), end="", flush=True)
        print("\n")
        
                    
