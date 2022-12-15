class CaloriesInventory:
    calories_carried_by_elf = {}
    elf_carriyin_more_calories = None

    def _validate_is_elf_carriyin_more_calories(self, current_elf, current_calories_carriying):
        if self.elf_carriyin_more_calories is None:
            self.elf_carriyin_more_calories = current_elf
        else:
            if self.calories_carried_by_elf[self.elf_carriyin_more_calories] < current_calories_carriying :
                self.elf_carriyin_more_calories = current_elf


    def _get_calories_carried_by_elf(self, file_path_with_calories_register: str):
        file = open(file_path_with_calories_register, 'r')
        counter = 0
        elf_number = 1
        for line in file:
            if line[0] != '\n':
                counter += int(line)
            else:
                self._validate_is_elf_carriyin_more_calories(elf_number, counter)
                self.calories_carried_by_elf[elf_number] = counter;
                counter = 0
                elf_number += 1

    def __init__(self, file_path_with_calories_register: str):
        self._get_calories_carried_by_elf(file_path_with_calories_register)

    def get_elf_carriying_most_calories(self):
        return self.elf_carriyin_more_calories

    def get_more_calories_quantity(self):
        if self.elf_carriyin_more_calories is None:
            return 0
        return self.calories_carried_by_elf[self.elf_carriyin_more_calories]

    def get_inventory(self):
        return self.calories_carried_by_elf


if __name__ == "__main__":
    calories_inventory = CaloriesInventory('input_excersize_1.txt')
    print(f"The elf {calories_inventory.get_elf_carriying_most_calories()} is carritying {calories_inventory.get_more_calories_quantity()} calories")
    print(len(calories_inventory.get_inventory()))