from rest_framework import serializers

from .models import Workspace, Location, ResponsePlan, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'country_short_code', 'long_name')


class WorkspaceSerializer(serializers.ModelSerializer):

    countries = CountrySerializer(many=True)

    class Meta:
        model = Workspace
        fields = ('id', 'title', 'workspace_code', 'countries',
                  'business_area_code')


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'title', 'latitude', 'longitude', 'p_code')


class ShortLocationSerializer(serializers.ModelSerializer):

    id = serializers.SerializerMethodField()
    title = serializers.CharField(read_only=True)

    class Meta:
        model = Location
        fields = ('id', 'title')

    def get_id(self, obj):
        return str(obj.id)


class IdLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', )


class ChildrenLocationSerializer(serializers.ModelSerializer):
    """
    Endpoint for drop down meny on PD list filterset - location.
    """
    id = serializers.SerializerMethodField()

    class Meta:
        model = Workspace
        fields = ('id', 'title')

    def get_id(self, obj):
        return str(obj.id)


class ResponsePlanSerializer(serializers.ModelSerializer):

    clusters = serializers.SerializerMethodField()

    class Meta:
        model = ResponsePlan
        fields = (
            'id',
            'title',
            'plan_type',
            'start',
            'end',
            'workspace',
            'documents',
            'clusters'
        )

    def get_clusters(self, obj):
        from cluster.serializers import ClusterSimpleSerializer
        return ClusterSimpleSerializer(obj.clusters.all(), many=True).data
