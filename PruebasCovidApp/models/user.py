from django.db                  import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError('El usuario debe tener un username')
        user = self.model(username = username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username = username , 
            password = password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length= 20, unique=True)
    password = models.CharField('Password', max_length=256)
    name = models.CharField('Nombres', max_length=50)
    lastname = models.CharField('Apellidos', max_length=50)
    age = models.IntegerField('Edad')
    gender = models.CharField('Sexo', max_length = 15)

    def save(self, **kwargs):
        some_salt = 'ahckudSNFjhVlJ945fkwpx'
        self.password = make_password (self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'