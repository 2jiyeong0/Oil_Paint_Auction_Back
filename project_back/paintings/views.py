from django.shortcuts import get_list_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from paintings.models import Painting, PaintStyle, TempImg
from paintings.serializers import StyleSerializer, PaintingCreateSerializer

from .styler import painting_styler


# Create your views here.
class PaintingStyleSelectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        styles = get_list_or_404(PaintStyle)
        serializer = StyleSerializer(styles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ImageUploadView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, style_num):
        print(request.user)
        temp_img = Painting()
        temp_img.image = request.FILES.get('image')
        temp_img.author_id = request.user.id
        temp_img.save()

        img_url = temp_img.image

        painting_styler(style_num, img_url)

        return Response({"message":"변환 완료"}, status=status.HTTP_200_OK)

class PaintingCreateView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PaintingCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, song_id=song_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)