from itertools import permutations

def find_rank(word):
    sorted_permutations = sorted(set(permutations(word)))
    return sorted_permutations.index(tuple(word)) + 1

# Get user input
word = input("Enter the word to find its rank: ")

# Calculate and print the rank
rank = find_rank(word)
print("The rank of the word '{word}' is: {rank}")