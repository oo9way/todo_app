from django.db import models

class Todo(models.Model):
    STATUS_CHOICES = [
        ("new", "Yangi"),
        ("in_process", "Jarayonda"),
        ("done", "Bajarildi"),
        ("canceled", "Bekor qilindi"),
    ]
    name = models.CharField("Ish nomi", max_length=255)
    description = models.TextField("Tavsif")
    status = models.CharField("Holati", choices=STATUS_CHOICES, max_length=10)
