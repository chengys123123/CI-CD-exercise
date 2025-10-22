from app.app import deduplicate

def test_deduplicate():
    # 测试基本去重功能
    assert deduplicate([1, 2, 2, 3]) == [1, 2, 3]
    
    # 测试空列表
    assert deduplicate([]) == []
    
    # 测试没有重复的情况
    assert deduplicate([1, 2, 3]) == [1, 2, 3]
    
    # 测试字符串去重
    assert deduplicate(['a', 'b', 'b', 'c']) == ['a', 'b', 'c']
    
    print("All tests passed!")


# 在原有测试基础上添加：
def test_addition():
    from app.app import add_numbers
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0