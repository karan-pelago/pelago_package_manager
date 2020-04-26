from django.shortcuts import render
from .models import Package
from rest_framework import generics
from .serializers import PackageSerializer
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import update_package_info
from .utilites import parse_package
class PackageListView(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

@api_view()
def StartUpdater(request):
    f =  open("cran/testdata/PACKAGES").read()
    i = 0
    for package in f.split("\n\n"):
        update_package_info.delay(package)

        i += 1
        if i == 1:
            break


    return Response({"message": "Hello, world!"})