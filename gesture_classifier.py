import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def classify_gesture(landmarks):
    if not landmarks or len(landmarks) != 21:
        return "Unknown"

    wrist       = landmarks[0]
    thumb_tip   = landmarks[4]
    thumb_ip    = landmarks[3]
    index_tip   = landmarks[8]
    middle_tip  = landmarks[12]
    ring_tip    = landmarks[16]
    pinky_tip   = landmarks[20]

    d_thumb  = euclidean_distance(thumb_tip, wrist)
    d_index  = euclidean_distance(index_tip, wrist)
    d_middle = euclidean_distance(middle_tip, wrist)
    d_ring   = euclidean_distance(ring_tip, wrist)
    d_pinky  = euclidean_distance(pinky_tip, wrist)
    ok_dist = euclidean_distance(thumb_tip, index_tip)

    # GESTURE: OK
    if ok_dist < 0.04 and d_middle > 0.15 and d_ring > 0.15 and d_pinky > 0.15:
        return "OK"

    # GESTURE: Fist
    if (ok_dist > 0.07 and all(d < 0.15 for d in [d_thumb, d_index, d_middle, d_ring, d_pinky])):
        return "Fist"

    # GESTURE: Open Hand
    if all(d > 0.25 for d in [d_thumb, d_index, d_middle, d_ring, d_pinky]):
        return "Open Hand"

    # GESTURE: Peace ✌️
    if (d_index > 0.25 and d_middle > 0.25 and d_ring < 0.15 and d_pinky < 0.15):
        return "Peace"

    # GESTURE: Thumbs Up 👍
    if (thumb_tip.y < thumb_ip.y and all(d < 0.15 for d in [d_index, d_middle, d_ring, d_pinky])):
        return "Thumbs Up"

    # GESTURE: Rock 🤘
    if (d_index > 0.25 and d_pinky > 0.25 and d_middle < 0.15 and d_ring < 0.15):
        return "Rock"

    # GESTURE: Stop ✋
    if all(d > 0.25 for d in [d_index, d_middle, d_ring, d_pinky]) and thumb_tip.x < index_tip.x:
        return "Stop"

    return "Unknown"

