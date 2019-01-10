#! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key


import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
    'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
    'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for i in range(35):
    Qz = open("Files\\Quiz\\CapitalQuiz%s.txt" %(i+1),"w")
    AnsQz = open("Files\\Quiz\\AnswerKey_CapitalQuiz%s.txt" %(i+1),"w")

    # Write out the header for the quiz.
    Qz.write('Name:\n\nDate:\n\nPeriod:\n\n')
    Qz.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (i + 1))
    Qz.write('\n\n')

    temp_key = list(capitals.keys())
    random.shuffle(temp_key)
    count=1
    for j in temp_key:
        Qz.write(str(count)+". "+"What is the capital of "+j+"?"+"\n")
        temp_value = list(capitals.values())
        temp_value.remove(capitals[j])
        AnswerOptions = random.sample(temp_value,3) + [capitals[j]]     # Good Find
        random.shuffle(AnswerOptions)
        Qz.write("\t"+"A. "+AnswerOptions[0]+"\n")      # Alternative way. Use 'ABCD'[0]
        Qz.write("\t"+"B. "+AnswerOptions[1]+"\n")      # Alternative way. Use 'ABCD'[1]
        Qz.write("\t"+"C. "+AnswerOptions[2]+"\n")      # Alternative way. Use 'ABCD'[2]
        Qz.write("\t"+"D. "+AnswerOptions[3]+"\n")      # Alternative way. Use 'ABCD'[3]
        Qz.write("\n\n")
        Answer = chr(65+AnswerOptions.index(capitals[j]))   # Alternative way. Use 'ABCD'[AnswerOptions.index(capitals[j])]
        AnsQz.write(str(count)+". "+Answer+"\n")
        count +=1
    Qz.close()
    AnsQz.close()
