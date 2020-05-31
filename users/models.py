import random
from django.contrib.auth.models import User, AbstractUser
from django.db import models


def gen_code():
	symbols = '1234567890'
	code = ''.join([random.choice(symbols) for i in range(6)])
	return code

# Create your models here.
class MyCustomUser(AbstractUser):

	code = models.CharField(max_length=6, default=gen_code, unique=True)
	points = models.PositiveIntegerField(default=0)

	def __str__(self):
		return str(self.code)






