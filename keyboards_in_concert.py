"""
Decision point: Use the current keyboard, or move to a different one
"""

inf = int(1e9)


def solve_top_down():
    min_result = inf
    memo = {}
    for i in range(n):
        min_result = min(
            min_result,
            top_down(0, i, memo)
        )

    print(min_result)

    # for k, v in memo.items():
    #     print("{}={}".format(k, v))


def top_down(n_index, k_index, memo):
    """
    memo[(n_index,k_index)] = minimum number of switches required to play everything from
        notes[n_index] to notes[len(notes)-1] if you start at keyboard[k_index]
    """
    if n_index >= len(notes):
        return 0

    if (n_index, k_index) in memo:
        return memo[(n_index, k_index)]

    if keyboard_cache[k_index][notes[n_index]]:
        result = top_down(n_index + 1, k_index, memo)
        memo[(n_index, k_index)] = result
        return memo[(n_index, k_index)]
    else:
        min_switches = inf
        for other_k_index in range(n):
            if other_k_index == k_index:
                continue
            if keyboard_cache[other_k_index][notes[n_index]]:
                min_switches = min(
                    min_switches,
                    top_down(n_index, other_k_index, memo) + 1
                )
        memo[(n_index, k_index)] = min_switches
        return memo[(n_index, k_index)]


def solve_bottom_up():
    dp = [[inf] * n for _ in range(len(notes))]

    for k_index in range(n):
        dp[-1][k_index] = 0 if keyboard_cache[k_index][notes[-1]] else 1

    for n_index in range(len(notes) - 2, -1, -1):
        # if a keyboard can play the current note, assign its value as
        # dp[n_index+1][k_index]
        for k_index in range(n):
            if keyboard_cache[k_index][notes[n_index]]:
                dp[n_index][k_index] = dp[n_index + 1][k_index]

        for k_index in range(n):
            if dp[n_index][k_index] < inf:
                continue

            min_switches = inf
            for other_k_index in range(n):
                if other_k_index == k_index:
                    continue

                if keyboard_cache[other_k_index][notes[n_index]]:
                    min_switches = min(
                        min_switches,
                        dp[n_index][other_k_index] + 1
                    )

            dp[n_index][k_index] = min_switches

    min_result = inf
    for i in range(n):
        min_result = min(
            min_result,
            dp[0][i]
        )
    print(min_result)


n, m = list(map(int, input().split()))

keyboard_cache = [[False] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    notes = list(map(int, input().split()))[1:]
    for note in notes:
        keyboard_cache[i][note] = True

notes = list(map(int, input().split()))

solve_top_down()
# solve_bottom_up()
