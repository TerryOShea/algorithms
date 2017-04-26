def range_overlap(point1, length1, point2, length2):
    highest_start_point = max(point1, point2)
    lowest_end_point = min(point1 + length1, point2 + length2)

    if highest_start_point >= lowest_end_point:
        return (None, None)

    overlap_length = lowest_end_point - highest_start_point

    return (highest_start_point, overlap_length)

def rect_intersection(r1, r2):
    x_overlap_point, overlap_width = range_overlap(r1['left_x'], r1['width'], r2['left_x'], r2['width'])
    y_overlap_point, overlap_height = range_overlap(r1['bottom_y'], r1['height'], r2['bottom_y'], r2['height'])

    if not overlap_width or not overlap_height:
        return {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None
        }

    return {
        'left_x': x_overlap_point,
        'bottom_y': y_overlap_point,
        'width': overlap_width,
        'height': overlap_height
    }

### TESTING ###

r1 = {
    'left_x': 1,
    'bottom_y': 5,
    'width': 10,
    'height': 4
}

r2 = {
    'left_x': 7,
    'bottom_y': 7,
    'width': 4,
    'height': 10
}

print(rect_intersection(r1, r2))
