
class PathElement:
    name: str
    _is_dir: bool
    _total_size: int
    _children_elements = []
    
    def _update_parent_size(self, size):
        if self._parent_element is not None:
            self._parent_element.add_size(size)

    def add_size(self, size: int):
        self._update_parent_size(size) 
        
        if self._is_dir is True:
            self._total_size += size
        else:
            self._total_size = size

    def __init__(self, name: str, is_dir: bool, total_size: int, parent_element) -> None:
        self.name = name
        self._is_dir = is_dir
        self._parent_element = parent_element
        self._total_size = 0
        self._children_elements = []
        self.add_size(total_size)

    def add_children(self, children):
        self._children_elements.append(children)

    def is_dir(self):
        return self._is_dir

    def get_parent_folder(self):
        return self._parent_element

    def get_folders_children(self):
        return list(filter(lambda children: children.is_dir() is True, self._children_elements))

    def get_size(self):
        return self._total_size

    def __str__(self) -> str:
        return f"{self.name}" 

class FileManager:

    def __init__(self):
        self.__init_path = PathElement('/', True, 0, None)
        self.__current_path = self.__init_path

    def create_folder(self, folder_name: str):
        new_folder = PathElement(folder_name, True, 0, self.__current_path)
        self.__current_path.add_children(new_folder)

    def create_file(self, file_name: str, size: int):
        new_file = PathElement(file_name, False, size, self.__current_path)
        self.__current_path.add_children(new_file)

    def go_to_folder(self, folder_name: str):
        current_path_children_folders = self.__current_path.get_folders_children()
        folder = next(path_element for path_element in current_path_children_folders if path_element.name == folder_name)
        if folder is not None:
            self.__current_path = folder

    def go_to_previous_path(self):
        previous_path = self.__current_path.get_parent_folder()  
        if previous_path is not None:
            self.__current_path = previous_path

    def go_to_root_path(self):
        self.__current_path = self.__init_path

    def get_folders_lower_than(self, size: int):
        folders_lower_than = self._find_folders_lower_than(self.__init_path, size)
        return folders_lower_than

    def _find_folders_lower_than(self, current_folder: PathElement, max_size: int):
        childrens_lower_than = []
        children_folders = current_folder.get_folders_children()
        
        for folder in children_folders:
            folders_lower_inside_folder = self._find_folders_lower_than(folder, max_size)
            childrens_lower_than.extend(folders_lower_inside_folder)
        
        if current_folder.get_size() <= max_size:
            childrens_lower_than.append(current_folder)
        return childrens_lower_than 

    def get_total_size_folders_lower_than(self, size: int):
        folders = self.get_folders_lower_than(size)
        total = 0
        for folder in folders:
            total += folder.get_size()
        return total


    def __str__(self) -> str:
        return f"Current path {self.__current_path.name}"

class CommandPromptReader:

    @classmethod
    def _is_command(cls, line):
        return line[0] == "$"

    @classmethod
    def _get_command(cls, line: str):
        line = line[2:-1]
        splited_command = line.split(' ')
        command_details = { "command": splited_command[0] }

        if len(splited_command) >= 2:
            command_details['args'] = " ".join(splited_command[-1:])

        return command_details
    
    @classmethod
    def _is_folder_output(cls, line: str):
        return line.split(" ")[0] == "dir"

    @classmethod
    def _get_folder_name(cls, line: str):
        name = line.split(" ")[1]
        if name[-1] == "\n":
            return name[:-1]
        return name

    @classmethod
    def _get_file_details(cls, line: str):
        details_splitted = line.split(" ")
        name = details_splitted[1]
        if name[-1] == "\n":
            name = name[:-1]
        return {
            "name": name,
            "size": int(details_splitted[0])
        }

    def __init__(self) -> None:
        self.__system_files = FileManager()

    def _manage_command(self, command: str):
        command_details = self._get_command(command)
        if command_details["command"] == "cd":
            if command_details["args"] == "/":
                self.__system_files.go_to_root_path()
            elif command_details["args"] == "..":
                self.__system_files.go_to_previous_path()
            else:
                self.__system_files.go_to_folder(command_details["args"])
    
    def _manage_command_output(self, out_put: str):
        if self._is_folder_output(out_put):
            folder_name = self._get_folder_name(out_put)
            self.__system_files.create_folder(folder_name)
        else:
            file_details = self._get_file_details(out_put)
            self.__system_files.create_file(file_details["name"], file_details["size"])

    def read_commands_from_file(self, file_name: str):
        commands = open(file_name, 'r')
        for command in commands:
            if self._is_command(command):
                self._manage_command(command)
            else: 
                self._manage_command_output(command)

    def get_total_size_folders_lower_than(self, size: int):
        return self.__system_files.get_total_size_folders_lower_than(size)
    


if __name__ == "__main__":
    command_prompt = CommandPromptReader()
    command_prompt.read_commands_from_file('input.txt')
    total_size = command_prompt.get_total_size_folders_lower_than(100_000) 
    print(f"The sum of the folders lower or equal than 100,000 is {total_size}")