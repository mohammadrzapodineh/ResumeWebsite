from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer  
from rest_framework.response import Response
from Protfillo.models import Portfillo, Category
from Api.serializers import ProtfilloSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView


class PortfilloListApiView(ListAPIView):
    queryset = Portfillo.objects.all()
    serializer_class = ProtfilloSerializer


@api_view(['GET'])
@renderer_classes([JSONRenderer, TemplateHTMLRenderer])
def portfillo_by_category_list(request, category_id):
    '''
    A View That can return Json or TemplateHtmlRender of the users asked
    '''
    category = get_object_or_404(Category, id=category_id)
    portfilloes = category.c_portfillo.all()

    if request.accepted_renderer.format == 'html':
        data = {
            'portfillos': portfilloes
        }
        return Response(data, template_name='shared/component/portfillo/portfillo_component_list.html')
    
    # Json Respone 
    seralizer = ProtfilloSerializer(portfilloes, many=True)
    return Response(data=seralizer.data, status=status.HTTP_200_OK)