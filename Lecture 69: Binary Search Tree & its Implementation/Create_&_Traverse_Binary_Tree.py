class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def insertIntoBST(root, data):
	# Base Case
	if(root == None):
		root = Node(data)
		return root
	if(data < root.data):
		root.left = insertIntoBST(root.left, data)
	else:
		root.right = insertIntoBST(root.right, data)
	return root


def takeInput(root):
	data = int(input())  
	while(data != -1):
		root = insertIntoBST(root, data)
		data = int(input())
	return root


def levelOrderTraversal(root):
	q = []
	q.append(root)
	q.append(None)

	while(len(q) != 0):
		temp = q[0]
		q.pop(0)

		if(temp == None):
			print()
			if(len(q) != 0):
				q.append(None)

		else:
			print(temp.data, end = ' ')
			if(temp.left):
				q.append(temp.left)
			if(temp.right):
				q.append(temp.right)

def inOrderTraversal(root): # L N R
	# Base Case
	if(root == None):
		return
	inOrderTraversal(root.left)
	print(root.data, end = ' ')
	inOrderTraversal(root.right)
  

def preOrderTraversal(root): # N L R
	# Base Case
	if(root == None):
		return
	print(root.data, end = ' ')
	preOrderTraversal(root.left)
	preOrderTraversal(root.right)
  

def postOrderTraversal(root): # L R N
	# Base Case
	if(root == None):
		 return
	postOrderTraversal(root.left)
	postOrderTraversal(root.right)
	print(root.data, end = ' ')


def main():

	root = None

	print("Enter data to create BST : ")
	root = takeInput(root)

	# Level Order
	print("Printing the BST in Level Order Traversal : ")
	levelOrderTraversal(root)
	print()

	# Inorder
	print("Printing the BST in IN-Order Traversal : ")
	inOrderTraversal(root)
	print()

	#PreOrder
	print("Printing the BST in Pre Order Traversal : ")
	preOrderTraversal(root)
	print()

	# PostOrdr
	print("Printing the BST in Level Order Traversal : ")
	postOrderTraversal(root)
	print()


if __name__ == '__main__':
	main()
