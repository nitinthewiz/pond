from django.db import models
from django.contrib.auth.models import User

class Reflection(models.Model):
	user = models.ForeignKey(User)
	content = models.TextField()
	date = models.DateTimeField()

	def __unicode__(self):
		return "A reflection made on " + str(self.date)