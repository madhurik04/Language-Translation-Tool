# Language Translation Tool

This is a simple GUI-based language translation tool built using Python's Tkinter library for the user interface and Googletrans for translation services. The application allows users to input text, select a source language, and a target language, and then get the translated text displayed.

<p align = "center">
    <img src = "https://github.com/madhurik04/Language-Translation-Tool/assets/131545409/15b6786e-d122-4f8e-8ce2-bc624a5d3a74">
</p>

## Features

- User-friendly graphical interface
- Supports translation between multiple languages
- Uses Google Translate for reliable translations

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Googletrans library

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/Language-Translation-Tool.git
    cd Language-Translation-Tool
    ```

2. **Install the required Python packages:**

    ```sh
    pip install googletrans==4.0.0-rc1
    ```

## Usage

1. **Run the application:**

    ```sh
    python google_test.py
    ```

2. **Using the Tool:**

- Enter the text you want to translate in the "Source Text" box.
- Select the source language from the drop-down menu.
- Select the target language from the drop-down menu.
- Click on the "Translate" button to get the translated text in the "Destination Text" box.

## Code Overview

The main sections of the code include:

- **Imports:** Importing necessary libraries and modules.
- **Translation Function:** `change(text, src, dest)` which uses Googletrans to perform the translation.
- **Data Handling Function:** `data()` which gets the input text and language selections, performs the translation, and updates the destination text box.
- **GUI Design:** Setting up the Tkinter window, labels, text boxes, comboboxes, and buttons for the user interface.

## Example

Here's a brief example of how to use the tool:

1. Enter "Hello, how are you?" in the "Source Text" box.
2. Select "English" as the source language.
3. Select "Hindi" as the target language.
4. Click "Translate".
5. The translated text "नमस्ते, आप कैसे हैं?" will appear in the "Destination Text" box.

## Contributing

Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Googletrans](https://py-googletrans.readthedocs.io/en/latest/) - A free and unlimited Python library that implemented Google Translate API.
