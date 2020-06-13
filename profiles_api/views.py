from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication



from profiles_api import models
from profiles_api import serializers
from profiles_api import permissions


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
            surName = serializer.validated_data.get('surName')
            age = serializer.validated_data.get('age')
            message = f'Hello {surName} { name} with age {age}'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """"Testing the put """
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Testing Patch"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Testing Delete"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Testing ViewSet"""

    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """Creating the List function"""
        an_viewSet = ['HTTP function is used to get functionalities like ',
        '1. LIST',
        '2. CREATE',
        '3. RETRIVE',
        '4. UPDATE',
        '5. PARTIAL UPDATE',]

        return Response({'message': 'Hello I am Learning Viewset', 'an_viewSet':an_viewSet})

    def create(self, request):
        """"Creating the object"""

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retriving the Object"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Updating the object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Updating the Object partially"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Deleting the object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating and updating user profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
