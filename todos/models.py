from django.db import models

class Todo(models.Model):
    item = models.CharField('ismi',max_length=200)
    surname = models.CharField('familiyasi',max_length=200)
    phone = models.CharField('Telefon raqami',max_length=100)
    adress = models.CharField('Manzili',max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
        

    def __str__(self):
        return self.item + ' | ' + str(self.completed)