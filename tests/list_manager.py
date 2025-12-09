my_list = []


def initialize_list():
    """Reset the list to empty."""
    global my_list
    my_list = []


def get_list():
    """Return the current list."""
    return my_list


def add_to_list(item):
    """Add an item to the list."""
    my_list.append(item)


def remove_from_list(item):
    """Remove an item. Raise ValueError if missing."""
    if item not in my_list:
        raise ValueError("Item not found")
    my_list.remove(item)


def replace_item_in_list(item, replacement):
    """Replace item with replacement. Raise ValueError if item not in list."""
    if item not in my_list:
        raise ValueError("Item not found")
    index = my_list.index(item)
    my_list[index] = replacement


def get_item_at_position(position):
    """Return item at 1-based position. Raise ValueError if invalid."""
    index = position - 1
    if index < 0 or index >= len(my_list):
        raise ValueError("Invalid list index")
    return my_list[index]
