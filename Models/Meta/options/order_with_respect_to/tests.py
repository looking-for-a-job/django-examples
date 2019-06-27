#!/usr/bin/env python
from .models import Answer, Question

question = Question.objects.get(id=1)
answers = question.get_answer_order()
print(answers)
