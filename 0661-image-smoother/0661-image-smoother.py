class Solution:
    def imageSmoother(self, img):
        rows, cols = len(img), len(img[0])
        smoothed_img = []

        for r in range(rows):
            smoothed_img.append([])
            for c in range(cols):
                total, count = 0, 0

                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        nr, nc = r + dx, c + dy

                        if 0 <= nr < rows and 0 <= nc < cols:
                            total += img[nr][nc]
                            count += 1

                smoothed_img[-1].append(total // count)

        return smoothed_img
