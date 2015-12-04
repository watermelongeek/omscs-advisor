from django import template

from advisor.config import Term

register = template.Library()


@register.inclusion_tag('elements/course_thumbnail.html')
def course_thumbnail(offering):
    return {
        'offering': offering
    }


@register.inclusion_tag('elements/review_thumbnail.html')
def review_thumbnail(review, show_reviewer=True):
    return {
        'review': review,
        'show_reviewer': show_reviewer
    }

@register.simple_tag()
def term(term):
    return Term.format(term)