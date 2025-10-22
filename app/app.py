def deduplicate(items):
    """去除列表中的重复元素"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    # 测试代码
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    result = deduplicate(sample_list)
    print(f"Original: {sample_list}")
    print(f"After deduplication: {result}")

def add_numbers(a, b):
    return a + b

# 如果这是主要执行文件，可以添加：
if __name__ == "__main__":
    print("Addition function is ready!")
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")