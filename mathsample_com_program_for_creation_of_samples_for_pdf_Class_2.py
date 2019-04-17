# PG80 Math App!!!

# levels
# Beginner_jump
# Easy_jump
# Standart_jump
# Hardcore_jump
# Professional_jump

import random
from PG80_Math_program_Data_info import Easy_jump
#    Standart_jump, Hardcore_jump, Professional_jump

Easy_jump_for_use = Easy_jump

class BasicLogicForFirstApp:

    def __init__(self, serial_number, number01, sign, number02, equals_sign, answer):
        self.serial_number = serial_number
        self.number01 = number01
        self.sign = sign
        self.number02 = number02
        self.equals_sign = equals_sign
        self.answer = answer

    def check_answer(self, try_answer):
        return try_answer == self.answer

question_list = []

for serial_number, number01, sign, number02, equals_sign, answer in Easy_jump_for_use:
#    Beginner_jump_for_use = Beginner_jump

    Beginner_jump_for_use_item = random.choice(Easy_jump_for_use)
    print('{} {} {} {} ____'.format(*Beginner_jump_for_use_item[1:]))
   # print(number01, sign, number02, equals_sign, '___')

    current_question = BasicLogicForFirstApp(serial_number, number01, sign, number02, equals_sign, answer)
    question_list.append(current_question)




















#    print(number01, sign, number02, equals_sign, '___')


#    print(number01, sign, number02, equals_sign, '___')
#    print(Beginner_jump_for_use_item['number01'])
#    print (random.choice(number01), random.choice(sign), random.choice(number02), random.choice(equals_sign), '___')
 #   print(random.choice (for serial_number, number01, sign, number02, equals_sign, answer in Beginner_jump_for_use))

#    print((random.choice(number01), (random.choice(sign)))


#    if current_question.check_answer(input('What answer?')):
#        first_is_correct_some_good_worlds = [
#        'Unbelievable!',
#        'Super!',
#        ]
#        print(random.choice(first_is_correct_some_good_worlds))
#
#    elif current_question.check_answer(input('Try, one more')):
#        print('Excellent, Street forward!')
#
#    elif current_question.check_answer(input('Try, last time')):
#        print('Good job, Street ahead!')
#
#    else:
#        print(number01, sign, number02, equals_sign, answer)
#
#        motivated_worlds = [
#            'Do not worry, street ahead!',
#            'Opportunities don’t happen, you create them',
#        ]
#        print(random.choice(motivated_worlds))
#        incorrect = []
#        incorrect.append(current_question)


#print('Pipe_outer_diameter_', (Pipes_for_test_365['Pipe_365.12']['OD']), '  Pipe_wall_thickness',
 #     (Pipes_for_test_365['Pipe_365.12']['WT']), '  Pipe_length', (Pipes_for_test_365['Pipe_365.12']['length']))


#import random
#movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']
#moview_item = random.choice(movie_list)
#print ("Randomly selected item from list is - ", moview_item)


#Easy_jump_for_use = Easy_jump
#Standart_jump_for_use = Standart_jump
#Hardcore_jump_for_use = Hardcore_jump
#Professional_jump_for_use = Professional_jump




