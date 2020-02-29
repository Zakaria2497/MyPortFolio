from django.db import models

# Create your models here.
#CReate a Blog Model

#title
#pubdate
#image
# Body    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title

    def summary(self):
        list = self.body.split()
        hint = " ".join(list[:15]) + "..."
        return  hint


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')



#create a migration

# migrate


#Add to the main