def reversal(word):
    if len(word) == 0:
        return word
    else:
        return reversal(word[1:]) + word[0]

def main():
    word = input("Enter a string to be reversed: ")
    print(reversal(word))

main()