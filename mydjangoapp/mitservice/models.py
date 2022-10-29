from django.db import models

"""
from tabnanny import verbose
from django.db.models import manager

class Objects_mr25(models.Model):
    object_mr25 = models.CharField('Объект', max_length=255)

    def __str__(self):
        return self.object_mr25

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

class System_mr25(models.Model):
    object_mr25 = models.ManyToManyField(Objects_mr25)
#    object_mr25 = models.ForeignKey(Objects_mr25, on_delete=models.CASCADE)
    system_type_mr25 = models.CharField('Система', max_length=255)
    #objects = manager.Manager()
    def __str__(self):
        return self.system_type_mr25

    class Meta:
        verbose_name = 'Система'
        verbose_name_plural = 'Системы'

class Signaling(models.Model):
#    object_mr25 = models.ForeignKey(Objects_mr25, on_delete=models.CASCADE)
    system_mr25 = models.ForeignKey(System_mr25, on_delete=models.CASCADE)
    
    device_mr25 = models.CharField('Оборудование', max_length=255)
    description_mr25 = models.CharField('Описание', max_length=255)
    login_mr25 = models.CharField('Пользователь', max_length=255)
    passwd_mr25 = models.CharField('Пароль', max_length=255)

#    def __str__(self):
#        return self.system_type_mr25

    class Meta:
        verbose_name = 'ОПС'
        verbose_name_plural = 'ОПС'

class Cctv(models.Model):
#    object_mr25 = models.ForeignKey(Objects_mr25, on_delete=models.CASCADE)
    system_mr25 = models.ForeignKey(System_mr25, on_delete=models.CASCADE)
    
    device_mr25 = models.CharField('Оборудование', max_length=255)
    description_mr25 = models.CharField('Описание', max_length=255)
    ipaddress_mr25 = models.CharField('IP - адрес', max_length=255)
    port_mr25 = models.CharField('Порт', max_length=255)
    login_mr25 = models.CharField('Пользователь', max_length=255)
    passwd_mr25 = models.CharField('Пароль', max_length=255)

    class Meta:
        verbose_name = 'СВН'
        verbose_name_plural = 'СВН'

class Accesscontrol(models.Model):
#    object_mr25 = models.ForeignKey(Objects_mr25, on_delete=models.CASCADE)
    system_mr25 = models.ForeignKey(System_mr25, on_delete=models.CASCADE)
    
    device_mr25 = models.CharField('Оборудование', max_length=255)
    description_mr25 = models.CharField('Описание', max_length=255)
    ipaddress_mr25 = models.CharField('IP - адрес', max_length=255)
    port_mr25 = models.CharField('Порт', max_length=255)
    login_mr25 = models.CharField('Пользователь', max_length=255)
    passwd_mr25 = models.CharField('Пароль', max_length=255)

    class Meta:
        verbose_name = 'СКУД'
        verbose_name_plural = 'СКУД'

"""