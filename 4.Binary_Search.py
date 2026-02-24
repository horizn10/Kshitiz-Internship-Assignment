def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] 
    try:
        target = int(input("Enter the target element: "))
        index = binary_search(sorted_array, target)
        
        if index != -1:
            print(f"Element {target} is found at index {index}.")
        else:
            print(f"Element {target} is not in the array.")
    except ValueError:
        print("Please enter a valid number.")