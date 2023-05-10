from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def seconds(context,seconds='',day=''):
    print('SECOND TO HM CALLED')
    if seconds=='' or seconds is None:
        return ''
    if type(seconds)==str:
        return seconds
    if seconds>=86400:
        day = day
    minutes = int(seconds / 60)
    hours = int(minutes / 60)
    days = int(hours/24)
    if day == 'day':
        return ("%d.%02d D" % (days,hours % 24))
    return("%02d:%02d" % (hours,minutes % 60))
print('SECOND TO HM CALLED aldadlalhsladlh ')
