
import tkinter as tk

def detect_mood(text):
    # Define mood keywords
    moods = {
        'happy': ['happy', 'joy', 'excited', 'great', 'fantastic', 'good'],
        'sad': ['sad', 'down', 'depressed', 'bad', 'unhappy'],
        'angry': ['angry', 'mad', 'frustrated', 'annoyed'],
        'neutral': ['okay', 'fine', 'meh', 'normal']
    }

    # Initialize mood count
    mood_count = {mood: 0 for mood in moods}

    # Check for keywords in the input text
    for mood, keywords in moods.items():
        for word in keywords:
            if word in text.lower():
                mood_count[mood] += 1

    # Determine the mood with the highest count
    detected_mood = max(mood_count, key=mood_count.get)

    return detected_mood if mood_count[detected_mood] > 0 else 'neutral'

def change_color(mood):
    # Define mood-color associations
    mood_colors = {
        'happy': 'yellow',
        'sad': 'black',
        'angry': 'red',
        'exicted': 'gray'
    }

    # Get the corresponding color for the mood
    color = mood_colors.get(mood, 'gray')
    root.configure(bg=color)

def check_mood():
    mood_input = mood_entry.get()
    mood = detect_mood(mood_input)
    change_color(mood)
    mood_entry.delete(0, tk.END)  # Clear the entry box

# Set up the main window
root = tk.Tk()
root.title("Mood Color Changer")
root.geometry("400x200")

# Mood input field
mood_entry = tk.Entry(root, width=30)
mood_entry.pack(pady=20)

# Submit button
submit_button = tk.Button(root, text="Change Color", command=check_mood)
submit_button.pack(pady=10)

# Run the application
root.mainloop()
