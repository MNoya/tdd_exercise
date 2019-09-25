from django.db import models


class Puzzle(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField()
    byline = models.CharField(max_length=255)
    publisher = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.publisher} {self.date}'


class Entry(models.Model):
    entry_text = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return f'{self.entry_text}'


class Clue(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    clue_text = models.CharField(max_length=512)
    theme = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.entry} {self.clue_text}'
