from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Testing API View"""

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