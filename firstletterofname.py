# 3. Create a function which answers the question "Are you playing banjo?".
# # If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

# def are_you_playing_banjo(name):
    
#     if 'r' starts name.lower():
#         return f"{name} + you are playing the banjo!"
#     else: 
#         return f"{name} + does not play banjo"

def are_you_playing_banjo(name):
    if name.lower().startswith('r'):
        return f"{name} plays the banjo!"
    else: 
        return f"{name} does not play the banjo"

result = are_you_playing_banjo("Rikke")
print(result)


def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'