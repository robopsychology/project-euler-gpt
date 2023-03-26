from ai.flan_t5 import Flan_T5

question = '''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

if __name__ == '__main__':
    flan_t5 = Flan_T5()
    answer = flan_t5.answer(question)
    print(answer)
