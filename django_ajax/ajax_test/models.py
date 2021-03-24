from django.db import models


class FileUpload(models.Model):

    UPLOADED = 1
    WORKING = 2
    SUCCESS = 3
    ERROR = 4
    STATUS_CHOICES = (
        (UPLOADED, 'Загружено'),
        (WORKING, 'Обрабатывается'),
        (SUCCESS, 'Завершено'),
        (ERROR, 'Ошибка')
    )

    file = models.FileField()
    status = models.IntegerField(
        "Состояние файла",
        null=True,
        blank=True,
        default = UPLOADED,
        choices = STATUS_CHOICES
    )