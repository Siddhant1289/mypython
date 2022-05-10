print("welcome to library management system")
print("press 1 for student")
print("press 2 for course")
print("press 3 for books")
print("press 4 for issue")
print("press 5 for return")
print("enter your choice!!!")
x=int(input())
if x==1:
	print("press 1 for saving a new student")
	print("press 2 for find a student according to rollno")
	print("press 3 for delete a student")
	print("press 4 for update an existing student")
	y=int(input('enter your choice'))
	if y==1:
		import student_data
	elif y==1:
		import student_find
	elif y==2:
		import student_delete
elif x==2:
	print("press 1 for saving a new course")
	print("press 2 for find a course")
	print("press 3 for delete a course")
	print("press 4 for update a course")
	y=int(input('enter your choice'))
	if y==1:
		import course_info
	elif y==2:
		import course_find	
	elif y==3:
		import course_delete	
elif x==3:
	print("press 1 for saving a new book")
	print("press 2 for find a book according to bookid")
	print("press 3 for delete a book")
	print("press 4 for update an existing book")
	y=int(input('enter your choice'))
	if y==1:
		import book_details
	elif y==2:
		import book_find	
	elif y==3:
		import book_delete
elif x==4:
	print("press 1 for saving a new issued entry")
	print("press 2 for find a issued entry ")
	print("press 3 for delete a issued entry")
	print("press 4 for update an existing issued")
	y=int(input('enter your choice'))
	if y==1:
		import issue_details
	elif y==2:
		import issue_find
	elif y==3:
		import issue_delete
elif x==5:
	print("press 1 for saving a return")
	print("press 2 for find a return")
	print("press 3 for delete a return")
	print("press 4 for update an existing return")
	y=int(input('enter your choice'))
	if y==1:
		import returns_details
	elif y==2:
		import returns_find	
	elif y==3:
		import course_delete
else:
	print("out of library management")	