def explain_topic():
    topic = input("\nEnter the topic you want to understand: ")
    print("\nStudy Prompt:")
    print(f"Explain {topic} in simple language with examples and key points.")


def exam_answer():
    topic = input("\nEnter the exam topic: ")
    marks = input("How many marks? ")

    print("\nStudy Prompt:")
    print(
        f"Explain {topic} as an exam-ready {marks}-mark answer. "
        "Include definition, important points, examples, and a short conclusion."
    )


def interview_practice():
    topic = input("\nEnter the interview topic: ")

    print("\nStudy Prompt:")
    print(
        f"Create 5 interview questions about {topic}. "
        "Give answers and briefly explain each answer."
    )


def revision_notes():
    topic = input("\nEnter the topic: ")

    print("\nStudy Prompt:")
    print(
        f"Create quick revision notes for {topic}. "
        "Include important definitions, formulas, concepts, and key points."
    )


def main():
    while True:
        print("\n==============================")
        print("      AI STUDY ASSISTANT")
        print("==============================")
        print("1. Explain a Topic")
        print("2. Exam Answer")
        print("3. Interview Practice")
        print("4. Revision Notes")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            explain_topic()

        elif choice == "2":
            exam_answer()

        elif choice == "3":
            interview_practice()

        elif choice == "4":
            revision_notes()

        elif choice == "5":
            print("\nGood luck with your studies! 🚀")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()