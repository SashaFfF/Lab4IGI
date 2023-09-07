from django.db import models
from django.urls import reverse


class PropertyType(models.Model):
    type = models.CharField(max_length=50, verbose_name="Тип")

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_id': self.pk})

    class Meta:
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Типы недвижимости'


class ServiceType(models.Model):
    type = models.CharField(max_length=50, verbose_name="Вид")

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Вид услуги'
        verbose_name_plural = 'Виды услуг'


class RealEstate(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    #slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(verbose_name="Описание")
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, verbose_name="Тип недвижимости")
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name="Тип услуги")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации недвижимости")
    area = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Площадь")
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена")
    purchased = models.BooleanField(verbose_name="Актуальность")

    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, verbose_name="Владелец")
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, verbose_name="Сотрудник")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('realty', kwargs={'realty_id': self.pk})

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'
        ordering = ['title', 'price']


class Owner(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=13, verbose_name="Номер телефона")
    passport_details = models.CharField(max_length=100, verbose_name="Паспортные данные")

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'


class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=13, verbose_name="Номер телефона")
    passport_details = models.CharField(max_length=100, verbose_name="Паспортные данные")
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Employee(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=13, verbose_name="Номер телефона")
    position = models.CharField(max_length=100, verbose_name="Должность")

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Deal(models.Model):
    real_estate = models.OneToOneField(RealEstate, on_delete=models.CASCADE, verbose_name="Недвижимость")
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name="Продавец недвижимости")
    buyer = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Покупатель")
    agent = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата сделки")

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'