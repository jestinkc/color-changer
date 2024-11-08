# Simple mood changer in Python

# Define a function to display mood
def display_mood(mood):
    moods = {
        "happy": "😊 You're feeling happy!",
        "sad": "😢 It's okay to feel sad sometimes.",
        "angry": "😠 Take a deep breath; you're feeling angry.",
        "relaxed": "😌 You're feeling relaxed. Enjoy it!",
        "excited": "😃 You're excited! That's great!",
        "bored": "😐 Feeling bored? Maybe try something new!",
    }
   
    # Get mood message or default message
    message = moods.get(mood.lower(), "🤔 I don't recognize that mood.")
    return message

# Ask for user input
user_mood = input("How are you feeling today? (happy, sad, angry, relaxed, excited, bored): ")

# Display the corresponding mood message
print(display_mood(user_mood))

