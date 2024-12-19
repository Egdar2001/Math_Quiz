import random
from django.shortcuts import render, redirect

# Create your views here.

def generate_question():
    operators = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

def index(request):
    if 'score' not in request.session:
        request.session['score'] = 0
        request.session['question'], request.session['answer'] = generate_question()

    return render(request, 'quiz/index.html', {
        'question': request.session['question'],
        'score': request.session['score'],
    })

def answer(request):
    if request.method == 'POST':
        user_answer = int(request.POST.get('answer', 0))
        correct_answer = request.session.get('answer', 0)

        if user_answer == correct_answer:
            request.session['score'] += 1
            message = "Correct!"
        else:
            message = f"Wrong! The correct answer was {correct_answer}."

        request.session['question'], request.session['answer'] = generate_question()

        return render(request, 'quiz/index.html', {
            'question': request.session['question'],
            'score': request.session['score'],
            'message': message,
        })

    return redirect('index')