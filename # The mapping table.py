# The mapping table
mapping = {
    "L": "a", "v": "b", "0": "c", "V": "d", "R": "e", "9": "f", "I": "g", "z": "h",
    "8": "i", "4": "j", "q": "k", "c": "l", "Z": "m", "b": "n", "1": "o", "y": "p",
    "X": "q", "P": "r", "U": "s", "7": "t", "K": "u", "w": "v", "t": "w", "d": "x",
    "k": "y", "S": "z", "A": "A", "C": "B", "x": "C", "i": "D", "D": "E", "6": "F",
    "a": "G", "F": "H", "J": "I", "e": "J", "O": "K", "5": "L", "H": "M", "f": "N",
    "p": "O", "n": "P", "o": "Q", "B": "R", "3": "S", "W": "T", "l": "U", "T": "V",
    "Y": "W", "j": "X", "s": "Y", "2": "Z", "N": "0", "g": "1", "m": "2", "G": "3",
    "Q": "4", "r": "5", "u": "6", "h": "7", "M": "8", "E": "9"
}

# Example garbled data (replace this with your file's content)
garbled_data = "LvR9I8cZ"

# Decode the garbled data
decoded_data = ''.join([mapping.get(char, char) for char in garbled_data])

# Split the decoded data into words
words = decoded_data.split()

# Extract the 4th character from each word
fourth_chars = [word[3] for word in words if len(word) > 3]

# Construct the flag
flag = f"HQ9{{{''.join(fourth_chars)}}}"

print(flag)
