class Solution:
    def countStudents(self, students, sandwiches) -> int:
        rep = 0

        while len(sandwiches) > 0:
            if rep >= len(sandwiches):
                return len(sandwiches)

            if sandwiches[0] == students[0]:
                rep = 0
                sandwiches[:] = sandwiches[1:]
                students[:] = students[1:]
            else:
                rep += 1
                students[:] = students[1:] + students[0:1]

        return len(sandwiches)