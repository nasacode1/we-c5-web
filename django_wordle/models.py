from django.db import models

# Create your models here.

#I must think of what tables i want for wordle. 
# in wordle game, i have 6 attempts to find the word. The list of 5 letter words must be stored. - CLASS: words FIELDS: word_name
# in the 6 attempts, i must store the words entered by the user. CLASS: Attempts FIELDS: word_name. 

class Word(models.Model):
    word_name = models.CharField(max_length=5)

    def __str__(self):
        return self.word_name
    
class Game(models.Model):
    attempts_count = models.IntegerField(default=6)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

 
class Attempt(models.Model):
    guess = models.CharField(max_length=5)
    feedback = models.CharField(max_length=5, default="rrrrr")
    won = models.BooleanField(default=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    
    
    def save(self, *args, **kwargs):
        word_name = self.game.word.word_name 
        f=['r']*5
        for i in range(5):
            if self.game.word.word_name[i]== self.guess[i]:
                f[i]='g'
        for i in range(5):
            if self.guess[i] in word_name and f[i] !='g':
                f[i]='y'
    
        self.feedback = ''.join(f)
        if self.guess == word_name:
            self.won = True
        super().save(*args, **kwargs)
        


    def __str__(self):
        if self.guess == self.game.word.word_name:
            return f"Correctly guessed. You won!"
        else:
            return f"Attempt : {self.guess}"



    
