from typing import List, Tuple


def study_schedule(permanence_period: List[Tuple[int, int]], target_time: int
                   ) -> int:
    if not isinstance(target_time, int):
        return None

    counter = 0

    for number_studying_same_time in permanence_period:
        (start, final) = number_studying_same_time
        if not isinstance(start, int) or not isinstance(final, int):
            return None
        if start <= target_time <= final:
            counter += 1
    return counter
