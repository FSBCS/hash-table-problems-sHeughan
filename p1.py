Letters = {"A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, 
            "I": 73, "J": 74, "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80,
            "Q": 81, "R": 82, "S": 83, "T": 84, "U": 85, "V": 86, "W": 87, "X": 88,
            "Y": 89, "Z": 90, "a": 97, "b": 98, "c": 99, "d": 100,"e": 101,"f": 102,
            "g": 103,"h": 104,"i": 105,"j": 106,"k": 107,"l": 108,"m": 109,"n": 110,
            "o": 111,"p": 112,"q": 113,"r": 114,"s": 115,"t": 116,"u": 117,"v": 118,
            "w": 119,"x": 120,"y": 121,"z": 122
            }

def hash(s):
    hash_num = 0
    for x in s:
        hash_num += Letters[x]
    hash_num = hash_num % 100
    #print(hash_num)
    return hash_num

def group_anagrams(words):
    anagrams = {}
    for x in words:
        if hash(x) not in anagrams:
            anagrams[hash(x)] = [x]
        
        else:
            anagrams[hash(x)].append(x)

    final_list = []
    for x in anagrams.values():
        final_list += [x]
    return final_list

words = ["bat", "meta", "tab", "tea", "ate", "tame", "jazz", "eat"]
print(group_anagrams(words))