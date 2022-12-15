class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.quantity_repetitions = 1
        self.paren_node = None
        self.left_node = None
        self.right_node = None

    def set_parent_node(self, parent_node):
        self.paren_node = parent_node

    def set_left_node(self, left_node):
        self.left_node = left_node

    def set_right_node(self, right_node):
        self.right_node = right_node

    def get_value(self):
        return self.value

    def get_parent_node(self):
        return self.paren_node

    def get_left_node(self):
        return self.left_node
    
    def get_right_node(self):
        return self.right_node

    def increment_quantity_aparitions(self):
        self.quantity_repetitions += 1


class OrderedBinaryTree:
    root = None

    def insert_value(self, value: int):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node is not None:
                parent_node = current_node
                if value < current_node.value:
                    current_node = current_node.get_left_node()
                else:
                    current_node = current_node.get_right_node()
            new_node.set_parent_node(parent_node)
            if value < parent_node.value:
                parent_node.set_left_node(new_node)
            elif value > parent_node.value:
                parent_node.set_right_node(new_node)
            else:
                parent_node.increment_quantity_aparitions()
    
    def get_items_in_order_desc(self):
        return self._go_through_nodes_desc(self.root, [])

    def get_items_in_order_asc(self):
        return self._go_through_nodes_asc(self.root, [])

    def _go_through_nodes_desc(self, current_node, aculated_items = []):
        if current_node is None:
            return aculated_items
        else:
            copy_acumulated_items = aculated_items
            left_node = current_node.get_left_node()
            if left_node is not None:
                copy_acumulated_items = self._go_through_nodes_desc(left_node, aculated_items)
            
            copy_acumulated_items.append(current_node.get_value())
            
            right_node = current_node.get_right_node()
            if right_node is not None:
                copy_acumulated_items = self._go_through_nodes_desc(right_node, copy_acumulated_items)
            return self._go_through_nodes_desc(None, copy_acumulated_items)

    def _go_through_nodes_asc(self, current_node, aculated_items = []):
        if current_node is None:
            return aculated_items
        else:
            copy_acumulated_items = aculated_items
            right_node = current_node.get_right_node()
            if right_node is not None:
                copy_acumulated_items = self._go_through_nodes_asc(right_node, copy_acumulated_items)

            copy_acumulated_items.append(current_node.get_value())
            
            left_node = current_node.get_left_node()
            if left_node is not None:
                copy_acumulated_items = self._go_through_nodes_asc(left_node, aculated_items)
            
            return self._go_through_nodes_asc(None, copy_acumulated_items)


class CaloriesInventory:

    def _get_calories_carried_by_elf(self, file_path_with_calories_register: str):
        file = open(file_path_with_calories_register, 'r')
        self.calories_inventory = OrderedBinaryTree()
        counter = 0
        for line in file:
            if line[0] != '\n':
                counter += int(line)
            else:
                self.calories_inventory.insert_value(counter)
                counter = 0
                

    def __init__(self, file_path_with_calories_register: str):
        self._get_calories_carried_by_elf(file_path_with_calories_register)

    def get_inventory_items_in_order_asc(self):
        return self.calories_inventory.get_items_in_order_asc()

    def get_inventory_items_in_order_desc(self):
        return self.calories_inventory.get_items_in_order_desc()

if __name__ == "__main__":
    calories_inventory = CaloriesInventory('input_excersize_1.txt')
    items_in_the_inventary = calories_inventory.get_inventory_items_in_order_asc()
    last_three_items = items_in_the_inventary[:3]
    last_three_items_total = sum(last_three_items)
    print(f"The sum of the three elves which are carriying more calories is {last_three_items_total}")