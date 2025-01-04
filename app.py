# import streamlit as st
# from src.quiz_system.crew import QuizSystemCrew
# from dotenv import load_dotenv
# import openai
# import os

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")


# def main():
#     st.title("Quiz System Crew")
#     st.write("Choose an action to perform with the Quiz System Crew.")

#     # Dropdown menu to select action
#     action = st.selectbox(
#         "Select an action:",
#         ["Run", "Train", "Replay", "Test"]
#     )

#     # Input fields for common inputs
#     topic = st.text_input("Enter the topic:", "Science and Technology")

#     if action == "Train" or action == "Test":
#         n_iterations = 1
#         model_or_file = "gpt-4"
#     elif action == "Replay":
#         task_id = st.text_input("Enter the task ID:")

#     # Execute action
#     if st.button(f"Execute {action}"):
#         try:
#             result = None
#             if action == "Run":
#                 inputs = {"topic": topic}
#                 result = QuizSystemCrew().crew().kickoff(inputs=inputs)
#             elif action == "Train":
#                 inputs = {"topic": topic}
#                 result = QuizSystemCrew().crew().train(n_iterations=int(n_iterations),
#                                                        filename=model_or_file, inputs=inputs)
#             elif action == "Replay":
#                 result = QuizSystemCrew().crew().replay(task_id=task_id)
#             elif action == "Test":
#                 inputs = {"topic": topic}
#                 result = QuizSystemCrew().crew().test(n_iterations=int(n_iterations),
#                                                       openai_model_name=model_or_file, inputs=inputs)

#             # Debugging result of type 'CrewOutput'
#             st.write(f"Debug: Result type is {type(result)}")

#             # Inspect attributes of 'CrewOutput'
#             if hasattr(result, '__dict__'):
#                 st.write(f"Debug: CrewOutput's attributes: {dir(result)}")
#                 st.write(
#                     f"Debug: CrewOutput's attribute values: {vars(result)}")

#                 # Look for a raw or relevant result field
#                 if hasattr(result, 'raw'):
#                     st.write(f"Debug: Raw result content: {result.raw}")
#                     st.success(f"Final result:\n{result.raw}")
#                 else:
#                     st.error("Could not find 'raw' in the result object.")
#             else:
#                 st.error("Result does not have attributes.")

#         except Exception as e:
#             st.error(f"An error occurred: {e}")


# if __name__ == "__main__":
#     main()


import streamlit as st
from src.quiz_system.crew import QuizSystemCrew
from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    st.title("Quiz System Crew")
    st.write("Choose an action to perform with the Quiz System Crew.")

    # Dropdown menu to select action
    action = st.selectbox(
        "Select an action:",
        ["Run", "Train", "Replay", "Test"]
    )

    # Input fields for common inputs
    topic = st.text_input("Enter the topic:", "Science and Technology")

    if action == "Train" or action == "Test":
        n_iterations = 1
        model_or_file = "gpt-4"
    elif action == "Replay":
        task_id = st.text_input("Enter the task ID:")

    # Execute action
    if st.button(f"Execute {action}"):
        try:
            result = None
            if action == "Run":
                inputs = {"topic": topic}
                result = QuizSystemCrew().crew().kickoff(inputs=inputs)
            elif action == "Train":
                inputs = {"topic": topic}
                result = QuizSystemCrew().crew().train(n_iterations=int(n_iterations),
                                                       filename=model_or_file, inputs=inputs)
            elif action == "Replay":
                result = QuizSystemCrew().crew().replay(task_id=task_id)
            elif action == "Test":
                inputs = {"topic": topic}
                result = QuizSystemCrew().crew().test(n_iterations=int(n_iterations),
                                                      openai_model_name=model_or_file, inputs=inputs)

            # # Debugging result of type 'CrewOutput'
            # st.write(f"Debug: Result type is {type(result)}")

            # Check for 'raw' field and display
            if hasattr(result, 'raw'):
                st.write(
                    f"The expected questions and their answer for this time are:\n{result.raw}")
                # st.success(f"Final result:\n{result.raw}")
            else:
                st.error("Could not find 'raw' in the result object.")

            # # Inspect 'tasks_output' if available
            # if hasattr(result, 'tasks_output'):
            #     st.write(f"Debug: tasks_output:\n{result.tasks_output}")

        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
