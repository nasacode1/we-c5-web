from django.db import models

# Create your models here.

#I must think of what tables i want for wordle. 
# in wordle game, i have 6 attempts to find the word. The list of 5 letter words must be stored. - CLASS: words FIELDS: word_name
# in the 6 attempts, i must store the words entered by the user. CLASS: Attempts FIELDS: word_name. 

class Word(models.Model):
    word_name = models.CharField(max_length=5)

    def __str__(self):
        return self.word_name

class Attempt(models.Model):
    word_name = models.ForeignKey(Word, on_delete=models.CASCADE)
    guess = models.CharField(max_length=5)
    feedback = "rrrrr"
    won = models.BooleanField(default=False)

   
    for i in range(5):
        if self.word_name[i]== self.guess[i]:
            feedback[i]='g'
    for i in range(5):
        if self.guess[i] in self.word_name and i not in green:
            feedback[i]='y'

    def __str__(self):
        if self.guess == self.word_name:
            self.won = True
            return f"Correctly guessed. You won!"
        else:
            return f"Attempt : {self.guess}"

class Game(models.Model):
    attempts_count = 6
 

    
