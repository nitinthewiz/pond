import os
from django.utils import timezone

def populate():
	u1 = add_user("spatel7", "123")

	add_reflection(u1, "Sometimes I feel like my life is just a blur.")
	add_reflection(u1, "Lessons are meant to help us out. The harder the better.")

	for r in Reflection.objects.all():
		print '- {0}'.format(str(r))

def add_user(username, password):
	u = User.objects.get_or_create(username=username)[0]
	u.set_password(password)
	u.save()
	return u

def add_reflection(user, content):
	r = Reflection.objects.get_or_create(user=user, content=content, date=timezone.now())[0]
	return r

if __name__ == "__main__":
	print "Staring Pond population"
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pondapp.settings')
	from pond.models import Reflection
	from django.contrib.auth.models import User
	populate()