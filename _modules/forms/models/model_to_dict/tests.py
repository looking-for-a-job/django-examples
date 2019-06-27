from django.forms.models import model_to_dict
from .models import MyModel

instance = MyModel(name="name value", last_name="last_name value")
data = model_to_dict(instance)
instance = MyModel(**data)

