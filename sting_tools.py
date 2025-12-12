# string_tools.py

def count_unique_chars(text: str, cache: dict = {}):
    """
    Returns number of unique characters in the string.
    
    BUG (intentional):
    - Uses a mutable default argument `cache={}`.
    - Because of caching between calls, repeated runs with different
      inputs will return wrong results.
    """
    if text in cache:
        return cache[text]

    # compute unique count
    unique_count = len(set(text))

    # store in cache
    cache[text] = unique_count
    return unique_count


def reverse_words(sentence: str):
    """Correct function — added to distract the contributor."""
    return " ".join(word[::-1] for word in sentence.split())
