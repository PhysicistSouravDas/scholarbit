from django.contrib.auth.models import AbstractUser # , BaseUserManager, UserManager
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from django.contrib.auth.validators import UnicodeUsernameValidator

User = get_user_model

# Create your models here.
occupation_choices = (
    ('student', 'Student'),
    ('teacher', 'Teacher')
)
avatar_choices = (
    ('https://avataaars.io/?avatarStyle=Transparent&topType=LongHairBob&accessoriesType=Prescription02&hairColor=Platinum&facialHairType=Blank&clotheType=Hoodie&clotheColor=Gray01&eyeType=EyeRoll&eyebrowType=Default&mouthType=Default&skinColor=Light', 'Avatar 1'), #Lady 1
    ('https://avataaars.io/?avatarStyle=Transparent&topType=LongHairStraight&accessoriesType=Blank&hairColor=BrownDark&facialHairType=Blank&clotheType=BlazerShirt&eyeType=Default&eyebrowType=Default&mouthType=Default&skinColor=Light', 'Avatar 2'), #Lady 2
    ('https://avataaars.io/?avatarStyle=Transparent&topType=LongHairCurvy&accessoriesType=Prescription01&hairColor=Black&facialHairType=Blank&clotheType=BlazerShirt&eyeType=Hearts&eyebrowType=RaisedExcitedNatural&mouthType=Smile&skinColor=Light', 'Avatar 3'), #Lady 3 lovely
    ('https://avataaars.io/?avatarStyle=Transparent&topType=Hat&accessoriesType=Round&facialHairType=Blank&clotheType=Hoodie&clotheColor=Black&eyeType=Default&eyebrowType=Default&mouthType=Default&skinColor=Tanned', 'Avatar 4'), #Boy 1 with hat and glasses
    ('https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortFlat&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=BlazerShirt&eyeType=Hearts&eyebrowType=RaisedExcitedNatural&mouthType=Smile&skinColor=Light', 'Avatar 5'), #Boy 2 lovely
    ('https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairDreads01&accessoriesType=Sunglasses&hairColor=Black&facialHairType=BeardMagestic&facialHairColor=Black&clotheType=CollarSweater&clotheColor=PastelBlue&eyeType=Hearts&eyebrowType=RaisedExcited&mouthType=Smile&skinColor=Light', 'Avatar 6'), #Beard-man
)
degree_choices = (
    ('Science', (
        ('bsc', 'BSc'),
        ('msc', 'MSc'),
    )),
    ('Arts', (
        ('ba', 'BA'),
        ('ma', 'MA'),
    )),
    ('Commerce', (
        ('bcom', 'BCom'),
        ('mcom', 'MCom'),
    )),
    ('Engineering', (
        ('btech', 'BTech'),
        ('mtech', 'MTech'),
    )),
    ('Education', (
        ('bed', 'BEd'),
        ('med', 'MEd'),
    )),    
    ('Research', (
        ('phd', 'PhD'),
    )),        
)
university_choices = (
    ('cu', 'Calcutta University'),
    ('other', 'Other University'),
)


class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        "Username or Email",
        max_length=150,
        unique=True,
        help_text=("Required. 150 characters or fewer. Letters, digits and +/-/./_ only."),
        validators= [username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    email = models.EmailField(max_length=254, blank=False, unique = True)
    age = models.PositiveIntegerField(null=True, blank=True)
    college = models.CharField("College Name", max_length = 100, blank=True)
    first_name = models.CharField(max_length = 30, blank = False)
    last_name = models.CharField(max_length = 50, blank = False)

    bio = models.TextField("Write something about yourself", blank=True)
    occupation = models.CharField("I am a ", max_length = 50, choices = occupation_choices, blank = True)
    honours = models.CharField("Favourite subject", max_length=50, blank = True)
    avatar = models.TextField("Choose your Avatar", choices = avatar_choices, blank = True)
    degree = models.CharField("If you are student, degree you are pursuing", max_length=250, choices = degree_choices, blank=True)
    university = models.CharField(max_length=50, choices = university_choices, blank=True)
    
    
    # article = one
# class Follower(models.Model):
#     follower = models.ForeignKey(User, related_name='following')
#     following = models.ForeignKey(User, related_name='followers')
    
#     class Meta:
#         unique_together = ('follower', 'following')

#     def __unicode__(self):
#         return u'%s follows %s' % (self.follower, self.following)
# class MyUserManager(BaseUserManager):
#     def get_by_natural_key(self, username):
#         return self.get(**{self.model.username__iexact: username})
#         # return self.get(username__iexact=username)

# class MyUserManager(UserManager):
#     def _create_user(self, username, email, password, **extra_fields):
#         """
#         Create and save a user with the given username, email, and password.
#         """
#         if not username:
#             raise ValueError('The given username must be set')
#         email = self.normalize_email(email)
#         # Lookup the real model class from the global app registry so this
#         # manager method can be used in migrations. This is fine because
#         # managers are by definition working on the real model.
#         GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
#         username = GlobalUserModel.normalize_username(username)
#         username += "Iaddedit"
#         user = self.model(username=username, email=email, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user