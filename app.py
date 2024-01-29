from flask import Flask, request, render_template

    app = Flask(__name__)

    # Set the OpenAI API Key initially as None
    api_key = None


    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/submit-query', methods=['POST'])
    def submit_query():
        global api_key
        # Retrieve the API key and user input from the form data
        api_key = request.form['api-key']
        user_input = request.form['user-input']
        # Call the handle_user_input function with the user input
        assistant_response = handle_user_input(user_input)
        # Return the assistant's response
        return {"botMessage": assistant_response}


    def handle_user_input(user_input):
        # Use the global api_key variable to set the OpenAI client
        client = OpenAI(api_key="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")
        # Create a chat completion request
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Python software engineer."},
                {"role": "user", "content": user_input}
            ]
        )
        # Retrieve the assistant's response
        response = chat_completion.choices[0].message.content
        return response


    if __name__ == '__main__':
        app.run(port=5001)












