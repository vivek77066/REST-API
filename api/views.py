from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmpoyeeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    @action(detail=True,methods=['get'])
    def employee(self,request,pk=None):
        company=Company.objects.get(pk=pk)
        emp=Employee.objects.filter(company=company)
        emp_serilizer=EmpoyeeeSerializer(emp,many=True,context={'request':request})
        return Response(emp_serilizer.data)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmpoyeeeSerializer