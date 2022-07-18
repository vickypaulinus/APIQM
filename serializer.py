from rest_framework import serializer

class Linkserializer (serializer.ModelSerializer)
        class Meta:
                model = Link
                fields = "__all__"