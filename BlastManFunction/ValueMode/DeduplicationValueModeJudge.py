# -*- coding: utf-8 -*-

def SingleDeduplication(request_file,mark_variable):
	mark_dic = {}
	mark_dic["Greater_than_0"] = False
	mark_dic["variable_Greater_than_0"] = ""

	if mark_variable is None:
		print("Variable tag cannot be empty,-M option")
		sys.exit()
	else:
		fopen = open(request_file, "r")
		request_file_content = fopen.read()
		fopen.close()
		count = request_file_content.count(mark_variable)
		if count == 0:
			print("Variable is mislabeled,-M option")
			sys.exit()
		elif count > 1:
			mark_dic["Greater_than_0"] = True
			request_file_content_list = request_file_content.split(mark_variable)
			mark = ""
			i = 0
			c = 0
			print("There are multiple burst points,please specify the blasting point, enter the serial number:")			
			for line in request_file_content_list:
				c += 1
				i += 1
				if len(request_file_content_list) != c:
					print("%s %s %s%s%s" % (i,":",line,mark_variable,"\n"))
			keyboard_input = input("Enter the serial number: ")
			for key in range(int(keyboard_input)):
				mark = mark + request_file_content_list[key] + mark_variable
			mark_dic["variable_Greater_than_0"] = mark

	return mark_dic

def DoubleDeduplication(request_file,mark_variable):
		fopen = open(request_file, "r")
		request_file_content = fopen.read()
		fopen.close()
		count = request_file_content.count(mark_variable)
		return count
