
class CommunicationSystem:

    def __init__(self, incoming_message_from_file: str, different_characteres_quantity = 4):
        self._different_characteres_quantity = different_characteres_quantity
        self._incoming_message_from_file = incoming_message_from_file

    def _constains_package_start_market(self, current_package: str) -> bool:
        current_character_position = 0
        for character in current_package:
            character_position = current_package.find(character)
            if character_position >= 0 and character_position != current_character_position :
                return False
            current_character_position += 1
        return True

    def get_first_package_start_marked(self):
        message = open(self._incoming_message_from_file, 'r')
        message_readed = ''
        for trama in message:
            message_readed += trama

        message_reading_position = self._different_characteres_quantity 
        for current in range(message_reading_position, len(message_readed)):
            package = message_readed[current - message_reading_position : current]
            if self._constains_package_start_market(package):
                return current
        return -1

if __name__ == "__main__":
    communication = CommunicationSystem('input.txt')
    print(f"The first package start marked is in the position {communication.get_first_package_start_marked()}")