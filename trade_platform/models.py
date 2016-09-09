from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name

class Goods(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	currency = models.CharField(max_length=3)
	supplier = models.CharField(max_length=100)
	category = models.ForeignKey(Category)

	def __str__(self):
		return self.name

class GoodsImage(models.Model):
	goods = models.ForeignKey(Goods)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.goods.name + ' image ' + str(self.pk)


class Email(models.Model):
	subject = models.CharField(max_length=100, verbose_name = u'Subject')
	message = models.TextField(verbose_name = u'Text')
	from_email = models.EmailField(verbose_name = u'Your email')
	from_name = models.CharField(max_length=100, verbose_name = u'Your name')