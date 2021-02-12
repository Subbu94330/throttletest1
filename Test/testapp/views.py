from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PeriodSerializer, UserSerializer
from .models import Period, User
from rest_framework.response import Response


class PeriodViewSet(viewsets.ViewSet):

    def list(self, request):
        period = Period.objects.all()
        serializer = PeriodSerializer(period, many=True, context={"request": request})
        response_dict = {"ok":True, "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = PeriodSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            response_dict = {"error":False, "message": "Timings Saved Successfully"}
        except:
            response_dict = {"error":True, "message": "Error Occur while saving"}
        return Response(response_dict)
        

class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        member = User.objects.all()
        serializer = UserSerializer(member, many=True, context={"request": request})
        response_dict = {"ok": True, "members": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            data = request.data
            new_user = User.objects.create(id=data["id"], real_name=data["real_name"],tz=data['tz'])
            new_user.save()
            for per in data["period"]:
                period_obj = Period.objects.get(start_time=per["start_time"])
                new_user.period.add(period_obj)
            serializer = UserSerializer(new_user)
            serializer.is_valid()
            serializer.save()
            response_dict = {"error":False, "message": "Data Saved Successfully"}
        except:
            response_dict = {"error":True, "message": "Error in saving data"}
        return Response(response_dict)

