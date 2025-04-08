N, A = (int(i) for i in input().split())
nums = list(int(i) for i in input().split())

def count_ways(N, A, nums):

    def helper(prev_sum, prev_count, i):
        if i == N:
            return 0

        # pick ith card or don't pick ith
        pick_sum, pick_count = prev_sum + nums[i], prev_count + 1

        if pick_sum / pick_count == A:
            count = 1
        else:
            count = 0

        return count + helper(pick_sum, pick_count, i+1) + helper(prev_sum, prev_count, i+1)

    return helper(0, 0, 0)


def count_ways_dp(N, A, nums):

    count_ways = [[[ None for _ in range(sum(nums))] for _ in range(N)] for _ in range(N)]

    nums.sort()
    def helper(prev_sum, prev_count, i):

        if i == N:
            return 0

        if prev_count > 0:
            current_average = prev_sum / prev_count
            if current_average > A:
                return 0

        if count_ways[prev_count][i][prev_sum]:
            return count_ways[prev_count][i][prev_sum]

        new_avg = (prev_sum+nums[i]) / (prev_count+1)

        ans = int(new_avg == A) + helper(prev_sum+nums[i], prev_count+1, i+1) + helper(prev_sum, prev_count, i+1)
        count_ways[prev_count][i][prev_sum] = ans
        return ans

    return helper(0, 0, 0)

def binomial_coeff(N: int) -> list[list[int]]:
    coeff = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N+1):
        coeff[i][0] = coeff[i][i] = 1

    for n in range(N+1):
        for k in range(1, n):
            coeff[n][k] = coeff[n-1][k-1] + coeff[n-1][k]

    return coeff

from collections import Counter
def quick(N, A, nums):
    counter = Counter(nums)
    pairs = list(counter.items())
    pairs.sort()
    coeff = binomial_coeff(N)
    ans = []
    count_ways = [[[ None for _ in range(sum(nums))] for _ in range(N)] for _ in range(N)]
    def helper(i, prev_sum, prev_count):
        if i == len(pairs):
            return 0
        if count_ways[i][prev_count][prev_sum]:
            return count_ways[i][prev_count][prev_sum]
        val, count = pairs[i]
        total = 0
        for k in range(0, count+1):
            bc = coeff[count][k]
            new_sum, new_count = prev_sum+k*val, prev_count+k
            if k != 0 and new_count > 0 and new_sum/new_count == A:
                ans.append((new_sum, new_count, k, bc, val, count))
                total += bc
            if new_count > 0 and new_sum/new_count > A:
                continue
            total += bc*helper(i+1, new_sum, new_count)
        count_ways[i][prev_count][prev_sum] = total
        return total
    a = helper(0, 0, 0)
    return a

# print(count_ways_dp(N, A, nums))
print(quick(N, A, nums))
