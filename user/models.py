from django.db import models

# Create your models here.
class SysMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=64)
    path = models.CharField(max_length=255, blank=True, null=True)
    perms = models.CharField(max_length=255, blank=True, null=True)
    component = models.CharField(max_length=255, blank=True, null=True)     
    type = models.IntegerField()
    icon = models.CharField(max_length=32, blank=True, null=True)
    ordernum = models.IntegerField(db_column='orderNum', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)
    statu = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_menu'


class SysRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    code = models.CharField(unique=True, max_length=64)
    remark = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    statu = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysRoleMenu(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_id = models.BigIntegerField()
    menu_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'sys_role_menu'


class SysUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)       
    avatar = models.CharField(max_length=255, blank=True, null=True)        
    email = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    statu = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    role_id = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'sys_user_role'













