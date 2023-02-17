from django.db import models
from django.utils.translation import gettext as _



SERVICE_CHOICES = (
    ("air transport", "air transport"),
    ("transport", "transport service"),
    ("warehouse", "Warehouse service"),
   
)

class SocialMedia(models.Model):
    name = models.CharField(verbose_name="name", max_length=50)
    icon = models.CharField(verbose_name="icon name", max_length=200)

    class Meta:
        verbose_name = _("SocialMedia")
        verbose_name_plural = _("SocialMedias")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("SocialMedia_detail", kwargs={"pk": self.pk})




class Contact(models.Model):
    title = models.CharField(verbose_name="contact title", max_length=50)
    email = models.EmailField(verbose_name="email address", max_length=254)
    phone = models.CharField(verbose_name="phone number", max_length=15)
    location = models.CharField(verbose_name="Location", null=True, max_length=255)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})




class Team(models.Model):
    name = models.CharField(verbose_name="team member name", max_length=50)
    email = models.EmailField(_("email adddress"), max_length=254)
    phone = models.CharField(_("mobile phone"), max_length=50)
    social_media = models.ManyToManyField(SocialMedia, verbose_name=_("social media"))
    social_media_link = models.URLField(verbose_name=_('social media link'), null=True)

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"pk": self.pk})


class Quote(models.Model):
    name = models.CharField(_("name"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    service = models.CharField(verbose_name="choose service", choices=SERVICE_CHOICES, max_length=50)
    massage = models.TextField(verbose_name="your quote massage", null=True)


    class Meta:
        verbose_name = _("Quote")
        verbose_name_plural = _("Quotes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("quote_detail", kwargs={"pk": self.pk})


class About(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='About/images/')
    decriptions = models.TextField(verbose_name="descriptions")





class Service(models.Model):
    title = models.CharField(verbose_name="service title", max_length=50)
    description = models.TextField(verbose_name='description')
    image = models.ImageField(verbose_name="service image", upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})