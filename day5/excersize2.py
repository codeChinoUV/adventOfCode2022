class BoxManager:

    def __init__(self, box_definitions_file: str):
        self._box_definitions_file = box_definitions_file
        self._stacks = [[], [], [], [], [], [], [], [], []]
        self._read_boxes_information()


    def _read_boxes_information(self, boxes_quantity = 9, characteres_distance = 4, start_in_character = 1 ):
        file = open(self._box_definitions_file, 'r')
        lines_readed_count = 1
        for line in file:
            for current_box in range(boxes_quantity):
                box_information_position = start_in_character
                if current_box != 0:
                    box_information_position += characteres_distance * current_box
                if line[box_information_position] != ' ':
                    self._stacks[current_box].insert(0, line[box_information_position])
            lines_readed_count += 1
            if lines_readed_count == boxes_quantity:
                break
        file.close()

    def reorder_stacks(self, order_instructions_start = 11):
        instructions = open(self._box_definitions_file, 'r')
        current_reading_line = 1
        for instruction in instructions:
            if current_reading_line >= order_instructions_start:
                current_instructions = instruction.split(' ')
                quantity_movements = int(current_instructions[1])
                stack_origin = int(current_instructions[3]) - 1
                stack_destination = int(current_instructions[5]) - 1

                movement_buffer = self._stacks[stack_origin][-quantity_movements:]

                del self._stacks[stack_origin][-quantity_movements:]
                self._stacks[stack_destination].extend(movement_buffer)
                
            current_reading_line += 1
    
    def get_stacks_items_on_the_top(self):
        items_on_the_top = ''
        for stack in self._stacks:
            items_on_the_top += stack[-1]
        return items_on_the_top



if __name__ == "__main__":
    box_manager = BoxManager('input.txt')
    box_manager.reorder_stacks()
    items_on_the_top = box_manager.get_stacks_items_on_the_top()
    print(f"After reorder the boxes the items on the top are {items_on_the_top}")
