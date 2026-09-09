from django.db import models
import string
import random



class URL(models.Model):
    original_url = models.URLField(max_length=2048)        # the long URL                                                                          
    short_code = models.CharField(max_length=10, unique=True)  # e.g. "aB3kX9"                                                      
    created_at = models.DateTimeField(auto_now_add=True)                                                                                           
    visit_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):                                                                                                               
            if not self.short_code:                                                                                                                    
                self.short_code = self.generate_short_code()                                                                                           
            super().save(*args, **kwargs)                                                                                                              
                                                                                                                                                       
    @staticmethod                                                                                                                                  
    def generate_short_code(length=6):                                                                                                             
        chars = string.ascii_letters + string.digits  # a-z, A-Z, 0-9                                                                              
        while True:                                                                                                                                
            code = ''.join(random.choices(chars, k=length))                                                                                        
            if not URL.objects.filter(short_code=code).exists():                                                                                   
                return code                                                                                                                        
                                                                                                                                                       
    def __str__(self):                                                                                                                             
        return f"{self.short_code} → {self.original_url}"
