from django.db import models

class Degree(models.TextChoices):
    BACHELOR = 'BA', 'Бакалавр'
    MASTER = 'MA', 'Магістр'
    SPECIALIST = 'SP', 'Спеціаліст'
    CANDIDATE = 'CAND', 'Кандидат наук'
    DOCTOR = 'DR', 'Доктор наук'
    PHD = 'PhD', 'Доктор філософії'

class TutorPosition(models.TextChoices):
    PROFESSOR = 'PROF', 'Професор'
    ASSOCIATE_PROFESSOR = 'DOC', 'Доцент'
    SENIOR_LECTURER = 'SLEC', 'Старший викладач'
    LECTURER_ASSISTANT = 'LEC', 'Викладач та асистент'
    HEAD_OF_DEPARTAMENT = 'HEAD', 'Завідувач кафедри'
    DEAN = 'DEAN', 'Декан'
    RECTOR = 'RECT', 'Ректор'

class Department(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)

    @property
    def head(self):
        return self.tutors.filter(position=TutorPosition.HEAD_OF_DEPARTAMENT).first()

    def __str__(self):
        return self.name

class Tutor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=32, choices=Degree.choices)
    position = models.CharField(max_length=32, choices=TutorPosition.choices)
    departament = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='tutors')

    def __str__(self):
        return f'{self.degree} {self.name}'.capitalize()

class Program(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    coordinator = models.ForeignKey(Tutor, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')

    def __str__(self):
        return f'{self.code} {self.name}'.capitalize()

class Subject(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name

class IndexPage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Index page"

class ContactEmail(models.Model):
    id = models.AutoField(primary_key=True)
    page = models.ForeignKey(
        IndexPage,
        on_delete=models.CASCADE,
        related_name="contacts",
    )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
