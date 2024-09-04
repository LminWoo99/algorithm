def solution(coin, cards):
    N = len(cards)
    hand = dict()
    coin1cnt = coin2cnt = 0
    for i in range(N//3):
        if hand.get(N+1-cards[i]):
            coin1cnt += 1
        else:
            hand[cards[i]] = True

    draw = dict()
    for i in range(N//3, N, 2):
        for j in range(i, i+2):
            draw[cards[j]] = True
            if hand.get(N+1-cards[j]) and coin > 0:
                coin1cnt += 1
                coin -= 1
            if draw.get(N+1-cards[j]):
                coin2cnt += 1
        if coin1cnt > 0:
            coin1cnt -= 1
        elif coin2cnt > 0 and coin > 1:
            coin2cnt -= 1
            coin -= 2
        else:
            return (i-N//3)//2+1
    return (N-N//3)//2+1