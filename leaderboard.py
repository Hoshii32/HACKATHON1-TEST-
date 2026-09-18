# Challenge 3: Leaderboard Sorter (Has a intentional bug!)
def sort_leaderboard(scores):
    # BUG: This currently sorts scores alphabetically/as strings instead of numerically descending!
    # TODO: Fix the bug so it sorts numerical scores in descending order.
    return sorted(scores, reverse=True)
