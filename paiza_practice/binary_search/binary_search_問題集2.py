
import bisect

def main():

    # 生徒の数取得
    student_count = int(input())
    
    # 各生徒の点数
    student_test_count = input().split()
    student_test_count = [int(s) for s in student_test_count]
    student_test_count.sort()
    
    # 比較数
    compared_count = int(input())
    
    # 比較数分ループ
    for i in range(compared_count):
        
        # 合格点取得
        pass_number = int(input())
        
        # 挿入位置取得
        count = bisect.bisect_left(student_test_count , pass_number)

        # 合格した生徒の数
        pass_student_number = student_count - count
        print(pass_student_number)
    
if __name__ == '__main__':
    main()

