""" 
Author = Cedric Kim

Analyzes the word frequencies in a Tale of Two Cities """

import string
from string import maketrans    
#import TaleofTwoCities.txt

def get_word_list(file_name):
    """reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case."""
    f = open(file_name,  'r')
    lines = f.readlines()
    end_line = 0
    start_line = 0
    while lines[start_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1: ##finds the line which this is located
        start_line += 1
    while lines[end_line].find('END OF THIS PROJECT GUTENBERG EBOOK') == -1: ##fined the line which end is located
        end_line +=1
    lines = lines[start_line+1:end_line-2] ##takes the rest of the book
    s = ''
    word_string = s.join(lines)         ##joins the list into a long string
    for char in string.punctuation:
        word_string = word_string.replace(char, '')         ##removes all puncuation
    word_list = word_string.split()                         ##splits the string into a list of words
    word_list = [word.lower() for word in word_list]        ##changes uppercase into lowercase
    return word_list



def get_top_n_words(word_list, n):
    """Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurrin"""
    word_count = dict()         ##create a new dictionary
    for word in word_list:      
        word_count[word] = 1 + word_count.get(word, 0)          ##creates key value pair for the words based on their frequency
    ordered_by_frequency = sorted(word_count, key=word_count.get, reverse=True)     ##sorts the words
    return ordered_by_frequency[:n]         ##takes the n most frequent words


if __name__ == '__main__':

    word_list = get_word_list('TaleofTwoCities.txt')
    top_frequency_words = get_top_n_words(word_list, 100)
    print top_frequency_words