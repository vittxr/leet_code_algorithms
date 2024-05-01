from solution import Solution, TreeNode

s = Solution()

root1 = TreeNode(val=0, left=TreeNode(val=-10), right=TreeNode(val=10))
root2 = TreeNode(
    val=5,
    left=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=2)),
    right=TreeNode(val=7),
)

# print(s.getAllElements(root1, root2))

root1 = TreeNode(
    val=99,
    left=TreeNode(
        val=90,
        left=TreeNode(
            val=8, left=TreeNode(val=7), right=TreeNode(val=85, right=TreeNode(val=87))
        ),
        right=None,
    ),
    right=None,
)

root2 = TreeNode(
    val=50,
    left=TreeNode(
        val=2,
        right=TreeNode(val=34, left=TreeNode(val=21, left=TreeNode(val=10))),
    ),
    right=TreeNode(
        val=73,
        left=TreeNode(
            val=58,
            right=TreeNode(val=64, right=TreeNode(val=68, left=TreeNode(val=66))),
        ),
        right=TreeNode(
            val=80,
            left=TreeNode(val=74),
            right=TreeNode(
                val=92,
                left=TreeNode(val=89, left=TreeNode(val=84)),
                right=TreeNode(val=100),
            ),
        ),
    ),
)

print(s.getAllElements(root1, root2))
