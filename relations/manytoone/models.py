from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return 'Reporter:\n\tName:{} {}\n\temail: {}'.format(self.first_name, self.last_name, self.email)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return 'Article\n\tHeadline: {}\n\tPublished: {}\n\t\tReporter: {} {}\n\t\t{}'.format(self.headline, self.pub_date, self.reporter.first_name, self.reporter.last_name, self.reporter.email)
