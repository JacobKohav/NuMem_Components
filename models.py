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

    def link_this(self):
      long_string = self.body #replace this with the database textfield
      link_list = long_string.splitlines()
    

      for i in range(len(link_list)):
        link_list[i] = '<a href="' + link_list[i] + '">'+ link_list[i] + ' </a><br>'

      link_list = "\n".join(link for link in link_list)
      print(link_list)
        
      return link_list

      #link_list = []
      	#for link in self.quick_links.split("\n")
      		#link_list.apphend(link)
