from django.db import models


# from . import models
# Create your models here.
class Contact(models.Model):
    sid =   models.AutoField(primary_key=True)
    sname =     models.CharField(max_length=40)
    sgmail = models.CharField(max_length=50)
    smessage = models.CharField(max_length=150)
    class Meta:
        db_table = "Contact"
    def __str__(self):
        return self.sname

#
# class Song(models.Model):
#         snumber=models.IntegerField()
# def __str__(self):
#         return self.snumber
#
class Appli(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    Father = models.CharField(max_length=50)
    Mother = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    DateBirth = models.DateField()
    Category = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=50)
    Disability = models.CharField(max_length=50)
    AddressLine1 = models.CharField(max_length=50)
    AddressLine2 = models.CharField(max_length=50)
    AddressLine3 = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    Pin = models.IntegerField()
    Highest_Educational_Qualification = models.CharField(max_length=150)
    YearOfPassing = models.IntegerField()
    Aadhar_Card_Number = models.IntegerField()
    Upload_Photo = models.ImageField(upload_to='shop/image')
    # pic = models.FileField(upload_to='media/')
    Upload_Signature = models.ImageField(upload_to='shop/image')
    Left_Hand_Thumb_Impression = models.ImageField(upload_to='shop/image')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Appli"


class contactus(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    Gmail = models.CharField(max_length=50)
    number = models.IntegerField()
    message = models.CharField(max_length=250)

    class Meta:
        db_table = "contactus"


class pay(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    Fathername = models.CharField(max_length=40)
    number = models.IntegerField()
    course = models.CharField(max_length=40)
    gmail = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)

    class Meta:
        db_table = "payment"


class Provisional(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    sno = models.CharField(max_length=50)
    file = models.FileField()

    class Meta:
        db_table = "Provisional"


class InqueryForm(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    gmail = models.CharField(max_length=50)
    number = models.IntegerField()
    course = models.CharField(max_length=50)
    message = models.CharField(max_length=50)

    class Meta:
        db_table = "InqueryForm"


class Image(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='myimage')


class about_s(models.Model):
    sid = models.AutoField(primary_key=True)
    speech = models.CharField(max_length=1250)
    class Meta:
        db_table = "about_m"
    def __str__(self):
        return self.speech

#
# class Reviewdata(models.Model):
#     sid = models.AutoField(primary_key=True)
#     nm = models.CharField(max_length=50, default='', blank=True,null=False)
#     m = models.CharField(max_length=1250, default='', blank=True,null=False)
#     class Meta:
#         db_table = "review"
#     def __str__(self):
#         return self.nm

class comment(models.Model):
    sid = models.AutoField(primary_key=True)
    comment_name = models.CharField(max_length=50)
    comment_message = models.CharField(max_length=700)
    class Meta:
        db_table = "comment"
    def __str__(self):
        return self.comment_name
