def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  char_dict = get_num_letters(text)
  char_sort = get_char_sort(char_dict)
  
  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} words found in the document")
  print()
  for key in char_sort:
    print(f"The '{key}' character was found {char_sort[key]} times")
  print("--- End report ---")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_words(text):
  words = text.split()
  return len(words)
  
def get_num_letters(text):
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] +=1
    else:
      chars[lowered] = 1
  return chars

def get_char_sort(char_dict):
  sorted_chars = dict(sorted(char_dict.items()))
  key = ''
  value = ''
  
  for key in list(sorted_chars):
    if key.isalpha() != True:
      sorted_chars.pop(key)
  return sorted_chars
main()