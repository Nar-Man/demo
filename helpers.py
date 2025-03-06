
import streamlit as st
import random

word_list = ['smile', 'peace', 'bless', 'trust', 'shine']

def get_feedback(secret_word, guessed_word):
    feedback = []
    for i, char in enumerate(guessed_word):
        if char == secret_word[i]:
            feedback.append("✅")  
        elif char in secret_word:
            feedback.append("🟡")  
        else:
            feedback.append("⬜")  
    return ''.join(feedback)


def reset_game():
    st.session_state.secret_word = random.choice(word_list).upper()
    st.session_state.attempts_left = 6
    st.session_state.guesses = []
    st.session_state.input_key += 1  

