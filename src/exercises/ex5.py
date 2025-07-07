def binarySearch(query: int, playlist: list[int]) -> bool:
    """
    Perform binary search to determine if 'query' is an element of 'playlist'.

    Args:
        query (int): The number to search for.
        playlist (list): A list of integers.

    Returns:
        bool: True if 'query' is present in 'playlist', False otherwise.
    """
    playlist.sort()

    start, end = 0, len(playlist) - 1

    while start <= end:
        mid = (start + end) // 2
        if playlist[mid] == query:
            return True
        elif playlist[mid] < query:
            start = mid + 1
        else:
            end = mid - 1

    raise ValueError(f"{query} is not in the playlist.")
