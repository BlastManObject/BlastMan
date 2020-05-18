# -*- coding: utf-8 -*-

from BlastManFunction.ValueMode import DeduplicationValueModeJudge

def SingleValueModeJudge(value_dict):
	mark_dic = DeduplicationValueModeJudge.SingleDeduplication(value_dict["request_file"],value_dict["mark_single_variable"])

	if value_dict["single_variable_file"] is not None:
		try:
			fopen = open(value_dict["single_variable_file"], "r")
			content = fopen.read(100)
			fopen.close()
			if len(content) == 0:
				print("Variable list is empty,-c option")
				sys.exit()
		except OSError:
			print("Variable list error,-c option")
			sys.exit()
	else:
		print("Variable list error,-c option")
		sys.exit()

	value_dict["mark_single_Greater_than_0"] = mark_dic["Greater_than_0"]
	value_dict["mark_single_variable_Greater_than_0"] = mark_dic["variable_Greater_than_0"]

	return value_dict
