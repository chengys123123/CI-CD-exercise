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




def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def add_numbers(a, b):
    """Add two numbers together"""
    return a + b

if __name__ == '__main__':
    sample = [1, 2, 3, 1, 2, 5]
    print(f"Original: {sample}")
    print(f"Deduplicated: {list(dedupe(sample))}")
    print(f"Addition test: 2 + 3 = {add_numbers(2, 3)}")