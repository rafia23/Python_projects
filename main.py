import time
import random

questions = {
     "easy": [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A",
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B",
    },
    {
        "prompt": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"],
        "answer": "C",
    },
    {
        "prompt": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D",
    },
     ],

     "medium": [
    {
        "prompt": "What is the chemical symbol for Gold?",
        "options": ["A. Au", "B. Ag", "C. Pb", "D. Fe"],
        "answer": "A",
    },
    {
        "prompt": "Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
        "answer": "C",
    },
    {
        "prompt": "Which gas do plants primarily use for photosynthesis?",
        "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
        "answer": "B",
    },
    {
        "prompt": "What is the powerhouse of the cell?",
        "options": ["A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Endoplasmic Reticulum"],
        "answer": "B",
    },
     ],

     "hard": 
     [
    {
        "prompt": "Which country is famous for inventing sushi?",
        "options": ["A. China", "B. Japan", "C. South Korea", "D. Thailand"],
        "answer": "B",
    },
    {
        "prompt": "What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C",
    },
    {
        "prompt": "What is the Heisenberg Uncertainty Principle related to?",
        "options": [
            "A. Thermodynamics",
            "B. Quantum Mechanics",
            "C. Classical Mechanics",
            "D. Relativity" ],
        "answer": "B",
    },
    {
        "prompt": "Which programming language is primarily used for developing AI and Machine Learning models?",
        "options": [
            "A. C++",
            "B. Java",
            "C. Python",
            "D. Ruby" ],
        "answer": "C",
    }, 
     ]
}


def run_quiz(questions, difficulty): #takes the questions list as input
    score = 0
    question_set = questions[difficulty] # Get questions for the chosen level    
    original_question_count = len(question_set)  # Store the total number of questions
    random.shuffle(question_set)  # Randomize question order

    print(f"\n🔥 Starting the quiz! Difficulty: {difficulty.capitalize()} 🔥\n")
    
    for question in question_set:
        print(question["prompt"])
        for option in question["options"]:
            print(option)

        start_time = time.time() #start timer   
        answer = input("Enter your answer(A, B, C or D) within 10 seconds:").upper()
        end_time = time.time() 
        
        time_taken = end_time - start_time #calculate time taken

        if time_taken > 10: 
            print("Time's up! You took too long!\n")
            continue #move to the next question

        if answer == question["answer"]:
            print("\nYou got it correct!!\n")
            score+=1

        else:
            print("\nWrong answer. The correct answer is", question["answer"],"\n")

        time.sleep(1)

    print(f"You got {score} out of {original_question_count} questions correct.")

    save_score(difficulty,score,original_question_count) #save score to file


def save_score(difficulty, score, total):
    """Saves the quiz score to a file."""
    with open("quiz_scores.txt", "a") as file:
        file.write(f"Difficulty: {difficulty.capitalize()} | Score: {score}/{total}\n")
    print("Your score has been saved!\n")

    

difficulty_level = input("Choose a difficulty level(easy, medium, hard):").lower()
run_quiz(questions, difficulty_level)
