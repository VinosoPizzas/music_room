from rest_framework import serializers
from .models import Room

# verifica as informações de cada sala (room) e deve ser utilizada para verificar se as informações são válidas
class RoomSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')

# serializer para criar a room
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')

# serializer para atualizar as infos da room
class UpdateRoomSerializer(serializers.ModelSerializer):
    """ 
    por conta do modelo Room gerar todas o data como unique, 
    esse código não vai funcionar poís ele n poderá 
    atualizar, pois o código interpretará como se fosse 
    criar uma outra sala com o mesmo código, essa linha remove essa 
    limitação para esse serializador
    """
    code = serializers.CharField(validators=[]) 
    

    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip', 'code')