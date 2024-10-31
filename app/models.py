# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BurnEvent(models.Model):
    transaction_hash = models.CharField()
    pool_address = models.CharField()
    block_number = models.IntegerField()
    owner = models.CharField()
    tick_lower = models.IntegerField()
    tick_upper = models.IntegerField()
    amount = models.CharField()
    amount0 = models.CharField()
    amount1 = models.CharField()

    class Meta:
        managed = False
        db_table = 'burn_event'


class CollectEvent(models.Model):
    transaction_hash = models.CharField()
    pool_address = models.CharField()
    block_number = models.IntegerField()
    owner = models.CharField()
    recipient = models.CharField()
    tick_lower = models.IntegerField()
    tick_upper = models.IntegerField()
    amount0 = models.CharField()
    amount1 = models.CharField()

    class Meta:
        managed = False
        db_table = 'collect_event'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MintEvent(models.Model):
    transaction_hash = models.CharField()
    pool_address = models.CharField()
    block_number = models.IntegerField()
    sender = models.CharField()
    owner = models.CharField()
    tick_lower = models.IntegerField()
    tick_upper = models.IntegerField()
    amount = models.CharField()
    amount0 = models.CharField()
    amount1 = models.CharField()

    class Meta:
        managed = False
        db_table = 'mint_event'


class PoolData(models.Model):
    block_number = models.CharField()
    event_type = models.CharField()
    transaction_hash = models.CharField()

    class Meta:
        managed = False
        db_table = 'pool_data'


class SwapEvent(models.Model):
    transaction_hash = models.CharField()
    pool_address = models.CharField()
    block_number = models.IntegerField()
    sender = models.CharField()
    to = models.CharField()
    amount0 = models.CharField()
    amount1 = models.CharField()
    sqrt_price_x96 = models.CharField()
    liquidity = models.CharField()
    tick = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'swap_event'


class Timetable(models.Model):
    start = models.DateField(primary_key=True)
    end = models.DateField(blank=True, null=True)
    completed = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timetable'


class TokenPairs(models.Model):
    token0 = models.CharField()
    token1 = models.CharField()
    fee = models.IntegerField()
    pool = models.CharField()
    block_number = models.CharField()
    completed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'token_pairs'
