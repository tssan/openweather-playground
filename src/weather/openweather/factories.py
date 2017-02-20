# import factory
# import factory.fuzzy

# from django.contrib.auth.models import User
# from django.conf import settings

# from toolsbelt.auth import generate_token


# class UserFactory(factory.DjangoModelFactory):
#     class Meta:
#         model = User

#     username = factory.fuzzy.FuzzyText(length=10)
#     email = factory.LazyAttribute(lambda a: "{0}@example.com")
#     password = "my_password"

#     @classmethod
#     def _create(cls, model_class, *args, **kwargs):
#         manager = cls._get_manager(model_class)
#         user = manager.create_user(*args, **kwargs)
#         setattr(user, 'auth_token', generate_token({
#             'pk': user.pk,
#             'username': user.username,
#         }, settings.SECRET_KEY))
#         return user
