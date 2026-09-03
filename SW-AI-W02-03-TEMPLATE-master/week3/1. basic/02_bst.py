class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def search_bst(root, target):
    if root is None:    # TODO: root가 None이면 False 반환
        return False
    if root.value == target:
        return True
    if root.value > target:
        return search_bst(root.left,target)
    if root.value < target:
        return search_bst(root.right, target)
      # TODO: 값을 찾으면 True 반환
    ## target이 작으면 왼쪽 서브트리에서 검색
    ## target이 크면 오른쪽 서브트리에서 검색



# 테스트 케이스
if __name__ == "__main__":
    # BST 생성:
    #       5
    #      / \
    #     3   7
    #    / \
    #   2   4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    
    print("=== 이진 검색 트리 ===")
    print("트리 구조: 5를 루트로 하는 BST")
    
    test_values = [2, 4, 5, 6, 7]
    for val in test_values:
        result = search_bst(root, val)
        print(f"값 {val} 검색: {result}")


