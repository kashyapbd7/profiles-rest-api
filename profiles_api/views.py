from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Testing API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Return a List of APIView features"""

        an_apiView = ['HTTP function is used to get functionalities like ',
        '1. GET',
        '2. POST',
        '3. PUT',
        '4. PATCH',
        '5. DELETE',
        ]

        return Response({'message': 'Hello World I am Learning Django',
                        'an_apiView': an_apiView})


    def post(self, request):
        """Testing POST API"""

        serializer = self.serializer_class (data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Testing the patch"""
        return Response({'method':'PUT'})

    def patch(self, request):
        """Testing the patch"""
        return Response({'method':'PATCH'})

    def delete(self, request):
        """Testing the patch"""
        return Response({'method':'DELETE'})
