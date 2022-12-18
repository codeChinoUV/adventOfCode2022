class CampCleanUpManager:

    def _is_containing(self, first_assigment: list, second_assigment: list) -> bool:
        return first_assigment[0] >= second_assigment[0] and first_assigment[1] <= second_assigment[1]

    def _get_assigment_integers_from_string(self, assigment: str):
        assigments = assigment.split('-')
        return [int(assigments[0]), int(assigments[1])]

    def get_assignments_contained(self):
        file = open(self._file_with_the_assigmenst, 'r')

        quantity_assigments_fullt_contained = 0
        for line in file:
            assigments = line.split(',')
            first_assigment = self._get_assigment_integers_from_string(assigments[0])
            second_assigment = self._get_assigment_integers_from_string(assigments[1])
            if self._is_containing(first_assigment, second_assigment) \
              or self._is_containing(second_assigment, first_assigment):
                quantity_assigments_fullt_contained += 1
        return quantity_assigments_fullt_contained

    def __init__(self, file_with_the_assigmenst: str) -> None:
        self._file_with_the_assigmenst = file_with_the_assigmenst

if __name__ == "__main__":
    manager = CampCleanUpManager('input.txt')
    print(f"The quantity of assigments fully contained is {manager.get_assignments_contained()}")
 
