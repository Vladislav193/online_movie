from rest_framework import serializers
from models import Video


class VideoSerializers(serializers.Serializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'video', 'posters']
