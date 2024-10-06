from django.db import models

# Create your models here.
class GamePassword(models.Model):
    correct_password = models.CharField(max_length=50)

    def __str__(self):
        return "Game Password"
    
class ResultTeam(models.Model):
    team_name = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name