#
# Welcome Pythonista. 
#
# This is a list of exercises so you can see if you got what it takes to be a Python programer. These all are begginer level type of tests, you better go hard or go home!
#  
# Exercises taken from www.berkeley.edu
# You can edit this python file and execute it to see the results directly.
# Follow me at GitHub> @ivrr207

# -------------------------------------          EXERCISE 01          -------------------------------------
# ---------------------------------------------------------------------------------------------------------
# The following code chunk contains errors that prevent it from executing properly. Find the “bugs” and correct them.

# def problem_one():

# capitals = 
# “Maryland” == “Annapolis”
# “California”: Sacramento,
# “New York”: “Albany,
# “Utah'': “Salt Lake City”,
# “Alabama”: “Montgomery”
# }
# for state, city in capitals.items()
# print(f”The capital of {state) is {‘city’}.”

# Once fixed, it should return the following output:
# The capital of Maryland is Annapolis.
# The capital of California is Sacramento.
# The capital of New York is Albany.
# The capital of Utah is Salt Lake City.
# The capital of Alabama is Montgomery.

# -------------------------------------          ANSWER 01          -------------------------------------
print("ANSWER 01:") 
# -------------------------------------------------------------------------------------------------------
def problem_one():
    capitals = {
        "Maryland": "Annapolis",
        "California": "Sacramento",
        "New York": "Albany",
        "Utah": "Salt Lake City",
        "Alabama": "Montgomery"
    }
    for state, city in capitals.items():
        print("The capital of", state, "is",city + ".")

problem_one()
# -------------------------------------          EXERCISE 02          -------------------------------------
# ---------------------------------------------------------------------------------------------------------
# Write a function multiply() that takes one parameter, an integer x. Check that x is an integer at least three characters long. If it is not, end the function and print a statement explaining why. If it is, return the product of x’s digits. Write another function matching() that takes an integer x as a parameter and “wraps” your multiply() function. Compare the results of the multiply() function on x with the original x parameter and return a sorted list of any shared digits between the two. If there are none, print “No shared digits!”
# Your code should reproduce the following examples:
# >multiply(1468)
# 192

# >multiply(74)
# This integer is not long enough!

# >matching(2789475)
# [2,4]

# -------------------------------------          ANSWER 02          -------------------------------------
print("ANSWER 02:") 
# -------------------------------------------------------------------------------------------------------

datoUsuario = int(input("Welcome. Instert a number to start the computation process."))

def multiply():
    if datoUsuario >= 3:
        test = str(datoUsuario)
        for i in test:
            counter = 1
            result = i * int(test[counter])
            counter += 1
            print(result)
            
multiply()

# -------------------------------------          EXERCISE 03          -------------------------------------
# ---------------------------------------------------------------------------------------------------------
# Write code that asks a user to input a monetary value (USD). You can assume the user will input an integer or float with no special characters. Return a print statement using string formatting that states the value converted to Euros (EUR), Japanese Yen (JPY), and Mexican Pesos (MXN). Your new values should be rounded to the nearest hundredth.

# Your code should reproduce the following examples:

# >Input a value to convert from $USD: 189
# 189 USD = 160.65 EUR = 20,909.07 JPY = 3,783.78 MXN

# >Input a value to convert from $USD: 17.82
# 17.82 USD = 15.15 EUR = 1,971.43 JPY = 356.76 MXN

# Hint: To match the exact values from the example, you can use currency conversion ratios from the time of publication. As of July 6, 2021, $1 USD is equivalent to 0.85 EUR, 110.63 JPY, and 20.02 MXN.

# -------------------------------------          ANSWER 03          -------------------------------------
print("ANSWER 03:") 
# -------------------------------------------------------------------------------------------------------

userCash = int(input("Welcome. Insert the value to convert here: "))
userEur = userCash * 0.85
userJpy = userCash * 110.63
userMxn = userCash * 20.92

print("You have inserted: ", userCash,".", "This is equivalent to:", "EUR--->", userEur,"|","JPY--->", userJpy,"|","MXN--->", userMxn,"|","Thanks for using the converter.\nTo compute a different value restart this program.")








# -------------------------------------          EXERCISE 04          -------------------------------------
# ---------------------------------------------------------------------------------------------------------
# Write a script that prompts the user for a name (assume it will be a one-word string). Change the string to lowercase and print it out in reverse, with only the first letter of the reversed word in uppercase. If the name is the same forward as it is backward, add an additional print statement on the next line that says “Palindrome!”

# Your code should reproduce the following examples:
# >Enter your name: Paul
# Luap

# >Enter your name: ANA
# Ana
# Palindrome!

# Hint: Use s.lower() and s.upper(), as appropriate.

# -------------------------------------          ANSWER 04          -------------------------------------
print("ANSWER 04:") 
# -------------------------------------------------------------------------------------------------------







# -------------------------------------          EXERCISE 05          -------------------------------------
# ---------------------------------------------------------------------------------------------------------
# Save the paragraph below — from Alice’s Adventures in Wonderland — to a variable named text. Write two programs using “for” loops and/or list comprehensions to do the following: 

# Create a single string that contains the second-to-last letter of each word in text, sorted alphabetically and in lowercase. Save it to a variable named letters and print. If a word is less than two letters in length, use the single character available.

# Find the average number of characters per word in text, rounded to the nearest hundredth. This value should exclude special characters, such as quotation marks and semicolons. Save it to a variable named avg_chars and print.

# text = “Alice was beginning to get very tired of sitting \
# by her sister on the bank, and of having nothing to do: \
# once or twice she had peeped into the book her sister \
# was reading, but it had no pictures or conversations in \
# it, ‘and what is the use of a book,’ thought Alice, \
# ‘without pictures or conversations?’”

# -------------------------------------          ANSWER 05          -------------------------------------
print("ANSWER 05:") 
# -------------------------------------------------------------------------------------------------------







# -------------------------------------          EXERCISE 06          -------------------------------------
# ---------------------------------------------------------------------------------------------------------
# Make a class named Drone that meets the following requirements:

# Has an attribute named altitude that stores the altitude of the Drone. Use a property to set the altitude attribute and make it hidden.
# Create getter and setter methods for the altitude attribute. Your setter method should return an exception if the passed altitude is negative.
# Has a method named ascend that causes the Drone to ascend to a passed altitude change.
# Has an attribute named ascend_count that stores the number of ascents the Drone has done.
# Has a method named fly that returns the Drone’s current altitude.
# Your code should mimic this sample output:
# > d1 = Drone(100)
# > d1.fly()
# The drone is flying at 100 feet.

# > d1.altitude = 300
# > d1.fly()
# The drone is flying at 300 feet.

# > d1.ascend(100)
# > d1.fly()
# The drone is flying at 400 feet.

# > d1.ascend_count
# 1

# -------------------------------------          ANSWER 06          -------------------------------------
print("ANSWER 06:") 
# -------------------------------------------------------------------------------------------------------







# -------------------------------------          EXERCISE 07          -------------------------------------
# ---------------------------------------------------------------------------------------------------------
# Write a program that lets the user create and manage a gradebook for their students. Create a Gradebook class that begins with an empty dictionary. Use helper functions inside the class to run specific tasks at the user’s request. Use the input() method to ask users what task they would like to complete. The program should continue to prompt the user for tasks until the user decides to quit. Your program must allow the user to do the following:

# Add student: Creates a new entry in a dictionary called `gradebook.` The user will input the key (a student’s name) and the value (a list of grades). You can assume grades will be integers separated by commas and no spaces.
# Add grades: Adds additional grades to an existing student’s gradebook entry.
# View gradebook: Prints the entire gradebook.
# Calculate averages: Prints each student’s unweighted average grade, rounded to the nearest hundredth.
# Quit: Ends the program.
# Your code should reproduce the following example:

# >What would you like to do?: Add student
# >Enter student name: Natalie
# A new student! Adding them to the gradebook...
# >Enter student grade(s): 87,82
# New entry complete!

# >What would you like to do?: View gradebook
# {'natalie': [87.0, 82.0]}

# >What would you like to do?: Calculate averages
# natalie: 84.50

# >What would you like to do?: Quit
# End of program

# Hint: Use a “while” loop to run the program while the input() response is anything other than “quit.” Within the “while” loop, set up if/else statements to manage each potential response.

# -------------------------------------          ANSWER 07          -------------------------------------
print("ANSWER 07:") 
# -------------------------------------------------------------------------------------------------------








# -------------------------------------          THE END.           ---------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
print("THE END.")
# ---------------------------------------------------------------------------------------------------------