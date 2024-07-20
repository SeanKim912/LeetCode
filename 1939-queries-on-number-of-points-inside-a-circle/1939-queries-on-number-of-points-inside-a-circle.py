class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        solution = []

        def query(dots, circle):
            counter = 0
            circlex = circle[0]
            circley = circle[1]
            radius = circle[2]
            for i in dots:
                dotx = i[0]
                doty = i[1]
                if (dotx - circlex)**2 + (doty - circley)**2 <= radius**2:
                    counter += 1

            return counter

        for j in queries:
            solution.append(query(points, j))

        return solution