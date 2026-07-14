from django.urls import reverse

from submission import models as submission_models


def article_is_commissioned(article):
    from plugins.commission import models

    if not article or not article.pk:
        return False
    return models.CommissionedArticle.objects.filter(article=article).exists()


def submission_form_init(form=None, article=None, journal=None, **kwargs):
    """
    The commissioning editor decides a commissioned article's section, so
    the author sees the editor's choice — even if the section is closed
    for public submission — but cannot change it.
    """
    if not article_is_commissioned(article):
        return

    section_field = form.fields.get('section')
    if section_field:
        section_field.queryset = submission_models.Section.objects.filter(
            pk=article.section_id,
        )
        section_field.disabled = True
        section_field.help_text = (
            'The section was selected by your commissioning editor and '
            'cannot be changed.'
        )


def admin_hook(context):
    return """
    <li>
        <a href="{url}">
            <i class="fa fa-arrow-circle-right"></i> Commission Articles
        </a>
    </li>
    """.format(url=reverse('commission_index'))
