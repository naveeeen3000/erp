from apps.leetcode.models.leet_code_problem import LeetCodeProblem



class LeetCodeManager:


    def add_leet_code_problem(self,**fields):
        try:
            inserted = LeetCodeProblem.objects.create(**fields)
            return inserted
        except Exception as e:
            return False
        
    def get_problems(self,limit=None):
        q = LeetCodeProblem.objects.all()
        if limit is not None:
            limited_q = q[:limit]
            return limited_q
        return q
        