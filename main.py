def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  lower_text= get_num_letters(text)
  print(f"{num_words} words found in the document")
  print(f"{lower_text}")

def get_num_words(text):
  words = text.split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def get_num_letters(text):
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] +=1
    else:
      chars[lowered] = 1
  return chars



main()