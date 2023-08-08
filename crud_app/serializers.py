from rest_framework import serializers
from crud_app.models import Label

class labelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'

