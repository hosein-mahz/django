from rest_framework import serializers
from .models        import Profile
# from profile.models import Profile  

class ProfileSerializer(serializers.ModelSerializer):
    # desk        = serializers.StringRelatedField(many=True)
    # Caffefile   = serializers.StringRelatedField(many=True)
    class Meta:
        model = Profile
        fields = [
            'name',
            'lastname',
            'username',
            'password',
            'email',
            'phone',
            'id'
        ]