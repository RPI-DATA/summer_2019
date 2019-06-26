ok = Notebook('lab02.ok')
name = 'test'
points_per_test=1
comments="trial1"
import sys
sys.path.append('..')
import grade
grade.grade(name, points_per_test, comments, ok)