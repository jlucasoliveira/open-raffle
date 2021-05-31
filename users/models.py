from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import managers


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        unique=True,
        db_index=True,
        max_length=200,
        verbose_name=_("nome de usuário"),
        help_text="Usado para identificar o usuário no sistema.",
    )
    email = models.EmailField(verbose_name=_("email"), null=True, default=None)
    name = models.CharField(_("nome"), max_length=300)
    is_staff = models.BooleanField(
        verbose_name=_("membro da equipe"),
        default=False,
        help_text=_("Permite que este usuário tenha acesso ao painel admin."),
    )
    is_active = models.BooleanField(verbose_name=_("ativo"), default=True)
    date_joined = models.DateTimeField(
        verbose_name=_("data de admissão"), auto_now_add=True
    )

    objects = managers.UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        verbose_name = _("usuário")

    def __str__(self) -> str:
        return self.username
