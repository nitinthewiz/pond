from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from pond.models import Reflection
from pond.forms import ReflectionForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def index(request):
	context = RequestContext(request)
	return render_to_response('pond/index.html', {}, context)

@login_required
def add_reflection(request):
	context = RequestContext(request)
	if request.method == "POST":
		reflection_form = ReflectionForm(request.POST)
		if reflection_form.is_valid():
			reflection = reflection_form.save(commit=False)
			reflection.date = timezone.now()
			u = User.objects.get(username=request.user)
			reflection.user = u
			reflection.save()
			return HttpResponseRedirect("/pond/home/")
		else:
			print reflection_form.errors
	else:
		reflection_form = ReflectionForm()
	return render_to_response("pond/add_reflection.html", {'reflection_form': reflection_form}, context)

@login_required
def home(request):
	context = RequestContext(request)
	u = User.objects.get(username=request.user)
	reflections = Reflection.objects.filter(user=u)
	context_dict = {'user': u, 'reflections': reflections}
	return render_to_response("pond/home.html", context_dict, context)

def register(request):
	context = RequestContext(request)
	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			return HttpResponseRedirect("/pond/login/")
		else:
			print user_form.errors
	else:
		user_form = UserForm()
	return render_to_response("pond/register.html", {"user_form": user_form}, context)

def user_login(request):
	context = RequestContext(request)
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect("/pond/home/")
			else:
				return HttpResponse("Your account has been disabled.")
		else:
			return HttpResponse("Invalid login information supplied.")
	return render_to_response("pond/login.html", {}, context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect("/pond/")



