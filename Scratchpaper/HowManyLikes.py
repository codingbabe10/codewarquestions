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
