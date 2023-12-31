import factory
from factory.django import DjangoModelFactory

from management.models import *
from utils.choices import *
from authentication.factories import StudentUserFactory, AssistantUserFactory, ItManagerUserFactory, \
    ProfessorUserFactory


class FacultyFactory(DjangoModelFactory):
    class Meta:
        model = Faculty

    name = factory.Faker("name")


class MajorFactory(DjangoModelFactory):
    class Meta:
        model = Major

    name = factory.Faker("name")
    units = 100
    stage = factory.Iterator([choice[0] for choice in STAGE_CHOICES])
    school = factory.SubFactory(FacultyFactory)

    @factory.post_generation
    def courses(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.courses.add(*extracted)


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    user = factory.SubFactory(StudentUserFactory, student=None)
    school = factory.SubFactory(FacultyFactory)
    major = factory.SubFactory(MajorFactory, school=factory.SelfAttribute('..school'))
    entrance_year = factory.Faker("year")
    entrance_term = factory.Iterator([choice[0] for choice in ENTRANCE_TERM_CHOICES])
    military_status = factory.Iterator([choice[0] for choice in MILITARY_STATUS_CHOICES])

    @factory.post_generation
    def courses(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.courses.add(*extracted)


class AssistantFactory(DjangoModelFactory):
    class Meta:
        model = Assistant

    user = factory.SubFactory(AssistantUserFactory, assistant=None)
    school = factory.SubFactory(FacultyFactory)
    major = factory.SubFactory(MajorFactory)


class ITManagerFactory(DjangoModelFactory):
    class Meta:
        model = ITManager

    user = factory.SubFactory(ItManagerUserFactory)


class ProfessorFactory(DjangoModelFactory):
    class Meta:
        model = Professor

    user = factory.SubFactory(ProfessorUserFactory)
    school = factory.SubFactory(FacultyFactory)
    major = factory.SubFactory(MajorFactory)


