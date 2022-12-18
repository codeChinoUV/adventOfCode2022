class CampCleanUpManager:

    def _is_overlapping(self, first_start: int, first_end: int, second_start: int, second_end: int) -> bool:
        return first_start <= second_end and second_start <= first_end

    def get_quantity_asigments_overlapping(self):
        file = open(self._file_with_the_assigmenst, 'r')

        quantity_assigments_fullt_contained = 0
        for line in file:
            assigments = line.split(',')

            first_start = int(assigments[0].split('-')[0])
            first_end = int(assigments[0].split('-')[1])

            second_start = int(assigments[1].split('-')[0])
            second_end = int(assigments[1].split('-')[1])
        
            if self._is_overlapping(first_start, first_end, second_start, second_end):
                quantity_assigments_fullt_contained += 1
        return quantity_assigments_fullt_contained

    def __init__(self, file_with_the_assigmenst: str) -> None:
        self._file_with_the_assigmenst = file_with_the_assigmenst

if __name__ == "__main__":
    manager = CampCleanUpManager('input.txt')
    print(f"The quantity of assigments overlapping is {manager.get_quantity_asigments_overlapping()}")
 
