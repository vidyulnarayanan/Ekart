from django.db import models

# Model for product
class product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    SIZE_S = 'S'
    SIZE_M = 'M'
    SIZE_L = 'L'
    SIZE_XL = 'XL'
    SIZE_CHOICES = [
        (SIZE_S, 'Small'),
        (SIZE_M, 'Medium'),
        (SIZE_L, 'Large'),
        (SIZE_XL, 'Extra Large'),
    ]
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default=SIZE_M)
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
