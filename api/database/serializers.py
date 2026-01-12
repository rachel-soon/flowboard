from rest_framework import serializers
from .models import Whiteboard


class WhiteboardSerializer(serializers.ModelSerializer):
    """
    Serializer for the Whiteboard model.
    Automatically handles all fields including created_at and updated_at.
    """

    class Meta:
        model = Whiteboard
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
