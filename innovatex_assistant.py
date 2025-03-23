class DynamicResponseSystem:
    def __init__(self):
        # Predefined response templates
        self.response_templates = {
            "find_investors": """
            To find investors, follow these steps:
            1. Go to the **'InnovateX Opportunities'** section.
            2. Click on the **'Search for Investors'** card.
            3. Browse or filter investors based on your industry.
            4. Send a detailed pitch to connect with potential investors.
            """,
            "reset_password": """
            To reset your password:
            1. Go to the login page.
            2. Click on **'Forgot Password'**.
            3. Enter your email address.
            4. Follow the instructions sent to your email.
            """,
            "default": "I'm not sure what you're asking. Can you clarify?"
        }

    def analyze_input(self, user_input):
        """
        Analyze the user's input to determine the intent.
        """
        if "investors" in user_input.lower():
            return "find_investors"
        elif "reset password" in user_input.lower():
            return "reset_password"
        else:
            return "default"

    def generate_response(self, user_input):
        """
        Generate a response based on the analyzed intent.
        """
        intent = self.analyze_input(user_input)
        return self.response_templates.get(intent, self.response_templates["default"])

# Main function to simulate the system
def main():
    print("Welcome to the InnovateX Dynamic Response System!")
    print("Type your question, or type 'exit' to quit.")

    system = DynamicResponseSystem()

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Generate and display the response
        response = system.generate_response(user_input)
        print(f"\nSystem: {response}")

# Run the program
if __name__ == "__main__":
    main()