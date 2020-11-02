from django.db import models

# Create your models here.
CATEGORY = (('business','ビジネス'),('life','ライフ'),('other','その他'))

class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
#class名ははmodel(データベーステーブルの名前)
class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add= True)
    category = models.CharField(
        max_length=50,
        #choiceでプルダウンで選択させる
        choices = CATEGORY
        )
    def __str__(self):
        return self.title
    
