from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid
from django.utils.text import slugify







def cap(string):
    new=string[0].upper()
    for i in range(1,len(string),1):
        if string[i-1] == '-':
            new += string[i].upper()
        else:
            new +=string[i]
    return new


class accountManager(BaseUserManager):
    def create_user(self,email,fname,lname,phone,password = None):
        if not email:
            raise ValueError('user must have an email')

        if not fname:
            raise ValueError('Unvalid Null Value')
        
        if not lname:
            raise ValueError('Unvalid Null Value')
        
        if not phone:
            raise ValueError('Unvalid Null Value')
        
        user = self.model(
            email = self.normalize_email(email),
            phone = phone,
            fname = fname,
            lname = lname,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    

    def create_superuser(self,email,fname,lname,phone,password):
        user = self.create_user(
            email = self.normalize_email(email),
            phone = phone,
            fname = fname,
            lname = lname,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user 









class UserType(models.Model):
    typeName = models.CharField(max_length=20)
    def __str__(self):
        return self.typeName

class User(AbstractBaseUser):
    def imagesave(instance,filename):
        imagename , extension = filename.split(".")
        return "users/%s.%s"%(instance.id,extension)
    user_id         = models.UUIDField(unique = True, default = uuid.uuid4,editable = False)
    fname           = models.CharField(max_length=30, verbose_name="First Name")
    lname           = models.CharField(max_length=30, verbose_name="Last Name")
    phone           = models.CharField(max_length=13, verbose_name="Phone Number")
    email           = models.EmailField(unique = True, max_length=254,verbose_name="Email")
    password        = models.CharField(max_length=150)
    image           = models.ImageField(default="users/logo.png",upload_to=imagesave, height_field=None, width_field=None)
    joined_at       = models.DateField(auto_now_add=True,verbose_name="joined at")
    slug            = models.SlugField(blank=True,null=True, unique=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    user_type       = models.ForeignKey(UserType, blank=False, null=False, on_delete=models.PROTECT)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['fname','lname','phone']

    objects = accountManager()



    def save(self, commit=True,*args, **kwargs):
        self.slug = slugify(self.fname+" "+self.lname)
        self.slug = cap(self.slug)
        # Save the provided password in hashed format
        user = super(User, self)
        user.set_password(self.password)
        if commit:
            # user.save()
            super(User,self).save(*args,**kwargs)
        return user


    def __str__(self):
        return self.slug


    def has_perm(self , perm , obj = None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True

