#AQI_Math

# Function to determine AQI color and health message
def get_aqi_info(score):
    if score <= 50:
        return "Green", "🟢", "Air quality is good. Enjoy your day outside!"
    elif score <= 100:
        return "Yellow", "🟡", "Air quality is acceptable, but sensitive groups should take care."
    elif score <= 150:
        return "Orange", "🟠", "Unhealthy for sensitive groups — limit outdoor exertion."
    elif score <= 200:
        return "Red", "🔴", "Unhealthy — everyone should reduce outdoor activity."
    elif score <= 300:
        return "Purple", "🟣", "Very unhealthy — health warnings of emergency conditions."
    else:
        return "Maroon", "🟤", "Hazardous — stay indoors and avoid outdoor exposure."

print("=== AQI COLOR DISPLAY ===")
print("Type 'exit' to quit.\n")

# Loop for continuous input
while True:
    place = input("Enter a place: ").strip()
    if place.lower() == "exit":
        print("Goodbye! Stay safe 🌎")
        break
    
    try:
        score = int(input("Enter the AQI score: "))
    except ValueError:
        print("⚠️ Please enter a valid number for AQI.\n")
        continue

    color, emoji, message = get_aqi_info(score)
    print(f"\n{emoji} {place} is {color}: AQI score is {score}")
    print(f"💬 {message}\n")