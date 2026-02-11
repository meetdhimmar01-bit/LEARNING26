from django.db import models



# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)
    class Meta:
        db_table = "employee"
    def __str__(self):
        return self.name
        
        
class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.CharField(max_length=100)
    class Meta:
        db_table = "course"
    def __str__(self):
        return self.name 
    

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    class Meta:
        db_table = "Player"
    def __str__(self):
        return self.name
    

class teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=50)
    class Meta:
        db_table = "teacher"
    def __str__(self):
        return self.name


        
    
