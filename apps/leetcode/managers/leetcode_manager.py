from apps.leetcode.models.leet_code_problem import LeetCodeProblem
from django.core.paginator import Paginator

class LeetCodeManager:

    def get_probelm_by_id(self,id):
        try:
            # problem = LeetCodeProblem.objects.get(problem_id=id)
            problem = LeetCodeProblem.objects.filter(problem_id=id)
            return problem
        except :
            return False

    def add_leet_code_problem(self,**fields):
        try:
            inserted = LeetCodeProblem.objects.create(**fields)
            return inserted
        except Exception as e:
            return False
        
    def get_problems(self,limit=None):
        q = LeetCodeProblem.objects.all()
        if limit is not None:
            pg = Paginator(q,limit)
            return pg.object_list
        return q
    
    def update_problem(self,id,**kwargs):
        updated = LeetCodeProblem.objects.filter(problem_id=id).update(**kwargs)
        return updated