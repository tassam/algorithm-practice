
def main():
    
    # 配列の個数取得
    arrangemant_count = int(input())
    
    # 配列取得
    arrangemant = input().split()
    
    # 比較対象の数取得
    compared_count = int(input())

    # 比較処理の実行
    judge_number(compared_count, arrangemant)

# 比較処理の実行
def judge_number(compared_count,arrangemant):

    # 取得した配列分をループ
    for number in range(compared_count):

        # 比較対象の取得
        compared_number = get_compared_number()
        
        # 二部探索
        _judge = binary_search(arrangemant, compared_number)
        
        # 探索判定
        if _judge:
            print("Yes")
        else:
            print("No")
        
# 比較対象の取得
def get_compared_number():
    compared_number = int(input())
    return compared_number

# 二部探索
def binary_search(arrangemant, compared_number):
    
    # 配列の最大index値取得
    right = len(arrangemant) - 1
    
    # 配列の最小index値取得
    left = 0

    # 探索実行
    while left <= right:
        
        # 中央値の取得
        median = int((right + left) / 2)
    
        # 中央値と同値か判定
        if int(arrangemant[median]) == compared_number:
            return True
        else:

            # 中央値より大きいか小さいか
            if int(arrangemant[median]) < compared_number:
                # 最小値を再設定
                left = median + 1
            else:
                # 最大値を再設定
                right = median - 1
    
    return False

if __name__ == "__main__":
    main()
