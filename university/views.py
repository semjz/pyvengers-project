from django.http import HttpResponse
from .tasks import test_func
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsItManager
from .models import Student
from .serializers import CreateStudentSerializer, UpdateStudentSerializer
from django_filters import rest_framework as filters
import university.filtersets as filtersets


def test(request):
    test_func.delay()
    return HttpResponse('Done')


class ITManagerStudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = (IsAuthenticated, IsItManager)
    http_method_names = ["get", "post", "put", "patch", "delete"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = filtersets.StudentFilterSet

    def perform_destroy(self, instance):
        instance.user.delete()

    def get_serializer_class(self):
        if self.action == "partial_update" or self.action == "update":
            return UpdateStudentSerializer
        else:
            return CreateStudentSerializer






