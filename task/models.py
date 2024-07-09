from django.db import models
from category.models import CategoryModel


class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(CategoryModel, related_name="taskCategor")

    def __str__(self):
        return f"{self.taskTitle} {self.taskDescription}, {self.categories} {self.is_completed} {self.taskAssignDate}"


# Create your models here.

# ‘TaskModel’ having fields
# taskTitle
# taskDescription
# is_completed by default False
# Task Assign Date
# N.B : Here ‘is_completed’ field should be of type models.BooleanField and default values for this field should be ‘False’                                                             ( Marks - 10 )

# TaskCategory Model will have
# Category Name
# Many-to-Many Relationships with task model                              ( Marks - 10 )
