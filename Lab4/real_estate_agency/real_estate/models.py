from django.db import models
from django.urls import reverse


class PropertyType(models.Model):
    type = models.CharField(max_length=50, verbose_name="Тип")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_slug': self.slug})

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
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(verbose_name="Описание")
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, verbose_name="Тип недвижимости")
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name="Тип услуги")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации недвижимости")
    area = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Площадь")
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена")
    photo = models.ImageField(upload_to="images", verbose_name="Фото", default="images/default_home.png")
    purchased = models.BooleanField(verbose_name="Актуальность")

    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, verbose_name="Владелец")
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, verbose_name="Сотрудник")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('realty', kwargs={'realty_slug': self.slug})

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
        return str(self.last_name) + " " + str(self.first_name)

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
        return str(self.last_name) + " " + str(self.first_name)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Position(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название должности")
    description = models.TextField(verbose_name="Описание обязанностей")
    is_vacant = models.BooleanField(verbose_name="Статус")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class Employee(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=13, verbose_name="Номер телефона")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Должность")
    photo = models.ImageField(upload_to="images", verbose_name="Фото", default="default_avatar.png")
    email = models.EmailField(max_length=200, verbose_name="Адрес электронной почты", default="fff@gmail.com")

    def __str__(self):
        return str(self.last_name) + " " + str(self.first_name)

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


#Lab1

class Article (models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="images", verbose_name="Изображение", default="logo.png")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Question(models.Model):
    description = models.TextField(verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации вопроса")

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class PromotionalCode(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    start_date = models.DateTimeField( verbose_name="Дата начала действия промокода")
    end_date = models.DateTimeField(verbose_name="Дата окончания действия промокода")
    is_active = models.BooleanField(verbose_name="Активен", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'


class Comment(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя пользователя")
    comment = models.TextField(verbose_name="Отзыв")
    grade = models.IntegerField(verbose_name="Оценка")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата написания отзыва")

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'