import random
import os
#print(os.getcwd())
#capitals = {'Bihar' : 'Patna', 'Odisha' : 'Bhubaneswar', 'Sikkim' : 'Gangtok', 'Assam' : 'Dispur', 'Jharkhand' : 'Ranchi', 'West Bengal' : 'Kolkata', 'Uttar Pradesh' : 'Lucknow', 'Maharashtra' : 'Mumbai', 'Karnataka' : 'Bengaluru', 'Punjab' : 'Chandigarh'}
#create the above dictionary from a text file
capitals = {}
with open('capitals.txt', 'r') as f:
    for line in f:
        words = line.split()
        if len(words) == 3:
            key = words[0] + ' ' + words[1]
            val = words[2]
            capitals[key] = val
        else:
            capitals[words[0]] = words[1]


#create 4 sets of questionbank
for quizNum in range(4):
    quFile = open('quiz%s.txt' % (quizNum + 1), 'w')
    ansFile = open('quiz_answers%s.txt' % (quizNum + 1), 'w')
    quFile.write((' ' * 20) + 'State Capitals Quiz (Set %s)' % (quizNum + 1))
    quFile.write('\n\n')
    quFile.write('Name:\n\nDate:\n\n')
    states = list(capitals.keys())
    random.shuffle(states)
    for qnum in range(10):
        correctAns = capitals[states[qnum]]
        wrongAns = list(capitals.values())
        del wrongAns[wrongAns.index(correctAns)]
        wrongAns = random.sample(wrongAns, 3)
        answerOptions = wrongAns + [correctAns]
        random.shuffle(answerOptions)
        
        quFile.write('%s. What is the capital of %s?\n\n' % (qnum + 1,states[qnum]))
        for i in range(4):
            quFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            #quFile.write('\n')
            # Write the answer key to a file.
        quFile.write('\n')
        ansFile.write('%s. %s\n' % (qnum + 1, 'ABCD'[answerOptions.index(correctAns)]))
    quFile.close()
    ansFile.close()
print('Quiz prepared')