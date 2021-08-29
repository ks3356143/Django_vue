from django.db import models
from django.utils import timezone

class Computer(models.Model):
    #下面是枚举字段
    COMPUTER_TYPES = (
       ("laptop", "laptop"),
       ("tablet", "tablet"),
       ("desktop", "desktop")
    )
    name = models.CharField(max_length=100,default="联想电脑1")
    computer_type = models.CharField(choices=COMPUTER_TYPES, default=COMPUTER_TYPES[0][0], max_length=100)
    cpu = models.CharField(max_length=100,default="i7")
    memory = models.CharField(max_length=100,default='8G')
    disk = models.CharField(max_length=100,default='500G')
    main_board = models.CharField(max_length=100,default='marton')
    display_card = models.CharField(max_length=100,default='sb')
    monitor = models.CharField(max_length=100,default='monitore1')
    publish_time = models.DateTimeField(default=timezone.now)
    halt_time = models.DateTimeField(blank=True,default=timezone.now)

    def __str__(self):
        return self.name
