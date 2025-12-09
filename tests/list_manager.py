my_list = []


def initialize_list():
    """Reset the list to empty."""
    global my_list
    my_list = []
    return my_list


def get_list():
    """Return the current list."""
    return my_list


def add_to_list(item):
    """Add an item to the list and return the updated list."""
    my_list.append(item)
    return my_list


def remove_from_list(item):
    """Remove item from the list, raise ValueError if missing."""
    if item not in my_list:
        raise ValueError("Item not found in list")
    my_list.remove(item)
    return my_list


def replace_item_in_list(item, replacement):
    """Replace an item with another. Raise ValueError if item is not found."""
    if item not in my_list:
        raise ValueError("Item not found in list")
    index = my_list.index(item)
    my_list[index] = replacement
    return my_list


def get_item_at_position(position):
    """Return the item at a specific index. Raise ValueError if out of range."""
    if position < 0 or position >= len(my_list):
        raise ValueError("Invalid list index")
    return my_list[position]
