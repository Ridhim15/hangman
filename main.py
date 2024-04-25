from hangman_word import word_list
import random
from hangman_art import logo,stages
from Hintfn import give_hint
import os



class Hangman:
    # contructor and class reference 
    def __init__(self) -> None:
        self.word=random.choice(word_list) #chooses random word from word list
        self.l=len(self.word)
        self.blank=['__']*self.l #create as many balnks as word length
        self.life=6 #life count for each hangman image
        self.losestreak=0
        self.hashset=set() #hashset for checking and displaying already entered letters
        self.word_idx_table = {} # HashMap
        
        for idx, ch in enumerate(self.word): #creating hashmap for hint function
            #if key does not exist in hashmap create key with empty list (prevents)
            if ch not in self.word_idx_table:
                self.word_idx_table[ch] = []
            self.word_idx_table[ch].append(idx)
            
            


    def main(self):# function containg main workings of game
        print(logo)
        print(stages[self.life],"\n")
        print("\n",*self.blank,"\n")
        while self.life>0:
          k=False
          if self.losestreak>3:
            self.losestreak=0
            print("\nHint function can be called")
            want_hint=input ("\nPress any key if you want hint\nPress 'n' if you want to continue without hint\n")
            if want_hint.lower()=="n":
              pass
            give_hint(self.word_idx_table,self.blank,self.hashset)
            print(stages[self.life],"\n")
            print("\n",*self.blank,"\n")


          user=input("Guess a letter \n")
          if not (len(user) == 1 and user.isalpha()):
              print("Please enter correct input\n")
              continue 
          if user in self.hashset:
              print("You have already entered this word\n")
              continue
          self.hashset.add(user)
      
        #REPLACING BLANK WITH CH IF USER GUESS IS CORRECT
          if user.lower() in self.word_idx_table.keys():
            k=True
            for ch in (self.word_idx_table[user.lower()]):
              self.blank[ch]=user.lower()
            print(f"Your chosen letter: {user} is correct\n")
            print(*self.blank)
            del self.word_idx_table[user]
          if not k:
            self.life-=1
            self.losestreak+=1
            print(f"Wrong Guess \nYou lose a live \nYou have now only {self.life} left \n")
          print(stages[self.life],"\n",*self.blank)
          if "__" not in self.blank:
              print("You win")
              break
          if self.life==0:
            print("You have 0 lives left \nYou lose\n")


    def gameloop(): 
        while True:
            obj=Hangman()
            obj.main()
            play_again=input("Do you want to play again\nPress 'Y' for yes 'N' for no\n\n")
            if play_again.lower()=='n':
                break
            os.system('cls||clear')
    
    
Hangman.gameloop()
