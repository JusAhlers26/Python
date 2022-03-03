#1 Task print "Hello WOrld"
print("Hello World")
#2 print Hello Noelle with name in a variable
name = "Justin Ahlers"
#2a
print("Hello", name)
#2b
print("Hello" + " " + name)
# 3. print "Hello 42!" with the number in a variable
num =  26
#3a
print("Hello", num)	# with a comma
#3b is commented out for the error
#print("Hello" + " " + num)	# with a +	-- this one should give us an error! (can only concatenate str (not "int") to str)
#ninja bonus fix the error without using a coma
print("Hello" +" "+ str(num))
# 4. print "I love to eat sushi and pizza." with the foods in variables
food_one = "sushi"
food_two = "ramen"
#4a .format method
print("I love to eat {} and {}.".format(food_one, food_two))
#4b f string
print(f"I love to eat", food_one, "and", food_two)
#ninja Bonus
print(food_one.upper())
print(food_one.upper(), "and", food_two.lower())
print(food_one.split())