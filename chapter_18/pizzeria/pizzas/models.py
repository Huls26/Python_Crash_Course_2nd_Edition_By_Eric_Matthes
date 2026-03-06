from django.db import models

class Pizza(models.Model):
    """A topic the user is learning about."""
    name = models.CharField(max_length=200)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.name