import itertools
#how could i possibly do this without itertools? :( & Google XD

def gen_passcode(keyword):
    """
	Generates a list of possible permutations of the characters in a string.
    Args:
        keyword: string
            String of characters to generate permutations from
    Returns:
        A list, which contains all possible permutations
    """
    keyword = keyword.lower()
    keyword = "".join(set(keyword))
    wordlength = len(keyword)
    wordlist = list(itertools.permutations(keyword, wordlength))
    finalwordlist = []
    """
    incomplete, needs to remove apostrophes and commas
    """

# Add tests below
password = input("What is the password?")
gen_passcode(password)
