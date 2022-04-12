from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Urgency(models.Model):
	urgency_type = models.CharField(max_length=255,unique=True,blank=True,null=True)
	weight = models.DecimalField(decimal_places=2, max_digits=12)

	def __str__(self):
		return self.urgency_type


class Subject(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Order(models.Model):
	HIGH_SCHOOL = "High School"
	BACHELORS = "Bachelors"
	MASTERS = "Masters"
	PHD = "PHD"
	SINGLE_SPACING = "Single spacing"
	DOUBLE_SPACING = "Double spacing"
	PENDING = "Pending"
	IN_PROGRESS = "In progress"
	COMPLETED = "Completed"

	EDUCATION_LEVELS = (
		(HIGH_SCHOOL,"High-School"),
		(BACHELORS,"Bachelor"),
		(MASTERS,"Master"),
		(PHD,"Doctorate"),
		)
	SPACING_CHOICE = (
		(SINGLE_SPACING,"Single-Spacing"),
		(DOUBLE_SPACING,"Double-Spacing"),
		)
	ORDER_STATUS = (
		(PENDING,"pending"),
		(IN_PROGRESS,"In-progress"),
		(COMPLETED,"completed"),
		)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	sources = models.IntegerField(blank=False)
	subject = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True, blank=True)
	details = models.TextField(blank=True,null=True)
	paper_format = models.CharField(max_length=255)
	urgency = models.ForeignKey(Urgency,on_delete=models.PROTECT)
	education_level = models.CharField(max_length=200,choices=EDUCATION_LEVELS)
	pages = models.IntegerField(blank=False)
	spacing = models.CharField(max_length=200,choices=SPACING_CHOICE)
	order_status = models.CharField(max_length=200,choices=ORDER_STATUS)

	def __str__(self):
		return self.id

	@property
	def get_order_total(self):
		return self.pages*8*self.urgency.weight
	

class MediaFiles(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='order_attachments')
	file = models.FileField(upload_to='files')