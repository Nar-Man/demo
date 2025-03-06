import streamlit as st
import random
from PIL import Image
from helpers import reset_game, get_feedback

image_path = "wordle.png"
image = Image.open(image_path)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(image, width=400)

col1, col2, col3 = st.columns([1, 5, 1])
with col2:
    st.subheader("Get 6 chances to guess a 5-letter word.")

word_list = ['smile', 'peace', 'bless', 'trust', 'shine'] 

if "secret_word" not in st.session_state:
    st.session_state.secret_word = random.choice(word_list).upper()
    st.session_state.attempts_left = 6
    st.session_state.guesses = []
    st.session_state.input_key = 0  
    

guessed_word = st.text_input("Enter a 5-letter word:", key=f"input_{st.session_state.input_key}").upper()

if guessed_word:
    if len(guessed_word) == 5 and guessed_word.isalpha():
        if guessed_word in st.session_state.guesses:  
            st.warning("You've already guessed this word!")
        else:
            feedback = get_feedback(st.session_state.secret_word, guessed_word)
            st.session_state.guesses.append(guessed_word)  
            st.session_state.attempts_left -= 1
            st.write(f"Feedback: {feedback}")

            if guessed_word == st.session_state.secret_word:
                st.success("🎉 Congratulations! You've guessed the correct word!")
                st.session_state.attempts_left = 0
    else:
        st.warning("Please enter a valid 5-letter word.")

col1, col2, col3 = st.columns([1, 1, 1])
with col2: 
    st.write("### Your Attempts:")
    for guess in st.session_state.guesses:
        st.write(guess, "→", get_feedback(st.session_state.secret_word, guess))

if st.session_state.attempts_left == 0 and guessed_word != st.session_state.secret_word:
    st.error(f"❌ Game Over! The correct word was: {st.session_state.secret_word}")

if st.session_state.attempts_left == 0 or guessed_word == st.session_state.secret_word:
    if st.button("🔄 Play Again"):
        reset_game()
        st.rerun()  
