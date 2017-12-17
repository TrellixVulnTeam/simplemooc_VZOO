from django.template import Library

register = Library()

from simplemooc.courses.models import Enrollment

# Este modo usa o template my_courses.html e em
# dashboard.html basta utilizar {% load courses_tags %} e
# substituir o html por  {% my_courses user %}
@register.inclusion_tag('courses/templatetags/my_courses.html')
def my_courses(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context
    