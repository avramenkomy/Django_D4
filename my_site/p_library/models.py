from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    pub_name = models.TextField("Название издательства")
    pub_city = models.TextField("Город издательства")
    pub_site = models.TextField("Сайт издательства")
    foundation_year = models.SmallIntegerField("Год основания")

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

    def __str__(self):
        return self.pub_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="book_publisher", verbose_name= ("Издательство"))
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book_author")
    copy_count = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=8, default=0)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

