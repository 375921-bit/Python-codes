import tkinter as tk
import tkinter.scrolledtext as tksc
import module_multifactorgui as mfg

# Create the main application window
root = tk.Tk()
root.title("Multi-Factor Authentication")

# Create a frame for authentication UI
frame_auth = tk.Frame(root)
frame_auth.pack(padx=10, pady=10)

# Create a multi-factor authenticator instance
my_authenticator = mfg.MultiFactorAuth()

# Set initial authentication credentials
my_authenticator.set_authentication("Warsaw0110!", "Warlan123!+")

# Retrieve and print authentication info
authentication_info = my_authenticator.get_authentication_info()
print(authentication_info)

# Set multi-factor question and answer
question = "What is your favorite color?"
answer = "turquoise"
my_authenticator.set_multiFactorAuthentication(question, answer)

# Create a scrolled text widget in the frame
test_textbox = tksc.ScrolledText(frame_auth, width=40, height=10)
test_textbox.pack()

# Start the Tkinter event loop
my_authenticator.mainloop()