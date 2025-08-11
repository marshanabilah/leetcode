from typing import List

def find_missing_numbers(nums: List[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def main():
    nums = [3,4,2,0,5]
    missing_number = find_missing_numbers(nums)
    print(f"The missing number is: {missing_number}")

if __name__ == "__main__":
    main()
