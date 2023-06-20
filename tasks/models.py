from django.db import models

class Brigades(models.Model):
    id_brigade = models.IntegerField(primary_key=True)
    name_of_brigade = models.CharField(max_length=45, blank=True, null=True)
    brigade_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brigades'


class Genders(models.Model):
    id_gender = models.IntegerField(primary_key=True)
    name_of_gender = models.CharField(max_length=45, blank=True, null=True)
    gender_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genders'


class Highways(models.Model):
    id_highway = models.IntegerField(primary_key=True)
    name_of_highway = models.CharField(max_length=45, blank=True, null=True)
    highway_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'highways'


class Objects(models.Model):
    id_object = models.IntegerField(primary_key=True)
    name_of_object = models.CharField(max_length=45, blank=True, null=True)
    object_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objects'


class Place(models.Model):
    id_place = models.AutoField(primary_key=True)
    id_town = models.ForeignKey('Towns', models.DO_NOTHING, db_column='id_town', blank=True, null=True)
    place_discription = models.CharField(max_length=45, blank=True, null=True)
    place_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place'


class Positions(models.Model):
    id_position = models.IntegerField(primary_key=True)
    name_of_position = models.CharField(max_length=45, blank=True, null=True)
    position_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'positions'


class Roles(models.Model):
    id_role = models.IntegerField(primary_key=True)
    name_of_role = models.CharField(max_length=45, blank=True, null=True)
    roles_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Streets(models.Model):
    id_street = models.IntegerField(primary_key=True)
    name_of_street = models.CharField(max_length=30)
    street_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'streets'


class SubTypeTasks(models.Model):
    id_sub_type_task = models.IntegerField(primary_key=True)
    sub_type_task_name = models.CharField(max_length=15, blank=True, null=True)
    sub_type_task_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_type_tasks'


class Tasks(models.Model):
    id_task = models.AutoField(primary_key=True)
    id_type_task = models.ForeignKey('TypeTask', models.DO_NOTHING, db_column='id_type_task', blank=True, null=True)
    id_object = models.ForeignKey(Objects, models.DO_NOTHING, db_column='id_object', blank=True, null=True)
    id_place = models.ForeignKey(Place, models.DO_NOTHING, db_column='id_place', blank=True, null=True)
    id_brigade = models.ForeignKey(Brigades, models.DO_NOTHING, db_column='id_brigade', blank=True, null=True)
    date_time_begin = models.DateField(blank=True, null=True)
    date_time_end = models.DateField(blank=True, null=True)
    task_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'


class Towns(models.Model):
    id_town = models.IntegerField(primary_key=True)
    name_of_town = models.CharField(max_length=30)
    town_status = models.IntegerField()
    id_street = models.ForeignKey(Streets, models.DO_NOTHING, db_column='id_street')
    id_highway = models.ForeignKey(Highways, models.DO_NOTHING, db_column='id_highway')

    class Meta:
        managed = False
        db_table = 'towns'


class TypeTask(models.Model):
    id_type_task = models.AutoField(primary_key=True)  # The composite primary key (id_type_task, id_sub_type_task) found, that is not supported. The first column is selected.
    id_sub_type_task = models.IntegerField()
    name_type_task = models.CharField(max_length=45, blank=True, null=True)
    type_task_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_task'
        unique_together = (('id_type_task', 'id_sub_type_task'),)


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    id_role = models.ForeignKey(Roles, models.DO_NOTHING, db_column='id_role')
    id_gender = models.ForeignKey(Genders, models.DO_NOTHING, db_column='id_gender')
    date_of_bers = models.DateField()
    second_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    telephone = models.CharField(max_length=25)
    e_mail = models.CharField(db_column='e-mail', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    photo = models.TextField(blank=True, null=True)
    login = models.CharField(unique=True, max_length=25)
    password = models.CharField(max_length=25)
    users_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class Workers(models.Model):
    id_worker = models.IntegerField(primary_key=True)
    id_position = models.ForeignKey(Positions, models.DO_NOTHING, db_column='id_position')
    id_gender = models.ForeignKey(Genders, models.DO_NOTHING, db_column='id_gender')
    id_brigade = models.ForeignKey(Brigades, models.DO_NOTHING, db_column='id_brigade')
    date_of_bers = models.DateField(blank=True, null=True)
    second_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    telephon = models.CharField(max_length=15)
    e_mail = models.CharField(db_column='e-mail', max_length=25, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    photo = models.TextField(blank=True, null=True)
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    worker_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'workers'
