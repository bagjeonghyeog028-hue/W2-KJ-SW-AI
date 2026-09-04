def make_change_greedy(change, coins):
    result = {}
    total_coins = 0

    for coin in coins:
        count = change // coin
        if count > 0:
            result[coin] = count
            total_coins += count
            change %= coin

    return total_coins, result

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    change1 = 1260
    coins1 = [500, 100, 50, 10]
    total, details = make_change_greedy(change1, coins1)
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change1}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
    
    # 테스트 케이스 2
    change2 = 4570
    coins2 = [500, 100, 50, 10]
    total, details = make_change_greedy(change2, coins2)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change2}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
    
    # 테스트 케이스 3
    change3 = 1000
    coins3 = [500, 100, 50, 10]
    total, details = make_change_greedy(change3, coins3)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change3}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")

"""
내가 한거.
def make_change_greedy(change, coins):
    a = 0
    b = 0
    c = 0
    d = 0

    while change > 0:
        if coins[0] <= change:
            change -= coins[0]
            a += 1
        elif coins[1] <= change:
            change -= coins[1]
            b += 1
        elif coins[2] <= change:
            change -= coins[2]
            c += 1
        elif coins[3] <= change:
            change -= coins[3]
            d += 1
        else:
            break
    result = {}
    total_coins = 0
    total_coins = {
    coins[0] : a,
    coins[1] : b,
    coins[2] : c,
    coins[3] : d
    }
    result = a + b + c + d
    return result,total_coins
"""