import turtle as t


class node:
	def __init__(self, data):
		self.left = None
		self.data = data
		self.right = None


def insert(root, data):
	if root is None:
		root = node(data)
	else:
		if data <= root.data:
			if root.left is None:
				root.left = node(data)
			else:
				root.left = insert(root.left, data)
		else:
			if root.right is None:
				root.right = node(data)
			else:
				root.right = insert(root.right, data)
	return root


def in_order(root):
	if root:
		in_order(root.left)
		print(root.data)
		in_order(root.right)

def tur():
	t.speed(1)
	t.right(90)
	t.penup()
	#t.backward(350)
	t.pendown()
	

def turt(root, length):
	distance = 200/length
	angle = 90 / length
	if root:
		if root.left:
			t.penup()
			t.right(angle)
			t.forward(20)
			t.pendown()
			t.forward(distance)
			t.penup()
			t.forward(20)
			t.pendown()
			turt(root.left, length+1)
			t.penup()
			t.backward(20)
			t.backward(distance)
			t.backward(20)
			t.left(angle)
			t.pendown()
			#left
		t.penup()
		t.write(root.data, align='center')
		t.pendown()
		#root
		if root.right:
			t.penup()
			t.left(angle)
			t.forward(20)
			t.pendown()
			
			t.forward(distance)
			t.penup()
			t.forward(20)
			t.pendown()
			turt(root.right, length+1)
			t.penup()
			t.backward(20)
			t.backward(distance)
			
			t.backward(20)
			t.right(angle)
			t.pendown()
			#right


	

r = None
print("inorder will be printed every time")
while True:
	print("\npress 1 to insert")
	print("press 2 to exit")
	print("press 3 to draw")
	a = int(input())
	if a == 1:
		data = int(input("\nEnter data:"))
		r = insert(r, data)
	elif a == 3:
		tur()
		turt(r, 1)
		t.hideturtle()
		t.exitonclick()
		t.mainloop()
	else:
		break
	in_order(r)


