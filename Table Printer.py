# Table Printer

grid = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def gridPrint():
    for b in range(len(grid[0])):
        for a in range(3):
            item = grid[a][b]
            print(item, end = ' ')
        print ('\n'.strip ())
        

gridPrint()
