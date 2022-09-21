from rest_framework import serializers

from .models import Product, downloadexcel,reporttoday,agent,chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = chat
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DownloadExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = downloadexcel
        fields = '__all__'

class ReportTodaySerializer(serializers.ModelSerializer):
    class Meta:
        model = reporttoday
        fields = '__all__'
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = agent
        fields = '__all__'