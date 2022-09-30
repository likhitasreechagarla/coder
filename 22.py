def containsVowels(string):
    string=string.lower()
    for char in string:
        if char in "aeiou":
            return True
    return False
print(containsVowels("education"))
print(containsVowels("automobile"))
print(containsVowels("evacuation"))
print(containsVowels("remunaration"))
print(containsVowels("regulation"))
