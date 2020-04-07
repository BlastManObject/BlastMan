# -*- coding: utf-8 -*-

from BlastManFunction.ValueMode import DeduplicationValueModeJudge

def DoubleValueModeJudge(request_file, mark_username, mark_password, username_file, password_file, value_dict):

	if mark_username is None:
		print("Username tag cannot be empty,-u option")
		sys.exit()
	else:
		count = DeduplicationValueModeJudge.DoubleDeduplication(request_file,mark_username)
		if count != 1:
			print("Username is mislabeled or not unique,-u option")
			sys.exit()

	if mark_password is None:
		print("Password tag cannot be empty,-p option")
		sys.exit()
	else:
		count = DeduplicationValueModeJudge.DoubleDeduplication(request_file,mark_password)
		if count != 1:
			print("Username is mislabeled or not unique,-p option")
			sys.exit()

	if username_file is None:
		print("Username column cannot be empty, -U option")
		sys.exit()
	else:
		try:
			fopen = open(username_file, "r")
			content = fopen.read(100)
			fopen.close()
			if len(content) == 0:
				print("Username list is empty,-U option")
				sys.exit()
		except OSError:
			print("Username list error,-U option")
			sys.exit()
		value_username = username_file

	if password_file is None:
		print("Password column cannot be empty,-p or -P option")
		sys.exit()
	else:
		try:
			fopen = open(password_file, "r")
			content = fopen.read(100)
			fopen.close()
			if len(content) == 0:
				print("Password list is empty,-U option")
				sys.exit()
		except OSError:
			print("Password list error,-U option")
			sys.exit()
		value_password = password_file

	value_dict["mark_username"] = mark_username
	value_dict["mark_password"] = mark_password
	value_dict["value_username"] = value_username
	value_dict["value_password"] = value_password
	value_dict["mark_single_Greater_than_0"] = False
	value_dict["mark_single_variable_Greater_than_0"] = ""
	value_dict["username_variable"] = None

	return  value_dict
