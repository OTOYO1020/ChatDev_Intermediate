from blocked_intervals import BlockedIntervals


def simulate(intervals, queries):
    # ★ intervalsをコンストラクタで渡す！
    blocked = BlockedIntervals(intervals)

    results = []
    for D in queries:
        res = blocked.query(D)
        results.append(res)

    return results

