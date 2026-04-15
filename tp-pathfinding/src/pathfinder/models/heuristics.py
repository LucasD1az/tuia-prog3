def manhattan_distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> int:
    """Calculate the Manhattan distance between two positions

        Args:
            pos1 (tuple[int, int]): First cell position
            pos2 (tuple[int, int]): Second cell position

        Returns:
            int: Manhattan distance between both cells
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])