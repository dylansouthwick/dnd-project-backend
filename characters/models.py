from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    
class Class(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Race(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    bonuses = models.TextField()

    def __str__(self):
        return self.title

class Character(models.Model):
    full_name = models.CharField(max_length=200)
    age = models.IntegerField()
    back_story = models.TextField(blank=True, null=True)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    equipment = models.TextField(blank=True, null=True)
    spells = models.TextField(blank=True, null=True)
    race_id = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='characters')
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='characters')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')

    def __str__(self):
        return f'{self.full_name}'


