from rest_framework import serializers
from stream.models import Stream, Show, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'


class ShowSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only = True)
    # reviews = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='review-details'
    # )
    
    class Meta:
        model = Show
        fields = '__all__'

class StreamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    stream_name = serializers.CharField(max_length=100)
    stream_desc = serializers.CharField(max_length=100)
    website= serializers.URLField(max_length=1000)
    shows = ShowSerializer(many=True, read_only=True)


    def create(self, validated_data):
        return Stream.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.stream_name = validated_data.get('stream_name', instance.stream_name)
        instance.stream_desc = validated_data.get('stream_desc', instance.stream_desc)
        instance.save()
        return instance
    
