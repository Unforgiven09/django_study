from django.db import models


class Teachers(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=10, verbose_name='Телефон')
    date_of_birth = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподователи'


class Courses(models.Model):
    name = models.CharField(max_length=50, verbose_name='Курс')
    description = models.TextField(verbose_name='Описание курса')
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name='Препрдаватель')
    start = models.DateField(verbose_name='Начало курса')
    end = models.DateField(verbose_name='Конец курса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Students(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=10, verbose_name='Телефон')
    url = models.URLField(verbose_name='Соцсети', blank=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    courses = models.ManyToManyField(Courses, related_name='Name', verbose_name='Курсы')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


