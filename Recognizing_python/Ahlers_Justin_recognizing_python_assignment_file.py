num1 = 42 #- variable declaration
num2 = 2.3 #- variable declaration
boolean = True #variable declaration boolean
string = 'Hello World' #variable declaration string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuple
print(type(fruit)) #print console, type check
print(pizza_toppings[1]) #print console, access value, list
pizza_toppings.append('Mushrooms') #list, add value
print(person['name']) #print console, access value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary change value
print(fruit[2]) #print console, access value

if num1 > 45: #conditional
    print("It's greater") #print string to console
else: #conditional
    print("It's lower") #print string to console

if len(string) < 5: #conditional
    print("It's a short word!") #print string to console
elif len(string) > 15: #conditional
    print("It's a long word!") #print string to console
else: #conditional
    print("Just right!") #print string to console

for x in range(5): #for loop, set range
    print(x) #print to console
for x in range(2,5): #for loop, set range
    print(x) #print to console
for x in range(2,10,3): #for loop, set range
    print(x) #print to console
x = 0 #variable declaration
while(x < 5): #while loop
    print(x) #print to console
    x += 1 #changing increment

pizza_toppings.pop() #list, remove value to the end
pizza_toppings.pop(1) #list, remove value to index position 1

print(person) #print to console
person.pop('eye_color') #dictionary, remove value of eye color
print(person) #print to console

for topping in pizza_toppings: #for loop 
    if topping == 'Pepperoni': #conditional 
        continue #continue
    print('After 1st if statement') #print to console
    if topping == 'Olives': #conditional
        break #stop

def print_hello_ten_times(): #function decleration
    for num in range(10): #for loop, set range
        print('Hello') #print string to console

print_hello_ten_times() #print function to console

def print_hello_x_times(x): #function decleration, set perameter
    for num in range(x): #for loop, set range
        print('Hello') #print string to console

print_hello_x_times(4) #print function to console

def print_hello_x_or_ten_times(x = 10): #function decleration, set perameter
    for num in range(x): #for loop, set range
        print('Hello') #print string to console

print_hello_x_or_ten_times() #print function to console
print_hello_x_or_ten_times(4) #print function to console


"""
Bonus section
"""

print(num3) #print variable to console
num3 = 72 #variable declaration
fruit[0] = 'cranberry' #add value to index 0
print(person['favorite_team']) #dictionary print value to console
print(pizza_toppings[7])  #print list index 7 to console
    print(boolean) #print true false to console
fruit.append('raspberry') #add vale to end 
fruit.pop(1) #remove value in index 1. 