"""List Assessment

Fill in the following functions according to the directions in the 
docstrings.

"""


def get_indexed_items(items):
    """Given a list of items, get a list of items with their indices."""
    
    tupled_items = list(enumerate(items,0))

    return tupled_items

def words_in_common(words1, words2):
    """Find words in common."""

    unique_words = set()

    for word in words1:
        if word in words2:
            unique_words.add(word)

    return unique_words


def every_other_item(items):
    """Return every other item in `items`, starting at first item."""

    every_other_item = items[::2]

    return every_other_item



def smallest_n_items(items, n):
    """Return the `n` smallest integers in list, in descending order."""

    items.sort()
    sliced_items = items[:n]
    sliced_and_reversed_items = sliced_items[::-1]

    return sliced_and_reversed_items

    

def get_unique_characters(word):
    """Given a string, return a sorted LIST of the unique letters."""
    
    words = []
    for char in word:
        if char not in words:
            words.append(char)

    words.sort()

    return words

