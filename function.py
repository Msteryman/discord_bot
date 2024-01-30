def math_decide_function(task: str):
    """Решает примеры по кусостанцкой математике"""
    from data import math_data
    task = task.replace('9y10','a')
    task = task.replace('10y9','b')
    task = task.replace('11y9','c')
    task = task.replace('12y0','d')
    task = task.replace('9y12','e')
    task = task.replace('95y08','f')
    task = task.replace('18 ЭА ЕЙ','g')
    task_split = task.split('y')

    answer_list = []
    answer = ''
    word_key = ''
    for i in task_split:
      for word_key  in i.split(' '):
        if '^' in word_key:
          answer_list.append(math_data[word_key[-2:]] + ' '+ math_data[word_key[:-2]])
          print('s')
        else:
          answer_list.append(math_data[word_key])

    for i in answer_list:
      answer += i + ' '

    answer = answer[:-1]
    capital_letter = answer[0].title()
    answer = answer[1:]
    answer = answer[::-1]
    answer += capital_letter
    answer = answer[::-1]
    return(answer)