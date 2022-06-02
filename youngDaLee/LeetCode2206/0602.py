class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        new_matric = []

        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            new_matric.append(row)

        return new_matric