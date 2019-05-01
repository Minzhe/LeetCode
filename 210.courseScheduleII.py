import collections

class Solution:
    def findOrder(self, numCourses, prerequisites):
        toCourse = {i: set() for i in range(numCourses)}
        fromCourse = collections.defaultdict(set)
        for course, prereq in prerequisites:
            fromCourse[course].add(prereq)
            toCourse[prereq].add(course)
        
        avail = [c for c in range(numCourses) if not fromCourse[c]]
        taken = []
        while avail:
            take = avail.pop(0)
            taken.append(take)
            for c in toCourse[take]:
                fromCourse[c].remove(take)
                if not fromCourse[c]:
                    avail.append(c)
        if all([len(fromCourse[c]) == 0 for c in fromCourse.keys()]):
            return taken
        else:
            return []
        
        toCourse = {i: set() for i in range(numCourses)}
        fromCourse = collections.defaultdict(set)
        for course, prereq in prerequisites:
            fromCourse[course].add(prereq)
            toCourse[prereq].add(course)
        
        avail = [c for c in range(numCourses) if not fromCourse[c]]
        taken = []
        while avail:
            take = avail.pop(0)
            taken.append(take)
            for c in toCourse[take]:
                fromCourse[c].remove(take)
                if not fromCourse[c]:
                    avail.append(c)
            fromCourse.pop(take)
        return taken if not fromCourse else []

sol = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
res = sol.findOrder(numCourses, prerequisites)
print(res)