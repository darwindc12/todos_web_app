FILEPATH = "todos.txt"


def get_todos():
    """
    Open todos.txt textfile and return list of to-do items
    """
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_local):
    """
    Write/update todos.txt textfile
    """
    with open(FILEPATH, 'w') as file:
        file.writelines(todos_local)


if __name__ == "__main__":
    print("Hello")

