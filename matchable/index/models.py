from django.db import models

class Institute(models.Model) :
    categories = [
        # 크리에이티브
        ('1', '디지털 드로잉'),
        ('2', '영상 편집'),
        ('3', '공예'),
        ('4', '요리/음료'),
        ('5', '베이킹/디저트'),
        ('6', '음악'),
        ('7', '댄스'),
        ('8', '운동'),
        ('9', '사진/영상'),
        # 컴퓨터
        ('10', '모션 그래픽'),
        ('11', '인테리어'),
        ('12', '제품 디자인'),
        ('13', 'IT'),
        ('14', '오피스'),
        ('15', '웹 디자인/웹 퍼블리셔'),
        ('16', '영상 편집'),
        ('17', '메타버스'),
        # 언어
        ('18', '영어'),
        ('19', '중국어'),
        ('20', '일본어'),
        ('21', '스페인어'),
        ('22', '불어'),
        ('23', '독일어'),
    ]
    name = models.CharField(max_length = 40)
    location = models.CharField(max_length = 12)
    description = models.TextField()
    category = models.CharField(max_length = 12, choices = categories)
    image = models.ImageField(upload_to = 'thumbnail/', blank = True, null = True)
    
    def __str__(self) :
        return self.name
        
    def summary(self) :
        return self.description[:46]