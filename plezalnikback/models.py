from django.db import models

class User(models.Model):
    fullname = models.CharField(max_length=200)
    fb_id = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return self.fullname
    
class Achievement(models.Model):
    achievement_type = models.CharField(max_length=20)
    grade_no = models.IntegerField()
    grade_letter = models.CharField(max_length=1)
    grade_speed = models.CharField(max_length=20)
    isfirst = models.BooleanField(default=False)
    date = models.DateField()
    user = models.ForeignKey(User)
    
    def ocena(self):
        value = str(self.grade_no) + self.grade_letter
    
    def __str__(self):
        value = str(self.grade_no) + self.grade_letter
        return value