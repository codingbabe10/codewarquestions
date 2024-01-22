# 1. You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.



def likes(names):
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))


def likes(howmanylikes):
    if len(howmanylikes) == 0:
        return "no one likes this"
    elif len(howmanylikes) == 1:
        return f"{howmanylikes[0]} likes this"
    else:
        return f"{', '.join(howmanylikes[:-1])} and {howmanylikes[-1]} like this"


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))









# 2. Return negative number

def make_negative(number):
    if number > 0:
        return number * -1
    else:
        return number

#3. Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

def are_you_playing_banjo(name):
    
    if name.lower().startswith['r']:
        return f"{name} + you are playing the banjo!"
    else: 
        return f"{name} + does not play banjo"
    

    #4 convert string to number

def string_to_number(s):
    result = int(s)
    return result


input_string = "42"
result_number = string_to_number(input_string)

print(f"The converted number is: {result_number}")

#5 implement a function which convert the given boolean value into its string representation.

def boolean_to_string(value):
    return str(value)


boolean_value = True
string_representation = boolean_to_string(boolean_value)

print(f"The string representation is: {string_representation}")

# https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
# I apologize I saw the instrction to put the link the Kata, after completing the 5th 
#question.