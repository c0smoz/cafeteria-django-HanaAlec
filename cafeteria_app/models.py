from django.db import models
from django.core.validators import MinValueValidator

class User(models.Model):
    ROLE_CHOICES = [
        ('student', 'Étudiant'),
        ('seller', 'Vendeur'),
        ('cashier', 'Responsable de caisse'),
        ('teacher', 'Professeur'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    credit = models.FloatField(default=0, validators=[MinValueValidator(0)])
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    is_subscriber = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"
    
    @property
    def shop_history(self):
        """Retourne l'historique des transactions de l'utilisateur"""
        return self.transactions.all().select_related('product').order_by('-date')
    
    def get_product_price(self, product):
        """Calcule le prix du produit avec réduction si applicable"""
        base_price = product.price
        
        # Appliquer réduction de 0.50€ si cotisant et produit éligible
        if self.is_subscriber and product.has_subscriber_discount:
            return max(0, base_price - 0.50)
        
        return base_price
    
    class Meta:
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    available = models.BooleanField(default=True)
    has_subscriber_discount = models.BooleanField(
        default=False,
        help_text="Appliquer une réduction de 0.50€ pour les étudiants cotisants"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.name} - {self.product.name} ({self.date.date()})"
    
    class Meta:
        ordering = ['-date']
        unique_together = ('user', 'product', 'date')