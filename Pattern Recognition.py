dim = lambda p: (len(p[0]), len(p))

def checkio(pattern, image):
    width_image, height_image = dim(image)
    width_pattern, height_pattern = dim(pattern)

    for y in range(height_image - height_pattern + 1):
        for x in range(width_image - width_pattern + 1):
            if pattern == [i[x:x+width_pattern] for i in image[y:y+height_pattern]]:
                for b in range(y, y+height_pattern):
                    for a in range(x, x+width_pattern):
                        image[b][a] += 2

    return image