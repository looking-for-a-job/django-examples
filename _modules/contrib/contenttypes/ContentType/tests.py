from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from taggit.models import Tag,TaggedItem
from .models import Food

"""
https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/
"""

apple = Food.objects.create(name="apple")
apple.tags.add("red", "green", "delicious")

strawberry = Food.objects.create(name="strawberry")
strawberry.tags.add("red","delicious")

# user_type = ContentType.objects.get(app_label='taggit', model='taggeditem')
user_type = ContentType.objects.get(app_label='app', model='food')
# q = TaggedItem.objects.filter(content_type=user_type).values('object_id').annotate(count=Count('object_id'))
#ids = TaggedItem.objects.filter(content_type=user_type).values('object_id', flat=True)

#print(q.all())
ids=list(Food.objects.values_list('id', flat=True))
q = Tag.objects.filter(food__id__in=ids).values('id','name').annotate(count=Count('id')).order_by('-count')
for t in q.all():
    print(t)
