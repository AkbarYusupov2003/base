from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class SecuredAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        print("Secured view accessed")
        res = {"worked": True}
        return Response(res)
