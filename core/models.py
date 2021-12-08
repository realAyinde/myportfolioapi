from django.db import models
from myportfolioapi.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext as _

# Create your models here.

class UserManager(BaseUserManager):
    """ Custom user model manager where email is the unique identifiers
        for authentication instead of usernames. """

    def create_user(self, email, password, **extra_fields):
        """ Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and save a SuperUser with the given email and password."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
        

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email



# Other Models used apart from Admin
class Author(BaseModel): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50, blank=True, null=True)
    proffesion = models.CharField(max_length=50)
    bio = models.TextField()
    slug = models.SlugField()

    def get_full_name(self):
        return self.first_name + self.last_name + self.other_names

    def __str__(self):
        try:
            if self.get_full_name():
                return self.get_full_name()
        except AttributeError:
            pass
        return ""

class Article(BaseModel): 
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    content = models.TextField()
    published = models.BooleanField()
    draft = models.BooleanField()
    authors = models.ManyToManyField("Author", verbose_name=_("Authors"))
    tags = models.ManyToManyField("Tag", verbose_name=_("Tags"))


class Tag(BaseModel): 
    name = models.CharField(max_length=50)
    slug = models.SlugField()