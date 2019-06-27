#!/usr/bin/env python
from .models import Student

Student(year_in_school='FR').save()
Student(year_in_school='??').save()
