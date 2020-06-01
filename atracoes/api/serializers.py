from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracoes

class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracoes
        fields = (
            'id', 'nome', 'descricao', 'horario_func', 'idade_min', 'foto')