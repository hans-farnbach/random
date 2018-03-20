# simple offline survey program I wrote for my brother; with a file containing questions (with certain syntax
# dictating how questions can be answered), will endlessly cycle through the questions so user can run simple surveys
question_file = ""				# file containing questions
output_file = ""				# output file; CSV for Excel spreadsheet
thanks_message = "Thanks for your time!"	# final message to user

survey_questions = {}
survey = []

with open(question_file) as f:
	data = f.readlines()
	
previous_q = ""		# keep track in case there are options for the question

# build question list
for line in data:							
	line = line.strip("\n")
	if "\t" in line:		# there are options
		survey_questions[previous_q].append(line)
	else:				# free response
		survey_questions[line] = []
		survey.append(line)
		previous_q = line

with open(output_file, "w") as f:	# start the CSV with questions as the headers
	f.write("Name")
	for q in survey_questions:
		f.write("," + q)
	f.write("\n")

while True:
	responses = []				# keep track of one respondents responses to each question
	response = ""
	name = input("Name: ")
	if name == "DoNe":			# quit survey
		quit()
	for q in survey:			# go through the question list we built earlier
		if not survey_questions[q]:
			print(q)
			response = input("> ")
		else:
			print(q)
			# exclusive options
			if "\t\t" in survey_questions[q][0]:
				print("Please select one.")
				exclusive = True
			else:
				print("Please select all that apply, e.g. 134")
				exclusive = False
			# list options, prepended by "1", "2", "3", etc.
			for index, answer in enumerate(survey_questions[q]):
				answer = answer.strip()
				print("\t" + str(index+1) + ": " + answer)
			invalid = True
			# make sure the response is selecting an option
			while invalid:
				response = input("> ")
				# make sure it's just one option
				while exclusive and len(response) > 1:
					print("Please select only one.")
					response = input("> ")
				try:
					int(response)
					invalid = False
				except ValueError:
					print("Please input just numbers, e.g. 123")
			final_response = ""
			for index, character in enumerate(response):
				# non-zero will be prepended by "||" to split up multiple answers
				if index:
					final_response += "||"
				answer = int(character) - 1
				# possible option out of bounds
				try:
					final_response += survey_questions[q][answer].strip("\t")
				except IndexError:
					pass
			response = final_response
		responses.append(response)
	# done
	print(thanks_message)
	# write responses to output file, then start again
	with open(output_file, "a") as f:
		f.write(name)
		f.write(",".join(response) + "\n")
