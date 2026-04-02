from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    bio = models.TextField()
    career_goals = models.TextField()
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    location = models.CharField(max_length=100, default='Philippines')
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Profile'


class Skill(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Proficient', 'Proficient'),
        ('Advanced', 'Advanced'),
        ('Strong', 'Strong'),
    ]
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Intermediate')
    percentage = models.IntegerField(default=50, help_text='Skill level as percentage (0-100)')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tools = models.CharField(max_length=300, help_text='Comma-separated list of tools/technologies')
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_tools_list(self):
        return [t.strip() for t in self.tools.split(',')]

    class Meta:
        ordering = ['order']


class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    year_start = models.CharField(max_length=10)
    year_end = models.CharField(max_length=10, default='Present')
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.degree} — {self.school}'

    class Meta:
        ordering = ['order']


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.name} ({self.sent_at.strftime("%Y-%m-%d")})'

    class Meta:
        ordering = ['-sent_at']
