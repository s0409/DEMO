from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = (
        ('0', 'High'),
        ('1', 'Medium'),
        ('2', 'Low'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    owner_email = models.EmailField(max_length=50)
    creator_email = models.EmailField(max_length=50)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='1')
    status = models.CharField(max_length=1, default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    class Meta:
        db_table = 'task_tbl'
