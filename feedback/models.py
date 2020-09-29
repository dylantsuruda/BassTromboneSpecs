from django.db import models

# Create your models here.

class Feedback(models.Model):
    feedback = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        string = self.feedback[:100]
        if len(self.feedback) > 100:
            string += "..."
        return string

    class Meta:
        ordering = ['datetime']
        verbose_name_plural = 'feedback'
