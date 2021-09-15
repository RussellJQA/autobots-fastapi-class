first_name = "Russell"
age: int = 56
employed = True
fav_numbers = [1,2,3,4,5, "six", True, first_name]
# print(first_name)
# print(age)
# print(fav_numbers[2])
# print(fav_numbers[:3])

user = {
    "first_name": first_name,
    "last_name": "Johnson",
    "age": 56,
    "favorite_food": ["Korean Food", "Pizza", "Burritos"],
    1: "hello"
}
print(user["favorite_food"][2])
print(user["favorite_food"][-1])

# start : stop : step
# [start:stop:step]
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1 

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6  (slice position)
#    0   1   2   3   4   5    (index position)
