import sys
input = sys.stdin.readline


def get_rider_cnt(M, a, time):

    sum_p = M
    for c in a:
        sum_p += time // c
    return sum_p


def get_time(N, M, a, MAX_PT):
    time = 0
    lt = 0
    rt = N // M * MAX_PT

    while lt <= rt:
        mid = (lt + rt) // 2
        sum_p = get_rider_cnt(M, a, mid)
        if sum_p >= N:
            rt = mid - 1
            time = mid
        else:
            lt = mid + 1

    return time

# 마지막 아이가 탑승한 놀이 기구의 번호반환
def get_last_ride(N, M, a, time):
    rider_cnt = get_rider_cnt(M, a, time - 1)
    for i in range(M):
        if time % a[i] == 0:
            rider_cnt += 1
        if rider_cnt == N:
            return i+1


if __name__ == "__main__":
    MAX_PT = 30
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    time = get_time(N, M, a, MAX_PT)
    # 0분에 모든 아이들이 탑승 가능하면 N번 놀이 기구가 마지막 번호가 됨
    if time == 0:
        print(N)
    else:
        print(get_last_ride(N, M, a, time))