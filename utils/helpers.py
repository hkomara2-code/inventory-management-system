# Lambda (anonymous function)
apply_discount = lambda price: price * 0.9   # 10% discount


# Recursion (Merge Sort by price)
def merge_sort(products):
    if len(products) <= 1:
        return products

    mid = len(products) // 2
    left = merge_sort(products[:mid])
    right = merge_sort(products[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].price < right[j].price:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# File handling
def save_receipt(cart):
    try:
        with open("receipt.txt", "w") as f:
            total = 0
            for item in cart:
                f.write(f"{item.name} - Rs.{item.price}\n")
                total += item.price
            f.write(f"\nTotal: Rs.{total}")
    except Exception as e:
        print("Error saving receipt:", e)