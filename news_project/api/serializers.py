from rest_framework import serializers

from news.models import News
from utils.serializers import TaggitSerializer, TagListSerializerField


class NewsSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = News
        fields = ['id', 'title', 'text', 'image', 'tags']

    def _pop_tags(self, validated_data):
        to_be_tagged = {}

        for key in self.fields.keys():
            field = self.fields[key]
            if isinstance(field, TagListSerializerField):
                if key in validated_data:
                    to_be_tagged[key] = validated_data.pop(key)
        return to_be_tagged, validated_data

    def _save_tags(self, tag_object, tags):
        for key in tags.keys():
            tag_values = tags.get(key).split(', ')
            getattr(tag_object, key).set(tag_values)
        return tag_object

    def create(self, validated_data):
        to_be_tagged, validated_data = self._pop_tags(validated_data)
        tag_object = super().create(validated_data)
        return self._save_tags(tag_object, to_be_tagged)

    def update(self, instance, validated_data):
        to_be_tagged, validated_data = self._pop_tags(validated_data)
        tag_object = super().update(instance, validated_data)
        return self._save_tags(tag_object, to_be_tagged)
