from django.db import models

# Create your models here.
class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField(verbose_name='email address' , 
                            max_length=255,
                            unique=True,
    )
    phone=models.CharField(max_length=20,blank=True)
    USER_REGULAR = 'USER_REGULAR'
    USER_ADMIN = 'USER_ADMIN'
    USER_CHOICES = (
        (USER_REGULAR , 'REGULAR - Can\'t delete members'),
        (USER_ADMIN , 'ADMIN - Can delete members')
    )

    user_type = models.CharField(max_length=20 , choices=USER_CHOICES , blank=False , default=USER_REGULAR)
