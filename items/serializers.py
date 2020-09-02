from rest_framework import serializers

from items.models import CompanyItem, BranchItem


class CompanyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyItem
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    item = CompanyItemSerializer()

    class Meta:
        model = BranchItem
        fields = "__all__"


class CreateItemSerializer(serializers.Serializer):
    sku = serializers.CharField(max_length=16, min_length=1, required=True)
    model = serializers.CharField(min_length=1, max_length=255, required=True)
    brand = serializers.UUIDField(required=True)
    cost = serializers.DecimalField(max_digits=12, decimal_places=2, required=True)
    price = serializers.DecimalField(max_digits=12, decimal_places=2, required=True)
    category = serializers.CharField(max_length=255, required=False)
    subcategory = serializers.CharField(max_length=255, required=False)
