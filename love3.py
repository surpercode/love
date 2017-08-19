# I am Douyaguang
# I love Wangwenjing forever!
# This script is written in 2017/8/10
# I will run it in front of wenjing today
# Give me good luck!!!
# newly modified in 2017/8/19 by Douyaguang

from functools import reduce
import re
import random
import time

mylove = '''


               WWWWW                  WWWWW      EEEEEEEEEEEEEEEEEEE      NNNNNN          NNNNNN
               WWWWW                 WWWWW       EEEEEEEEEEEEEEEEEEE      NNNNNNN         NNNNNN 
                WWWWW      WWWWW    WWWWW       EEEEE                    NNNNNNNNN       NNNNNN  
                WWWWW     WWWWWW   WWWWW        EEEEE                    NNNNNN NNN      NNNNNN  
                 WWWWW   WWW WWW  WWWWW        EEEEEEEEEEEEEEEEEEE      NNNNNN   NNN    NNNNNN   
                 WWWWW  WWW  WWW WWWWW         EEEEEEEEEEEEEEEEEEE      NNNNNN    NNN   NNNNNN   
                  WWWWWWWW   WWWWWWWW         EEEEE                    NNNNNN      NNN NNNNNN     
                  WWWWWWW    WWWWWWW          EEEEE                    NNNNNN       NNNNNNNNN     
                   WWWWW     WWWWWW          EEEEEEEEEEEEEEEEEEE      NNNNNN         NNNNNNN      
                   WWWWW     WWWWW           EEEEEEEEEEEEEEEEEEE      NNNNNN          NNNNNN      


                              JJJJJJ           IIIIII         NNNNNN          NNNNNN             GGGGGGGGG          
                              JJJJJJ           IIIIII         NNNNNNN         NNNNNN          GGGGGGGGGGGGGGGG    
                              JJJJJJ          IIIIII         NNNNNNNNN       NNNNNN        GGGGGG         GGGGGG  
                              JJJJJJ          IIIIII         NNNNNN NNN      NNNNNN       GGGGGG           GGGGGG 
                              JJJJJJ         IIIIII         NNNNNN   NNN    NNNNNN       GGGGGG                   
               JJJJJJ         JJJJJJ         IIIIII         NNNNNN    NNN   NNNNNN       GGGGGG        GGGGGGGGG  
               JJJJJJ         JJJJJJ        IIIIII         NNNNNN      NNN NNNNNN         GGGGGG       GGGGGGGGG  
                JJJJJJ       JJJJJJ         IIIIII         NNNNNN       NNNNNNNNN          GGGGGG           GGGG  
                 JJJJJJJJJJJJJJJJ          IIIIII         NNNNNN         NNNNNNN            GGGGGGGGGGGGGGG GGGG  
                     JJJJJJJJJJ            IIIIII         NNNNNN          NNNNNN               GGGGGGGGGGGG GGGG  

                                                             IIIIII   
                                                             IIIIII  
                                                            IIIIII  
                                                            IIIIII  
                                                           IIIIII   
                                                           IIIIII   
                                                          IIIIII   
                                                          IIIIII    
                                                         IIIIII     
                                                         IIIIII      


                   LLLLLL                     OOOOOO         VVVVVV            VVVVVV    EEEEEEEEEEEEEEEEEEE 
                   LLLLLL                 OOOOOOOOOOOO       VVVVVV           VVVVVV     EEEEEEEEEEEEEEEEEEE  
                  LLLLLL               OOOOOOOOOOOOOOOOO      VVVVVV         VVVVVV     EEEEE                 
                  LLLLLL             OOOOOO        OOOOOO     VVVVVV        VVVVVV      EEEEE                 
                 LLLLLL             OOOOOO          OOOOOO     VVVVVV      VVVVVV      EEEEEEEEEEEEEEEEEEE    
                 LLLLLL             OOOOOO          OOOOOO     VVVVVV     VVVVVV       EEEEEEEEEEEEEEEEEEE    
                LLLLLL               OOOOOO        OOOOOO       VVVVVV   VVVVVV       EEEEE                   
                LLLLLL                OOOOOOOOOOOOOOOOO         VVVVVV  VVVVVV        EEEEE                   
               LLLLLLLLLLLLLLLLLLL      OOOOOOOOOOOO             VVVVVVVVVVVV        EEEEEEEEEEEEEEEEEEE      
               LLLLLLLLLLLLLLLLLLL        OOOOOO                 VVVVVVVVVVV         EEEEEEEEEEEEEEEEEEE      


                   YYYYYY         YYYYYY            OOOOOO              UUUUUU         UUUUUU 
                    YYYYYY      YYYYYY          OOOOOOOOOOOO           UUUUUU         UUUUUU  
                     YYYYYY   YYYYYY         OOOOOOOOOOOOOOOOO         UUUUUU         UUUUUU   
                      YYYYYYYYYYYY         OOOOOO        OOOOOO       UUUUUU         UUUUUU    
                       YYYYYYYYY          OOOOOO          OOOOOO     UUUUUU         UUUUUU     
                        YYYYYY            OOOOOO          OOOOOO     UUUUUU        UUUUUU      
                        YYYYYY             OOOOOO        OOOOOO      UUUUUU        UUUUUU      
                       YYYYYY               OOOOOOOOOOOOOOOOO         UUUUUU     UUUUUU       
                       YYYYYY                 OOOOOOOOOOOO             UUUUUUUUUUUUUU          
                      YYYYYY                    OOOOOO                   UUUUUUUU               

'''


def love_verify():
    print ('''
         Are you wenjing?
         A: yes      B: no
    ''')
    i = 0
    while(1):
        ans = input('>')
        if ans in  ['yes', 'Yes', 'Y', 'y', 'A', 'a', 'YES']:
            varify_questions()
            break
        else:
            if i == 0:
                print ('Oh, no, I only love wenjing! I do not know who are you, you can leave now please!')
            if i == 1:
                print ('Oh, no, I realy only love wenjing! I do not know who are you, Do not bother me.')
            if i == 2:
                print ('This is the third time, I realy realy realy only love wenjing! Do I express it clear enough???')
            if i >= 3:
                break
            i += 1


def varify_questions():
    print ('''
             You say you are wenjing who are my best love. I think you can also answer the following questions that only known by Douyaguang and you.''')
    input()
    questions = [
                'When is your birthday (mm-dd) by traditional Chinese calendar?',
                'When is my birthday (mm-dd) by traditional Chinese calendar?',
                'How old are you and me?',
                'How many films have we seen together, be carefull, there was a film we saw together not in cinema?',
                'When did I declare the love and make love confession for you? (yyyy-mm-dd)',
                '''
                   What is the shape of my running track in May?
                   A 521,      B 520      C love,      D red heart shape,      E wenjing''',
                '''
                   Which of the following words are always said by you or your pet phrase? (Multiple choice)
                   A: axiba,      B: soda,      C: ni hao fan a,      D: ximada,      E:your sister,      F:lalala''',
                '''
                   Which of the folowing parks have we been here? (Multiple choice)
                   A Shanghai Gongqing National Forest Park,      B Shanghai HuangXing Park
                   C Shanghai Wild Animal Park,      D Shanghai Riverside Forest Park,      E Shanghai Century Park''',
                '''
                   When we walk together or eat together or do all the things together, which of the following things I usually do? (Multiple choice)
                   A holding your hand,      B take photos,      C can not help staring at you,      D praise your kindness and ty''',
                '''
                   Which of the following things have we played or done together? (Multiple choice)
                   A fly a kite,      B paddle a boat,      C shooting,      D runing,      E singing,      F talking late at night by phone or webchat
                   G taking jokes,      H riding bicycles,      I go to the hospital,      J talking about poems and love and the future''',
                ]
    answers = [
              ['03-03', '3-3', '03-3', '3-03', '3/3', '03/3', '3/03'],
              ['04-21', '4-21', '4/21', '04/21'],
              ['26', '18'], ## heihei, 18 old is a good age that wenjing will be forever in my heart!
              ['5', '05', '5.0'],
              ['2017-06-18', '2017-6-18', '06-18', '6-18', '2017/06/18', '2017/6/18', '06/18', '6/18'],
              ['B', 'b', '520'],
              ['ABCDE', 'abcde', 'A,B,C,D,E', 'a,b,c,d,e', 'A B C D E', 'a b c d e', 'A, B, C, D, E', 'a, b, c, d, e'],
              ['ABD', 'A B D', 'A, B, D', 'A,B,D', 'abd', 'a b d', 'a, b, d', 'a,b,d'],
              ['BCD', 'B C D', 'B, C, D', 'B,C,D', 'bcd', 'b c d', 'b, c, d', 'b,c,d'],
              ['ABCDEFGHIJ', 'abcdefghij', 'A,B,C,D,E,F,G,H,I,J', 'A B C D E F G H I J', 'A, B, C, D, E, F, G, H, I, J', 'a, b, c, d, e, f, g, h, i, j', 
               'a b c d e f g h i j', 'a,b,c,d,e,f,g,h,i,j', 'All', 'all', 'ALL']
              ]
    def check_answer(ans, i):
        if 0 <= i <= 4:
            if ans in answers[i]:
                return 1
            else:
                return 0
        if 5 <= i <= 9:
            if ans in answers[i]:
                return 1
            else:
                # sub = lambda x, y : x.replace(y, '')
                # ans_new = reduce(sub, [',', '.', ' ', '\t', '?', '%', '$', '%', '|', '!', '(', ')'], ans.upper())
                ## an alternative way to do this
                ans_new = re.sub(r'[\t,.? %&|!()]', '', ans.upper())
                if sorted(list(ans_new)) == sorted(list(answers[i][0])):
                    return 1
                else:
                    return 0

    def response_answer(ans, i):
        right = check_answer(ans, i)
        if i == 0:
            if right:
                print ('Oh yes, right! I think you know wenjing very well, come on!')
            else:
                print ('This is a big problem, you do not even kown the birthday of yourself, I must be careful.')
        elif i == 1:
            if right:
                print ('Haha, wenjing know my birthday, this is my great honor. I love you, wenjing!')
            else:
                print ('It is so disappointed, are you realy wenjing? Wenjing know my birthday but you do not. I will check you further.')
        elif i == 2:
            if right and ans == '18':
                print ('Clever, we are 18 forever, wenjing is the most beatiful girl in the world! I like this answer, wise and smart!')
            elif right and ans == '26':
                print ('Right answer, cheering! Wenjing is the most beatiful girl in the world and is 18 in my heart forever.')
            else:
                print ('Wrong, I am confused that you do not know the age of yourself. Are you really wenjing or you are just kidding me.')
        elif i == 3:
            if right:
                print ('Excellent, we have seen 5 films together, 3 times in Heshenghui, 1 time in Wanda, 1 time in JiangWan acitivity center. '
                       'The number will continue to increase, perhaps it can often record, heihei!')
            else:
                print ('I am sorry, it is not correct. Think clearly, perhaps you missed some film. I believe you can give me a right answer is '
                       'you are really wenjing.')
        elif i == 4:
            if right:
                print ('Yeah, right! This is one of the most unforgettable day in my life. I love you, I sent you gifts and wrote my love peoms '
                       'to you. I love you, I love you, I love you. I am waiting for you and your love, wenjing.')
            else:
                print ('Oh, my god, you are wrong. It is unbelievable if you are really wenjing that you can forget this import day. So I must '
                       'say that you are not wenjing in a large probability.')
        elif i == 5:
            if right:
                print ('Good answer! In 2017-05-20, I ran around the campus to creat this love track 520. I love you wenjing, wo ai ni, the track '
                       'tell you my heart in the specical day!!!')
            else:
                print ('I am so sad that you do not know the track shape. You are not wenjing. Give me some time to cry. Yesterday the sweats, '
                       'now the tears.')
        elif i == 6:
            if right:
                print ('HaHaHa, rigth answer, great! Wenjing have many pet phrases, all of them is very funny and interesting, I love all of them '
                       'even thought it is axiba, qie, pi. I love you!!!')
            else:
                print ('Not exactly right. If you are wenjing, you will know all of the pet phrases, this is a question. But perhaps you do not know '
                       'thems well because you said them without aware of them.')
        elif i == 7:
            if right:
                print ('Good, Right! It was such a sweety and wonderfull time when we went to different parks. We walked, talked, played kites, swing, '
                       'took photos, saw the rivers and sea, enjoyed the trees flowers and all the ties in the nature. There were smiling and laughing '
                       'all over the world in my heart. I love you, wenjing!!!')
            else:
                print ('Wrong! You are not wenjing, I cannot help doing this decision. These wonderfull times are so sweet that I think we can not forget '
                       'forever.')
        elif i == 8:
            if right:
                print ('HaHa, right, you know me, wenjing. I am a little bothered when I took photos time and time. Please forgive me, wenjing, your '
                       'are so beautiful, my heart is on you, I want to record all the beauties of you, and it is also the love of me.')
            else:
                print ('I must say the answer is not right. I took photos and staring at you to record and appreciate your ties, I fall into them, '
                       'I love you, wenjing.')
        elif i == 9:
            if right:
                print ('Wenjing, you are wenjing, yeah, exactly right! We have done all of them. I am the most happiest person. I want to hold your '
                       'hands and go through our lives till we are old. I love you.')
            else:
                print ('I am sorry, all of them have been done by wenjing and me. If you are wenjing, you will know the right answer. I love wenjing, '
                       'but are you wenjing?')
        input()
        return right

    ques_num = len(questions) # 10
    ques_inds = list(range(ques_num)) # range(10)
    #random.seed(10)
    random.shuffle(ques_inds)
    right_ans = []
    ques_inds_left = ques_inds
    minus_6_times = 0
    while(len(right_ans) < ques_num):
        for i in ques_inds_left:
            print ('question: ' + questions[i])
            ans = input('>')
            right = response_answer(ans, i)
            if right:
                right_ans.append(i)

        if len(right_ans) < ques_num:
            print ('##########################################################################################################')
            print ('You have correctly answered {} questions!'.format(len(right_ans)))
            if len(right_ans) < 6:
                minus_6_times += 1
                if minus_6_times >= 3:
                    break
                print ('If the right answers numbers is less than 6 by three consecutive times, this travel will stop here!')
            print ('You must answer all the questions right before you go forward! Come on!')
            input()
        else:
            print ('Excellent, all the question done! You are my best love wenjing, let\'s go')
            input()
            ready()
    
        ques_inds_left = [x for x in ques_inds_left if x not in right_ans]
        random.shuffle(ques_inds_left)


def ready():
    print ('''
         Are you ready?
         A: yes      B: no
    ''')
    while(1):
        ans = input('>')
        if ans in ['yes', 'Yes', 'Y', 'y', 'A', 'a', 'YES']:
            love_confirm()
            break
        else:
            print ('invalid answer, please input again')


def love_confirm():
    print ('''
         I am Douyaguang, do you love me?
         A: yes      B: no
    ''')
    i = 0
    while(1):
        ans = input('>')
        if ans in ['yes', 'Yes', 'Y', 'y', 'A', 'a', 'YES']:
            print ('Oh, wenjing love me, yeah, yeah, yeah!!!\n'
                   'I can not believe it, is it a dream?! Yeah, it is truth!!!\n'
                   'I love you wenjing, I love you wenjing, I love you wenjing!!!\n'
                   'The most import thing must be expressed three times!\n'
                   'Wenjing, now is the magic time\n')
            input()
            show_love()
            break
        else:
            if i == 0:
                print ('I love you so much, why not love me. please input again')
            if i == 1:
                print ('No, I will be very sad and the life will be meaningless if you do not love me? please inpput again')
            if i == 2:
                print ('I know you love me. Do not hesitate to fall in love with me! Go to input the yes, you will get a surprise!')
            if i == 3:
                print ('HumHumHum, I love you forever whatever you do. No matter whether you choose the yes answer, I will show his love for you!!!!')
            if i == 4:
                print ('Now I must tell you the truth, I can only accept the yes answer, hahahahahaha! please input again')
            if i >= 5:
                print ('Please input yes!' + '!' * (i - 5))
            i += 1


def show_love():
    lines = mylove.split('\n')
    for i, line in enumerate(lines):
        if 0<= i <= 24:
            time.sleep(0.1 * random.random())
            print ('\033[1;36;47m' + line)
        elif 25 <= i <= 35:
            time.sleep(0.1 * random.random())
            print ('\033[1;34;47m' + line)
        elif 36 <= i <= 47:
            time.sleep(0.2 * random.random())
            print ('\033[1;31;47m' + line)
        else:
            time.sleep(0.1 * random.random())
            print ('\033[1;36;47m' + line)


def main():
    print ('This is a love travel when you start it, many intresting outputs will be a surprise to you!\n'
           'Now, GO!!!\n')
    input()
    love_verify()


if __name__ == '__main__':
    main()
