from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Order, MediaFiles, Subject, Urgency


class MediaFilesSerializers(serializers.Serializer):
	class Meta:
		model = MediaFiles
		fields = ['id','order','file']
		extra_kwargs = {
		'order': {'required': False}
		}

class OrderSerializer(serializers.ModelSerializer):
	files = MediaFilesSerializers(many=True, required=False)
	
	class Meta:
		model = Order
		fields = ['id','files','sources','user','subject','details','paper_format','urgency','education_level','pages','spacing','order_status']
		extra_kwargs = {
		'user': {'required': False}
		}

	def create(self, validated_data):
		# print("validated_data",validated_data)
		user = self.context['request'].user
		validated_data['user'] = user
		order = Order.objects.create(**validated_data)
		try:
			files_data = dict((self.context['request'].FILES).lists()).get('files',None)
			for file in files_data:
				MediaFiles.objects.create(order=order,file=file)
		except:
			MediaFiles.objects.create(order=order)
		return order

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = '__all__'


class UrgencySerializer(serializers.ModelSerializer):
	class Meta:
		model = Urgency
		fields = ['urgency_type',]