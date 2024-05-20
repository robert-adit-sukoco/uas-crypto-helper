def is_primitive_root(p, q):
    nums = []
    for i in range(1, q):
        num = (p ** i) % q
        if num in nums:
            return False, []
        nums.append(num)
    return True, nums

def find_primitive_root(n: int):
    return_dict = dict()
    for i in range(2, n):
        is_pr, nums = is_primitive_root(i, n)
        if is_pr:
            return_dict[i] = nums

    return return_dict

def primitive_root_members(p, q):
    flag, results = is_primitive_root(p, q)
    if flag:
        return results
    return []

if __name__ == "__main__":
    print(find_primitive_root(13))
