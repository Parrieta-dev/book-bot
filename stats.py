def get_word_count(text: str) -> int:
    """
    Gets a string with text and returns the number of words in it

    Args:
        text (str): The text to be analyzed

    Returns:
        word_count (int): The number of words in the text
    """
    split_text = text.split()
    return len(split_text)

def get_char_count(text: str) -> dict[str,int]:
    """
    Gets a string with text and returns the number of counts for each distinct lower case character.

    Args:
        text (str): The text to be analyzed

    Returns:
        character_counts (dict[str,int]): The number of instances of each character in the text
    """

    lowercase_text = text.lower()

    character_counts = {}

    i = 0

    for char in lowercase_text:
        if char not in character_counts:
            character_counts[char] = 1
        else:
            character_counts[char] += 1

    return character_counts

def sort_on(char_count: tuple[str,int]) -> int:
    """
    Support function meant to help sort the character counts in descending order later.
    """
    return char_count[1]

def char_dict_to_sorted_list(char_dict: dict[str,int]) -> list[tuple[str,int]]:
    """
    Gets a dictionary with the number of counts for each distinct lower case character, and returns it as a sorted list of tuples for clarity in outputs

    Args:
        text (str): The text to be analyzed

    Returns:
        character_counts (dict[str,int]): The number of instances of each character in the text
    """
    
    temp_list = []
    
    for char in char_dict:
        new_tuple = char, char_dict[char]
        temp_list.append(new_tuple)

    sorted_list = sorted(temp_list, reverse=True, key=sort_on)
    return sorted_list