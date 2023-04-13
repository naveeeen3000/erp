from django.db import models


class LeetCodeProblem(models.Model):

    difficulty_choices = (
        ("Easy","EASY"),
        ("Not Set",""),
        ("Medium","MEDIUM"),
        ("Hard","HARD")
    )
    problem_id = models.BigAutoField(primary_key=True,auto_created=True)
    topic = models.CharField(max_length=100,null=True)
    leetcode_question_link = models.URLField(max_length=255)
    difficulty = models.CharField(choices=difficulty_choices,max_length=100)
    started_at = models.DateTimeField(null=True)
    finished_at = models.DateTimeField(null=True)
    solved = models.BooleanField(default=False)
    beats_time_complexity = models.FloatField(null=True)

    class Meta:
        db_table = 'leetcode_problems'
        ordering = ['difficulty']