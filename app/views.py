from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.views import APIView
from app.models import URL
from app.serializers import URLSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample

class URLView(APIView):
    def get(self, request):
        urls = URL.objects.all().order_by('-created_at')
        serializer = URLSerializer(urls, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=URLSerializer,
        responses={201: URLSerializer},
        description="created a short url",
        examples=[
            OpenApiExample(
                name="Example Request",
                value={
                    'original_url':'https://google.com',
                },
                request_only=True

            )
        ]
    )
    def post(self, request):
        serializer = URLSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "success":"True",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)


@ensure_csrf_cookie
def home_view(request):
    return render(request, 'app/index.html')
