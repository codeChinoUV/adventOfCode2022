
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
        quantity_visible_trees = 0
        for i in range(position_x + 1, len(self.__tree_grid[position_y])):
            quantity_visible_trees += 1
            if self.__tree_grid[position_y][i] >= self.__tree_grid[position_y][position_x]:
                return quantity_visible_trees
            
        return quantity_visible_trees

    def _check_left(self, position_y: int, position_x: int):
        quantity_visible_trees = 0
        for i in range(position_x - 1, -1, -1):
            quantity_visible_trees += 1
            if self.__tree_grid[position_y][i] >= self.__tree_grid[position_y][position_x]:
                return quantity_visible_trees

        return quantity_visible_trees

    def _check_bottom(self, position_y: int, position_x: int):
        quantity_visible_trees = 0
        for i  in range(position_y + 1, len(self.__tree_grid[position_y])):
            quantity_visible_trees += 1
            if self.__tree_grid[i][position_x] >= self.__tree_grid[position_y][position_x]: 
                return quantity_visible_trees

        return quantity_visible_trees

    def _check_top(self, position_y: int, position_x: int):
        quantity_visible_trees = 0
        for i in range(position_y - 1, -1, -1):
            quantity_visible_trees += 1
            if self.__tree_grid[i][position_x] >= self.__tree_grid[position_y][position_x]:
                return quantity_visible_trees

        return quantity_visible_trees

    def _get_scenic_score_from_spot(self, position_y, position_x: int):
        visible_from_left = self._check_left(position_y, position_x)
        visible_from_right = self._check_right(position_y, position_x)
        visible_from_top = self._check_top(position_y, position_x)
        visible_from_bottom = self._check_bottom(position_y, position_x)

        return visible_from_left * visible_from_right * visible_from_top * visible_from_bottom

    def get_highest_scenic_score(self): 
            highest_scenic_score = 0
            for i in range(1, len(self.__tree_grid) -1):
                for j in range(1, len(self.__tree_grid[i]) -1):
                    score = self._get_scenic_score_from_spot(i, j)
                    if score > highest_scenic_score:
                        highest_scenic_score = score
            return highest_scenic_score


if __name__ == "__main__":
    watcher = TreeWatcher('input.txt')
    highest_score = watcher.get_highest_scenic_score()
    print(f"The highest scenic score is {highest_score}")