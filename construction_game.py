class ConstructionGame:
    def __init__(self, length, width):
        """
        :param length: (int) Length of the base
        :param width: (int) Width of the base
        """
        # Write your code here
        self.length = length
        self.width = width
        self.table = []

        for i in range(self.length):
            self.table.append([0] * self.width)


    def add_cubes(self, cubes):
        """
        :param cubes: (list(bool)) The position of each cube to be dropped on the table
        """
        # Write your code here

        for r in range(len(cubes)):
            for c in range(len(cubes[0])):
                if cubes[r][c]:
                    self.table[r][c] += 1


    def height(self):
        """
        :returns: (int) The maximum vertical height in cubes
        """
        # Write your code here
        hights = []
        for r in range(len(self.table)):
                hights.append(max(self.table[r]))
        
        return max(hights)
                

if __name__ == "__main__":
    game = ConstructionGame(2, 2)

    game.add_cubes([
        [True, True],
        [False, False]
    ])
    game.add_cubes([
        [True, True],
        [False, True]
    ])
    print(game.height())

    game.add_cubes([
        [False, False],
        [True, True]
    ])
    print(game.height())