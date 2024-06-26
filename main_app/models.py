from datetime import date
from django.db import models

# A tuple of 2-tuples
COMMENTS = (
    ('P', 'Positive'),
    ('N', 'Neutral'),
    ('B', 'Negative')
)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField(default=2005)

    def __str__(self):
        return self.name

    def rev_for_today(self):
        return self.reviews_set.filter(date=date.today()).count() >= len(COMMENTS)


class Review(models.Model):
    date = models.DateField('Commenting Date')
    comments = models.CharField(
        max_length=100,
        choices=COMMENTS,
        # set the default value for meal to be 'B'
        default=COMMENTS[0][0])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_comments_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
