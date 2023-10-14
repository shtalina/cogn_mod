from django.db import models


class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    fio = models.TextField()
    spec = models.TextField(blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    tel = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    spec_napravl = models.TextField(blank=True, null=True)
    forma = models.CharField(max_length=20, blank=True, null=True)
    sroki = models.TextField(blank=True, null=True)
    facultet = models.TextField(blank=True, null=True)
    kafedra = models.CharField(max_length=50, blank=True, null=True)
    rukov = models.CharField(max_length=50, blank=True, null=True)
    tema = models.CharField(max_length=100, blank=True, null=True)
    gruppa = models.IntegerField(blank=True, null=True)
    edecanat_id = models.IntegerField(unique=True, blank=True, null=True)
    fac_id = models.IntegerField(blank=True, null=True)
    course = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class Faculties(models.Model):
    fak_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    ims = models.CharField(db_column='IMS', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'faculties'


class Files(models.Model):
    fio = models.CharField(max_length=50, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    owner = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    id = models.IntegerField(db_column='stud_id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'files'


class Groups(models.Model):
    fak_id = models.IntegerField()
    gruppa = models.CharField(max_length=255)
    course = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups'


class Marks(models.Model):

    student_id = models.IntegerField(db_column='STUDENT_ID', blank=True, null=True)  # Field name made lowercase.
    student_fio = models.CharField(db_column='STUDENT_FIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gruppa = models.IntegerField(db_column='GRUPPA', blank=True, null=True)  # Field name made lowercase.
    discipline_name = models.TextField(db_column='DISCIPLINE_NAME', blank=True, null=True)  # Field name made lowercase.
    mark_name = models.CharField(max_length=20, blank=True, null=True)
    is_examen = models.IntegerField(db_column='IS_EXAMEN', blank=True, null=True)  # Field name made lowercase.
    number_of_semester = models.IntegerField(db_column='NUMBER_OF_SEMESTER', blank=True, null=True)  # Field name made lowercase.
    mark = models.IntegerField(blank=True, null=True)
    coddis = models.CharField(db_column='CODDIS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='stud_id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'marks'


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    metric1 = models.PositiveIntegerField()
    metric2 = models.PositiveIntegerField()
    metric3 = models.PositiveIntegerField()
    metric4 = models.PositiveIntegerField()
    metric5 = models.PositiveIntegerField()
    intro_extro = models.PositiveIntegerField()
    adapt = models.PositiveIntegerField()
    social = models.PositiveIntegerField()
    refl = models.PositiveIntegerField()
    motivation = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cogn_student'

class Comp(models.Model):
    id = models.IntegerField(primary_key=True)
    kod_plana = models.PositiveIntegerField()
    stud_plan = models.PositiveIntegerField()
    comp_name = models.PositiveIntegerField()
    shifr_name = models.PositiveIntegerField()
    order = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'comp'