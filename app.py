import streamlit as st
import time

def calculate_wpm(text, time_taken):
    words = text.split()
    num_words = len(words)
    minutes = time_taken / 60
    wpm = num_words / minutes if minutes > 0 else 0
    return round(wpm)

def main():
    st.title("Typing Test Game")

    st.write("Welcome to the Typing Test Game! Type the following text as fast as you can within 30 seconds:")

    text_to_type = "GeeksforGeeks is a popular online platform that provides a wide variety of resources for computer science students, professionals, and enthusiasts. It is primarily focused on computer science topics such as algorithms, data structures, programming languages, software engineering, system design, and more."
    st.write(text_to_type)

    # Increase height for larger content
    user_input = st.text_area("Type here:", height=200)

    start_time = time.time()
    timer_placeholder = st.empty()  # Placeholder for timer
    timer = 30
    while timer > 0:
        timer = 30 - int(time.time() - start_time)
        timer_placeholder.write("Time remaining: {} seconds".format(timer))
        time.sleep(1)

    time_taken = time.time() - start_time
    wpm = calculate_wpm(user_input, time_taken)

    st.write("Time's up!")
    st.write("Your typing speed is: {} WPM".format(wpm))


if __name__ == "__main__":
    main()
