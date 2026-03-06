from django.db import models

class Pizza(models.Model):
    """A topic the user is learning about."""
    name = models.CharField(max_length=200)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Topping(models.Model):
    """Something specific learned about a topic."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.pizza.name}: {self.name[:50]}..."
        
        return f"{self.pizza.name}: {self.name}"