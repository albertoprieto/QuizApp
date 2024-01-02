# Quiz App Readme

This is a simple quiz application built using KivyMD, a framework for developing cross-platform mobile applications in Python. The app allows users to navigate through different screens, answer quiz questions, and view their results.

## Getting Started

1. **Dependencies**: Make sure you have KivyMD installed. You can install it using:

    ```bash
    pip install kivymd
    ```

2. **Run the App**: Execute the script `main.py` to launch the quiz app.

    ```bash
    python main.py
    ```

## App Structure

The app is organized into different screens, each serving a specific purpose:

- **SplashScreen**: The initial screen that appears when the app is launched.

- **FirstScreen**: Allows users to choose a quiz topic and navigate to the quiz screen.

- **AboutScreen**: Placeholder for any information about the app or quiz.

- **Primer**: The main quiz screen where users answer questions. It includes a timer, feedback dialogs, and a progress indicator.

- **Results**: Displays the user's quiz results, including the number of correct answers and the total number of questions.

## Features

1. **Timer**: Each question has a timer, and if the user doesn't answer within the time limit, the app proceeds to the next question.

2. **Feedback Dialogs**: After answering a question, a feedback dialog appears indicating whether the answer was correct or incorrect.

3. **Results Screen**: Provides a summary of the user's performance, displaying the number of correct answers and the total number of questions.

4. **Dynamic Screen Management**: The app uses Kivy's ScreenManager to navigate between different screens.

## How to Use

1. Launch the app, and the Splash Screen will be displayed for 5 seconds.

2. Navigate to the First Screen and select a quiz topic.

3. Answer the quiz questions on the Primer screen within the time limit.

4. After completing the quiz, view the results on the Results screen.

## Customization

- **Quiz Questions**: Add or modify quiz questions by updating the `preguntas.json` file.

- **Themes**: Customize the app's appearance by adjusting the theme parameters in the `build` method of the `App` class.

## Contributing

Feel free to contribute to the development of this app by submitting issues or pull requests.

## License

This quiz app is released under the [MIT License](LICENSE).
