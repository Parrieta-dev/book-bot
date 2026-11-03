from stats import get_word_count, get_char_count, char_dict_to_sorted_list
import sys

def get_book_text(filepath: str) -> str:
    """
    Reads the content of a book from a given file path.

    Args:

    Returns:
        str: The content of the book.
    """
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path: str, word_count: int, char_count_list: list[tuple[str, int]]):
    """
    Prints the results from the rest of the code in a pretty format
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char, count in char_count_list:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============= END ===============")

def main(filepath: str): # You could do this main(filepath: str = "books/frankenstein.txt"): to make it so that if no filepath is provided, it defaults to frankenstein.txt but oh well.
    """
    Main function to execute the book reading functionality.
    """
    book_text = get_book_text(filepath)
    
    num_words = get_word_count(book_text)
    
    dict_char_count = get_char_count(book_text) 
    sorted_char_count = char_dict_to_sorted_list(dict_char_count)

    print_report(filepath, num_words, sorted_char_count)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)