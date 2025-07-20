
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)

            status_label.config(text="Listening...")
            audio = r.listen(source, phrase_time_limit=10)
            app.update()

            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()

            result_var.set(f"You said: {text}")
            status_label.config(text="Recognition successful")

    except sr.UnknownValueError:
        result_var.set("Could not understand. Try again.")
        status_label.config(text="Recognition failed")
    except Exception as e:
        result_var.set(f"Error: {e}")
        status_label.config(text="Something went wrong")

# -------------------- UI --------------------
app = tk.Tk()
app.title("Speech Recognition Tool")
app.geometry("400x300")
app.configure(bg="white")

tk.Label(app, text="Speech Recognition Tool", font=("Arial", 16), bg="white").pack(pady=10)

tk.Button(app, text="Start Listening", font=("Arial", 12), command=recognize_speech).pack(pady=10)

result_var = tk.StringVar()
tk.Label(app, textvariable=result_var, font=("Arial", 12), bg="white", wraplength=350).pack(pady=10)

status_label = tk.Label(app, text="", font=("Arial", 10), fg="green", bg="white")
status_label.pack(pady=5)

tk.Label(app, text="Try saying: hello, open, stop, exit", font=("Arial", 10), bg="white").pack(pady=5)

app.mainloop()
