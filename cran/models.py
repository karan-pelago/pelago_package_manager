from django.db import models

class Package(models.Model): 
    class Meta:
        unique_together = (('name', 'version'),)
    name = models.CharField(max_length=500)
    version = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    authors = models.CharField(max_length=500)
    maintainers = models.CharField(max_length=500)
    publish_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
            return self.name
    def from_dict(self, d):
        self.name = d["name"]
        self.version = d["version"]
        self.title = d["title"]
        self.description = d["description"]
        self.authors = d["author"]
        self.maintainers = d["maintainer"]
        self.publish_date = d["date"]
        self.save()
