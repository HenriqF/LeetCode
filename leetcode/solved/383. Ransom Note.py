#https://leetcode.com/problems/ransom-note/description/

ransomNote = "a"
magazine = "a"

for char in ransomNote:
    i = magazine.find(char)
    if i == -1:
        print(False)
    magazine = magazine[:i] + magazine[i+1:]
print(True)



