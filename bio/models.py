from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    descripiton = models.TextField()
    user = models.ForeignKey(User, max_length=20, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='image/', default='default.png', null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class KindSkill (models.Model):
    skill_category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.skill_category}'
    
class Skill(models.Model):
    kind_skill = models.ForeignKey(KindSkill, null=True, max_length=100, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, max_length=20, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.skill_name}'
    

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    do_date = models.DateField()
    image = models.ImageField(upload_to='image/', default='default.png', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, max_length=20, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title}'
    

class Course (models.Model):
    title = models.CharField(max_length=100)
    do_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Tanggal Selesai (Bisa kosong jika masih bekerja)
    is_current = models.BooleanField(default=False) 
    image = models.ImageField(upload_to='image/', default='default.png', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, max_length=20, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Portofolio(models.Model):
    title = models.CharField(max_length=100)
    do_date = models.DateField()
    image = models.ImageField(upload_to='image/', default='default.png', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, max_length=20, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title}'

class PengalamanKerja(models.Model):
    job_title = models.CharField(max_length=100)  # Jabatan
    company_name = models.CharField(max_length=100)  # Nama Perusahaan
    location = models.CharField(max_length=100, blank=True, null=True)  # Lokasi kerja (opsional)
    start_date = models.DateField()  # Tanggal Mulai
    end_date = models.DateField(blank=True, null=True)  # Tanggal Selesai (Bisa kosong jika masih bekerja)
    is_current = models.BooleanField(default=False)  # Apakah masih bekerja di sini?
    description = models.TextField(blank=True, null=True)  # Deskripsi pekerjaan
    user = models.ForeignKey(User, max_length=20, on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='image/', default='default.png', null=True, blank=True)

    class Meta:
        ordering = ['-start_date']  # Urutkan dari pengalaman terbaru

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
