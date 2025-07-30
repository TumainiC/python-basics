"""
Create a program that asks for the user’s name and favorite color, then prints a personalized greeting like: “Hello, [Name]! Your favorite color, [Color], is awesome!”
"""

# name = input("What is your name? ")
# colour = input("What is your favourite color?")
# print(f"Hello, {name}! Your favourite color, {colour} is awesome!")

"""
Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again. 
"""
def ask_question(question_data):
    print(f"/nQuestion: {question_data['question']}")
    for choice in question_data['choices']:
      print(choice)

    while True:
      answer = input("Your answer (A, B, C, or D): ").strip().upper()
      if answer in ["A", "B", "C", "D"]:
        return answer == question_data['answer']
      else:
        print("Please enter a valid choice between (A, B, C or D)")
def play_quiz(names, quiz):
  scores = []
  for name in names:
    print(f"/nNow playing: {name}")
    correct_ans = 0
    for q in quiz:
      if ask_question(q):
        correct_ans += 1
        scores.append(
          {
            "name": name,
            "score": correct_ans
          }
        )
        print(f"{name}, you got {correct_ans} answers correct!")
    return scores

        
def main():
  print("Welcome to the Python Quiz Game!")
  print("You will be asked a series of questions. Answer with A, B, C, or D.")
  print("Let's see how well you know Python!")
  quiz = [
  {
  "question":"What is the output of print(type([])) in Python?",
  "choices": ["A) <class 'list'>","B) <type 'list'>", "C) list","D) []"],
  "answer": "A"
  },
  {
  "question":" Which of the following is not a valid Python data type?",
  "choices": ["A) tuple","B) dictionary", "C) array", "D) set"],
  "answer": "C"
  },
  {
  "question":"What does the len() function do?",
  "choices": ["A) Counts characters in a string only","B) Returns the memory size of an object", "C) Returns the number of items in an object","D) Deletes an object"],
  "answer": "C"
  },
  {
  "question":"What will this code output? print('3' + '4')",
  "choices": ["A) 7","B) 34", "C) TypeError","D) 12"],
  "answer": "B"
  }
  ]

  while True:
    start = input("/nHey there! Wanna play a fun quiz game? yes/no").strip().lower()
    if start != "yes":
      print("Maybe next time. Bye!")
      break
    else:
      try:
            players = int(input("How many players? "))
            if players < 1:
                print("At least one player required.")
                continue
        except ValueError:
            print("Enter a valid number.")
            continue

        names = [input(f"Player {i+1}, your name: ") for i in range(players)]
        print("\nAwesome, let's begin!")
        scores = play_quiz(names, quiz)

        print("\n🏆 Final Scores 🏆")
        for entry in scores:
            print(f"{entry['name']}: {entry['score']}/{len(quiz)}")

        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing! 🎉")
            break

if __name__ == "__main__":
    main()
