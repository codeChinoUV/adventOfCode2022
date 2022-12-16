class RuckSacksManager:

    _priority_items_order = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def _search_repeat_item(self, first_compartment: str, second_compartment: str) -> str:
        for character in first_compartment:
            if character in second_compartment:
                return character
        return None

    def _get_item_priority(self, item: str) -> int:
        priority = self._priority_items_order.index(item.lower())
        if priority is None or priority < 0:
            return 0
        priority += 1
        # When the item is lower case the priority is the same at item position
        if item.islower():
            return priority
        # When the item is upper case the priority is the continue of the lower case characteres, so we add 26
        else:
            return priority + 26

    def _calculate_repeated_items_priority(self):
        file = open(self._file_with_the_ruck_sacks_info, 'r')

        repeated_items_priority = 0
        for line in file:
            total_items = len(line)
            definition_first_comparment_end = int(total_items/2)
            first_compartment = line[:definition_first_comparment_end]
            second_compartment = line[definition_first_comparment_end:]
            repeated_item = self._search_repeat_item(first_compartment, second_compartment)
            item_priority = self._get_item_priority(repeated_item)
            repeated_items_priority += item_priority
        return repeated_items_priority


    def _search_common_item_in_group(self, group: list) -> str:
        for item in group[1]:
            if item in group[0]:
                if item in group[2]:
                    return item
        return None


    def _calculate_group_common_items_priority(self, group_size):
        file = open(self._file_with_the_ruck_sacks_info, 'r')

        items_gruops_priority = 0
        group = []
        for line in file:
            if len(group) < group_size-1:
                group.append(line)
            else:
                group.append(line)
                common_item = self._search_common_item_in_group(group)
                item_priority = self._get_item_priority(common_item)
                items_gruops_priority += item_priority
                group = []
        return items_gruops_priority

    def __init__(self, file_with_the_ruck_sacks_info: str) -> None:
        self._file_with_the_ruck_sacks_info = file_with_the_ruck_sacks_info

    def get_repeated_items_priority(self) -> int:
       return self._calculate_repeated_items_priority()

    def get_group_common_items_priority(self, group_size = 3):
        return self._calculate_group_common_items_priority(group_size)

if __name__ == "__main__":
    ruck_management = RuckSacksManager('input.txt')
    print(f"The sum of the common items on groups is {ruck_management.get_group_common_items_priority()}")
 
