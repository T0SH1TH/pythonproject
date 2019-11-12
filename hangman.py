Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random 
# library that we use in order to choose random words from a list of words 
  
  
print("Good Luck ! ") 
  
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']  


word = random.choice(words) 
  
  
print("Guess the characters") 
  
guesses = '' 
  
turns = 9
  
  
while turns > 0: 
      
    # counts the number of times a user fails 
    failed = 0
      
    for char in word:  
          
        if char in guesses:  
            print(char) 
              
        else:  
            print("_") 
              
            failed += 1
              
  
    if failed == 0: 
        print("You Win")  
          
        print("The word is: ", word)  
        break
      
    # if user has input the wrong alphabet then it will ask user to enter another alphabet 
    guess = input("guess a character:") 
      
    guesses += guess  
      
    if guess not in word: 
          
        turns -= 1
          
        # if the character doesn’t match the word then “Wrong” will be given as output  
        print("Wrong") 
           
        print("You have", + turns, 'more guesses') 
          
          
        if turns == 0: 
            print("You Loose")
            print("The word is: ", word)
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
