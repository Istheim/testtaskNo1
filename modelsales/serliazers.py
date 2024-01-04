from rest_framework import serializers

from modelsales.models import NetworkElement


class ModelsalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkElement
        fields = '__all__'
        read_only_fields = ('debt',)
