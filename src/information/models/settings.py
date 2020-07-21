# import os
# import random
#
# from django.db import models
# from django.template.defaultfilters import slugify
#
#
# def get_filename_exist(file_path):
#     base_name = os.path.basename(file_path)
#     name, ext = os.path.splitext(base_name)
#     return name, ext
#
#
# # To save Book image with new name by function
# def upload_image_path(inistance, file_name):
#     favicon = slugify(inistance.name)
#     new_filename = random.randint(1, 101119)
#     name, ext = get_filename_exist(file_name)
#     final_filename = f'{new_filename}{ext}'
#     return f"settings/{favicon}/{final_filename}"
#
#
# class Settings(models.Model):
#     title = models.CharField(max_length=220, blank=False, null=False, help_text="Enter Web Site Title")
#     favicon = models.ImageField(upload_to=upload_image_path, blank=True, help_text="")
# #
