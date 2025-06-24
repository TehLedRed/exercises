playlist = [8, 4, 12, 16, 23, 32, 28]

def binarySearch(query: int, playlist: [int]) -> bool:
    playlist.sort()

    start, end = 0, len(playlist) - 1

    while start < end:
        mid = (start + end) // 2
        if playlist[mid] == query:
            return True
        elif playlist[mid] < query:
            start = mid + 1
        else:
            end = mid -1


    # def helper(start, end):
    #     if start > end:
    #         return False  # Not found

    #     mid = (start + end) // 2
    #     if playlist[mid] == query:
    #         return True
    #     elif playlist[mid] < query:
    #         return helper(mid + 1, end)
    #     else:
    #         return helper(start, mid - 1)

    # return helper(0, len(playlist) - 1)

print(binarySearch(16, playlist = [8, 4, 16, 23, 32, 28]))