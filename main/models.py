from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, is_staff=False, is_active=True, is_superuser=False):
        if not phone:
            raise ValueError('users must have a phone number')
        if not password:
            raise ValueError('user must have a password')

        user_obj = self.model(phone=phone)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.super = is_superuser

        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, phone, password=None):
        user = self.create_user(phone, password=password, is_staff=True, )
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        return user


class User(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Up to 15 digits allowed.")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    fname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    address = models.TextField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    first_login = models.BooleanField(default=False)
    otp = models.CharField(max_length=9, blank=True, null=True)
    verified = models.BooleanField(default=False, help_text='If otp verification got successful')
    count = models.IntegerField(default=0, help_text='Number of otp sent')

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    super = models.BooleanField(default=False)

    plan_user = models.BooleanField(default=False)
    booking_user = models.BooleanField(default=False)
    service_user = models.BooleanField(default=False)
    mechanic_user = models.BooleanField(default=False)
    customer_review_user = models.BooleanField(default=False)
    faq_user = models.BooleanField(default=False)
    support_user = models.BooleanField(default=False)
    account_user = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone

    def get_full_name(self):
        return self.fname + " " + self.lname

    def get_short_name(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.super


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    mobile = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)

    def __str__(self):
        return self.mobile + '| ' + self.user.username


class RazorPay(models.Model):
    secret_key = models.CharField(max_length=200, blank=True, null=True)
    public_key = models.CharField(max_length=200, blank=True, null=True)
