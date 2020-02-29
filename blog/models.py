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




#create a migration

# migrate


#Add to the main