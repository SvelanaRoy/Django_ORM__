from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    id  = models.IntegerField(primary_key = True)
    model  = models.CharField(max_length=20,null=True)
    year  = models.IntegerField(null=True)
    color  = models.CharField(max_length=15,null=True)
    mileage = models.IntegerField(null=True)
    volume = models.DecimalField (max_digits = 5, decimal_places  = 1,null=True)
    body_type = models.CharField(max_length=15, choices = BODY_TYPE_CHOICES,null=True)
    drive_unit = models.CharField(max_length=15, choices = DRIVE_UNIT_CHOICES,null=True)
    gearbox  = models.CharField(max_length=15, choices = GEARBOX_CHOICES,null=True)
    fuel_type = models.CharField(max_length=15, choices = FUEL_TYPE_CHOICES,null=True)
    price  = models.DecimalField (max_digits = 10, decimal_places  = 2,null=True)
    image = models.ImageField (upload_to="products",null=True)

    def __str__(self):
        return f'{self.model} {self.year}'
    
class Sale(models.Model):
    id  = models.IntegerField(primary_key = True)
    client = models.ForeignKey (Client, on_delete = models.CASCADE)
    car = models.ForeignKey (Car, on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} {self.car} {self.created_at}'