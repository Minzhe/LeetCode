import collections
class Solution:
    def canFinish(self, numCourses, prerequisites):
        # *****************   BFS   ******************** #
        # ith course is the prerequisits of what courses  
        toCourse = {i: set() for i in range(numCourses)}
        # ith course depends on what courses
        fromCourse = collections.defaultdict(set)

        for course, prereq in prerequisites:
            toCourse[prereq].add(course)
            fromCourse[course].add(prereq)
        # start from course with no prerequisits
        avail = [c for c in range(numCourses) if len(fromCourse[c]) == 0]
        while avail:
            taken = avail.pop(0)
            for c in toCourse[taken]:
                fromCourse[c].remove(taken)
                if not fromCourse[c]:
                    avail.append(c)
        return all([len(fromCourse[c]) == 0 for c in fromCourse.keys()])

        # # *****************   DFS   ******************** #
        # # ith course is the prerequisits of what courses  
        # toCourse = {i: set() for i in range(numCourses)}
        # # ith course depends on what courses
        # fromCourse = collections.defaultdict(set)

        # for course, prereq in prerequisites:
        #     toCourse[prereq].add(course)
        #     fromCourse[course].add(prereq)
        # # start from course with no prerequisits
        # avail = [c for c in range(numCourses) if len(fromCourse[c]) == 0]
        # while avail:
        #     taken = avail.pop()
        #     for c in toCourse[taken]:
        #         fromCourse[c].remove(taken)
        #         if not fromCourse[c]:
        #             avail.append(c)
        #     fromCourse.pop(taken)
        # return not fromCourse


sol = Solution()
numCourses = 2
prerequisites = [[1,0]]
res = sol.canFinish(numCourses, prerequisites)
print(res)