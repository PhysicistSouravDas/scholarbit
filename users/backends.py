from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

# UserModel = get_user_model

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username = None, password = None, **kwargs):
#         try:
#             user = UserModel.objects.get(
#                 Q(username__iexact = username) | Q(email__iexact = username)
#             )
#         except ObjectDoesNotExist:
#             UserModel().set_password(password)
#         except MultipleObjectsReturned:
#             return User.objects.filter(email=username).order_by('id').first()
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user

#     def get_user(self, user_id):
#         try:
#             user = UserModel.objects.get(pk = user_id)
#         except ObjectDoesNotExist:
#             return None
#         return user if self.user_can_authenticate(user) else None
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))               # (email=username))
            if ('@gmail.com') in username.lower():
                if username.count('@') > 1:
                    index_of_separator = username.rfind('@')
                    email_local, email_domain = username[:index_of_separator], username[index_of_separator + 1:]
                else: # if email.count('@') == 1:
                    email_local, email_domain = username.split('@')    
                user = UserModel.objects.get(Q(email__iexact=email_local+'@googlemail.com') | Q(email__iexact=email_local+'@gmail.com'))

            elif ('@googlemail.com') in username.lower():
                if username.count('@') > 1:
                    index_of_separator = username.rfind('@')
                    email_local, email_domain = username[:index_of_separator], username[index_of_separator + 1:]
                else: # if email.count.count('@') == 1:
                    email_local, email_domain = username.split('@')
                user = UserModel.objects.get(Q(email__iexact=email_local+'@gmail.com') | Q(email__iexact=email_local+'@googlemail.com'))

            else:
                user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))    
        except UserModel.DoesNotExist:
            return None
            # UserModel().set_password(password)
        except UserModel.MultipleObjectsReturned:
            return UserModel.objects.filter(email=username).order_by('id').first()  
        else:
            if user.check_password(password):# and self.user_can_authenticate(user):
                return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(pk = user_id)
        except UserModel.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None