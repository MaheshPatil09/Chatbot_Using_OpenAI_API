# find more coding projects & free ebooks at Codewithcurious.com
import tkinter as tk
import openai
import os

# Option 1: Direct API Key Assignment (less secure)
# openai.api_key = "sk-your_actual_api_key_here"

# Option 2: Environment Variable (more secure)
openai.api_key = "sk-proj-xTnAlNFq1kJ2WH1BERujT3BlbkFJPnjUkutCury29m2GC2d6"


def generate_response(prompt):
    try:
        completions = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text.strip()
        return message
    except Exception as e:
        return f"Error: {str(e)}"

def display_response():
    input_text = input_field.get()
    response = generate_response(input_text)
    output_field.config(state='normal')
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, response)
    output_field.config(state='disabled')

# The rest of your GUI setup code remains the same...


# Create the main window
root = tk.Tk()
root.title("OpenAI Chatbot")
root.geometry("600x700")

# Create the input field
input_field = tk.Entry(root, font=("Arial", 14))
input_field.pack(pady=10)

# Create the submit button
submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=display_response)
submit_button.pack(pady=10)

# Create the output field
output_field = tk.Text(root, font=("Arial", 14), state='disabled')
output_field.pack(pady=10)

# Start the GUI event loop
root.mainloop()