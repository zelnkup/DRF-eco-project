from django.db import models


def image_folder(instanse, filename):
	filename = instanse.slug + '.' + filename.split('.')[1]
	return '{0}/{1}'.format(instanse.slug, filename)


class Product(models.Model):
	name = models.CharField(max_length=200, db_index=True, verbose_name="Name")
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to=image_folder, blank=True, verbose_name="Product image")
	description = models.TextField(blank=True, verbose_name="Description")
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
	available = models.BooleanField(default=True, verbose_name="Available")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['name']
		index_together = [
			['id', 'slug']
		]

	def __str__(self):
		return self.name