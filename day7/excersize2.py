
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

    def __init__(self, total_space = 70_000_000):
        self.__init_path = PathElement('/', True, 0, None)
        self.__current_path = self.__init_path
        self.__total_space = total_space

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

    def get_used_space(self):
        return self.__init_path.get_size()

    def get_free_space(self):
        return self.__total_space - self.__init_path.get_size()

    def get_folder_closest_to_size(self, size):
        return self._find_clostest_folder_with_size(self.__init_path, size)

    def _find_clostest_folder_with_size(self, current_folder: PathElement, min_size: int):
        folder_closets_to_size = current_folder if current_folder.get_size() >= min_size else None

        for folder in current_folder.get_folders_children():
            folder_closest = self._find_clostest_folder_with_size(folder, min_size)
            if folder_closets_to_size is None:
                folder_closets_to_size = folder_closest
            else:
                if folder_closest is not None and folder_closest.get_size() < folder_closets_to_size.get_size():
                    folder_closets_to_size = folder_closest

        return folder_closets_to_size

        

    def _find_folders_grather_than(self, current_folder: PathElement, min_size: int):

        if current_folder.name != "/" and current_folder.get_size() >= min_size:
            return [current_folder]

        

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

    def get_free_space(self):
        return self.__system_files.get_free_space()

    def get_space_used(self):
        return self.__system_files.get_used_space()

    def get_folder_with_size_clostest_to(self, size):
        return self.__system_files.get_folder_closest_to_size(size)
    


if __name__ == "__main__":
    command_prompt = CommandPromptReader()
    command_prompt.read_commands_from_file('input.txt')
    free_space = command_prompt.get_free_space()
    space_used = command_prompt.get_space_used()
    space_free_needed = 30_000_000
    space_need_to_liberate = space_free_needed - free_space
    folder_to_delete = command_prompt.get_folder_with_size_clostest_to(space_need_to_liberate)

    print(f"Space in use: {space_used}")
    print(f"Free space: {free_space}")
    print(f"Space needed to install the update: {space_need_to_liberate}")
    print(f"The directory with the closest size is {folder_to_delete.name} with size {folder_to_delete.get_size()}")
