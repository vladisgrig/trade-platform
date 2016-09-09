from django.shortcuts import render, get_object_or_404
from .models import Category, Goods, GoodsImage
from .forms import EmailForm
from django.shortcuts import redirect
import smtplib

EMAIL = 'Enter here your login'
PASSWORD = 'Enter here your password'

MANAGER_EMAIL = 'borodaa@gmail.com'

def send_confirmation(form):
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.starttls()
	smtpObj.login(EMAIL, PASSWORD)
	smtpObj.sendmail(EMAIL, form.from_email, 'We have received your message.\nWe will contact you within 24 hours.')
	smtpObj.quit()

def send_to_manager(form):
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.starttls()
	smtpObj.login(EMAIL, PASSWORD)
	msg = form.from_name + " " + form.from_email + " " + form.subject + " " + form.message
	smtpObj.sendmail(EMAIL, MANAGER_EMAIL, msg)
	smtpObj.quit()

def category_list(request):
	categories = Category.objects.all()
	return render(request, 'trade_platform/index.html', {'categories': categories})

def get_image_list(good):
	images = GoodsImage.objects.filter(goods = good)
	image_list = [image for image in images]
	return image_list

def goods_list(request, category_name):
	category_name = category_name.capitalize()
	our_category = Category.objects.get(name=category_name)
	goods = Goods.objects.filter(category=our_category)
	goods_list =[]
	for good in goods:
		goods_list.append([good, get_image_list(good)])
	categories = Category.objects.all()
	return render(request, 'trade_platform/goods_list.html', {'goods': goods_list, 
		'category_name': category_name, 'categories': categories})

def catalog(request):
	goods = Goods.objects.all()
	goods_list =[]
	for good in goods:
		goods_list.append([good, get_image_list(good)])
	categories = Category.objects.all()
	return render(request, 'trade_platform/catalog.html', {'goods': goods_list, 'categories': categories})

def contacts(request):
	if request.method == "POST":
		form = EmailForm(request.POST)
		if form.is_valid():
			email_form = form.save()
			send_confirmation(email_form)
			send_to_manager(email_form)
			form = EmailForm()
			return render(request, 'trade_platform/contacts.html', {'form': form, 'result': 'Your email is send'})
	else:
		form = EmailForm()
		return render(request, 'trade_platform/contacts.html', {'form': form})
