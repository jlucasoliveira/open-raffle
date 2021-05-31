import uuid

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.formats import localize
from django.utils.timezone import localdate
from django.utils.translation import gettext_lazy as _


class AutoCreatedUpdatedMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.deletion.PROTECT,
        verbose_name=_("criado por"),
    )
    created_at = models.DateTimeField(
        verbose_name=_("data de criação"), auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("data de atualização"), auto_now=True
    )

    class Meta:
        abstract = True


class Raffle(AutoCreatedUpdatedMixin):
    value = models.DecimalField(
        verbose_name=_("valor por ponto"),
        decimal_places=2,
        max_digits=12,
        validators=[MinValueValidator(0)],
    )
    raffle_date = models.DateField(verbose_name=_("data do sorteio"))
    amount = models.PositiveSmallIntegerField(
        verbose_name=_("quantidade de pontos"),
        default=50,
    )

    class Meta:
        verbose_name = _("rifa")

    def __str__(self):
        localized_date = localize(localdate(self.raffle_date))
        return f"{self.created_by} - {localized_date}"


class RaffleItem(AutoCreatedUpdatedMixin):
    raffle = models.ForeignKey(
        to="raffle.Raffle",
        on_delete=models.deletion.CASCADE,
        verbose_name=_("rifa"),
    )
    item = models.PositiveSmallIntegerField(verbose_name=_("ponto"))
    winner = models.BooleanField(verbose_name=_("ganhador"), default=False)

    class Meta:
        verbose_name = _("ponto")
        index_together = ["raffle", "item"]
        unique_together = ["raffle", "item"]

    def __str__(self):
        return f"{self.raffle} - {self.item}"
