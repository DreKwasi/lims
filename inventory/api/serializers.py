from rest_framework import serializers

from accounts.models import Facility
from inventory.models import Inventory, LogisticArea, Site


class LogisticAreaSerializer(serializers.ModelSerializer):
    site_id = serializers.SlugRelatedField(
        slug_field="facility_name",
        queryset=Site.objects.all(),
        required=False,
    )

    class Meta:
        model = LogisticArea
        fields = ["area_name", "area_description", "site_id"]


class SiteSerializer(serializers.ModelSerializer):
    areas = LogisticAreaSerializer(many=True)
    facility = serializers.SlugRelatedField(
        slug_field="facility_name",
        queryset=Facility.objects.all(),
        required=False,
    )

    class Meta:
        model = Site
        fields = ["facility", "created_date", "areas"]
