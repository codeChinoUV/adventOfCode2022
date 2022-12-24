
class TreeWatcher:
    __tree_grid = []

    def __init__(self, file_with_tree_grid_definition: str) -> None:
        self.__save_tree_grid(file_with_tree_grid_definition)

    def __save_tree_grid(self, tree_grid_definition: str):
        grid = open(tree_grid_definition, 'r')
        for row in grid:
            if row[-1] == '\n':
                row = row[:-1]
            self.__tree_grid.append(row)
    
    def print_grid(self):
        for line in self.__tree_grid:
            print(line)

    def _check_right(self, position_y: int, position_x: int):
        for i in range(position_x + 1, len(self.__tree_grid[position_y])):
            if self.__tree_grid[position_y][i] >= self.__tree_grid[position_y][position_x]:
                return False
            
        return True

    def _check_left(self, position_y: int, position_x: int):
        for i in range(position_x - 1, -1, -1):
            if self.__tree_grid[position_y][i] >= self.__tree_grid[position_y][position_x]:
                return False

        return True

    def _check_down(self, position_y: int, position_x: int):
        for i  in range(position_y + 1, len(self.__tree_grid[position_y])):
            if self.__tree_grid[i][position_x] >= self.__tree_grid[position_y][position_x]: 
                return False

        return True

    def _check_up(self, position_y: int, position_x: int):
        for i in range(position_y - 1, -1, -1):
            if self.__tree_grid[i][position_x] >= self.__tree_grid[position_y][position_x]:
                return False

        return True

    def _is_visibility(self, position_y, position_x: int):
        return self._check_left(position_y, position_x) or self._check_right(position_y, position_x) or self._check_up(position_y, position_x) or self._check_down(position_y, position_x)

    def get_visible_trees(self): 
            visibleTrees = (len(self.__tree_grid) + len(self.__tree_grid[0])) * 2 - 4;
            for i in range(1, len(self.__tree_grid) - 1):
                for j in range(1, len(self.__tree_grid[i]) -1):
                    if self._is_visibility(i, j):
                        visibleTrees += 1
                    
            return visibleTrees


if __name__ == "__main__":
    watcher = TreeWatcher('input.txt')
    visible_trees = watcher.get_visible_trees()
    print(f"The visible trees from outside the grid are {visible_trees}")