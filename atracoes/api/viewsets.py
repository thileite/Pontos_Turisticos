from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracoes
from .serializers import AtracaoSerializer

class AtracaoViewSet(ModelViewSet):
    queryset = Atracoes.objects.all()
    serializer_class = AtracaoSerializer
    filter_fields = ('nome', 'descricao')

