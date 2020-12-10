
def getCount(root, l, h):
    if root == None:
        return 0 
    elif root.data <= h and root.data >= l:
        return 1 + getCount(root.left, l, h) + getCount(root.right, l, h)
    elif root.data > h:
        return getCount(root.left, l, h)
    else: 
        return getCount(root.right, l, h)
