# -*- coding: utf-8 -*-

from BlastManFunction.ValueMode import DeduplicationValueModeJudge

def DoubleValueModeJudge(value_dict):

	if value_dict["mark_username"] is None:
		print("Username tag cannot be empty,-u option")
		sys.exit()
	else:
		count = DeduplicationValueModeJudge.DoubleDeduplication(value_dict["request_file"],value_dict["mark_username"])
		if count != 1:
			print("Username is mislabeled or not unique,-u option")
			sys.exit()

	if value_dict["mark_password"] is None:
		print("Password tag cannot be empty,-p option")
		sys.exit()
	else:
		count = DeduplicationValueModeJudge.DoubleDeduplication(value_dict["request_file"],value_dict["mark_password"])
		if count != 1:
			print("Username is mislabeled or not unique,-p option")
			sys.exit()

	if value_dict["username_file"] is None:
		print("Username column cannot be empty, -U option")
		sys.exit()
	else:
		try:
			fopen = open(value_dict["username_file"], "r")
			content = fopen.read(100)
			fopen.close()
			if len(content) == 0:
				print("Username list is empty,-U option")
				sys.exit()
		except OSError:
			print("Username list error,-U option")
			sys.exit()
		value_username = value_dict["username_file"]

	if value_dict["password_file"] is None:
		print("Password column cannot be empty,-p or -P option")
		sys.exit()
	else:
		try:
			fopen = open(value_dict["password_file"], "r")
			content = fopen.read(100)
			fopen.close()
			if len(content) == 0:
				print("Password list is empty,-U option")
				sys.exit()
		except OSError:
			print("Password list error,-U option")
			sys.exit()
		value_password = value_dict["password_file"]

	value_dict["value_username"] = value_username
	value_dict["value_password"] = value_password
	value_dict["mark_single_Greater_than_0"] = False
	value_dict["mark_single_variable_Greater_than_0"] = ""
	value_dict["username_variable"] = None

	return  value_dict
