# Alejandro Chavez
# Chapter 6 exercise 3
# Word count

def get_words():
    "This gets the number of words out of a sentence"
    user_input = input('\nEnter a line of text.\n').strip()
    sentence_info = user_input.split(" ")
    print(f'Number of words in sentence is {len(sentence_info)}')

def main():
    get_words()
    
if __name__ == "__main__":
    main()

"""
    output
Enter a line of text.
This is a line of text filled with some words. I may not be able to count this high but thankfully I do not have too, thanks to this word counting script that I have made. It will automatically count it for me and tell me the amount of words within this sentence.
Number of words in sentence is 53
"""