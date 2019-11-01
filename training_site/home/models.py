from django.db import models

# Create your models here.

#class QuizQuestion(models.Model):
#    pass
#
#class Quiz(models.Model):
#    questions = models.ManyToManyField(QuizQuestion)
#
#class SlideShowPage(models.Model):
#    pass
#
#class SlideShow(models.Model):
#    pages = models.ManyToManyField(SlideShowPage)
#    #quiz = models.ForeignKey(Quiz) = models.TextField()

class ResourceLink(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    quick_links = models.TextField()
    thumbnail = models.ImageField(default='rec_info_default.png', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:25] + "..."
