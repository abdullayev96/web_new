from django.db import models

# class Fakultet(models.Model):
#     name = models.CharField(max_length = 100, blank = False, null= False )
#     age = models.SmallIntegerField(blank = False, null = False)
#
#     def __str__(self):
#         return self.name
#
# class Guruhlar(models.Model):
#     name = models.CharField(max_length = 100, blank = False, null = False)
#
#     def __str__(self):
#         return f"{self.name}"
#
# class Student(models.Model):
#     name = models.CharField(max_length = 100, blank = False,null = False)
#     price = models.IntegerField(blank = False, null = False)
#     fakultet = models.ForeignKey(Fakultet, blank = False, null = True, on_delete = models.SET_NULL)
#     guruhlar = models.ForeignKey(Guruhlar, blank = False, null = True, on_delete = models.SET_NULL)
#
#
#     def __str__(self):
#         return self.name
#
#


class Followrs(models.Model):   #### new
    id=models.IntegerField(primary_key=True)
    email=models.CharField(max_length=200, blank=False, null=False)  ### new
    name=models.CharField(max_length=200, blank=False, null=False)
    #phone=models.IntegerField(null=False, blank=False)


    def __str__(self):
        return f"{self.id} || {self.name} || {self.email} "