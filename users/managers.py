from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, username, password, is_staff, is_superuser, **kwargs):
        user = self.model(
            username=username, is_staff=is_staff, is_superuser=is_superuser, **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **kwargs):
        return self._create_user(username, password, False, False, **kwargs)

    def create_superuser(self, username, password, **kwargs):
        return self._create_user(username, password, True, True, **kwargs)
