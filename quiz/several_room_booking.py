def get_max_num_ok_slots(
    slot_begin_end_pairs: 'List[Tuple[str, str]]'
) -> int:
    num_ok_slots: int = 0
    last_end: 'Optional[str]' = None
    
    for begin, end in sorted(
        slot_begin_end_pairs,
        key=lambda pair: pair[1],
    ):
        if last_end is None or begin >= last_end:
            last_end = end
            num_ok_slots += 1
            
    return num_ok_slots


def solve(
    begin_end_pairs: 'List[Tuple[int, int]]',
    num_rooms: int,
) -> int:
    pass

if __name__ == "__main__":
    begin_end_pairs = [(0, 10), (15, 25), (10, 25), (5, 30)]
    num_rooms = 2