from django.db import models

class Availability(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.date} - {self.start_time} to {self.end_time}"

class Staff(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(
        max_length=20,
        choices=[
            ('mentor', 'Mentor'),
            ('judge', 'Judge'),
            ('workshop_leader', 'Workshop Leader'),
        ],
        default='mentor',
    )
    availabilities = models.ManyToManyField(Availability, blank=True)

    def __str__(self):
        return self.name