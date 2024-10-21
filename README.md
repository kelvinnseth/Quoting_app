# Quoting Application

## Overview
The Quoting Application is a simple GUI-based tool for generating quotes based on area dimensions and optional discount percentages. The application calculates the total cost based on user-defined dimensions and provides a final quote after applying any specified discount.

## Features
- Input for area dimensions (length and width)
- Option to specify a discount percentage
- Displays a detailed quote with total cost, discount applied, and final price

## Technologies Used
- Python 3.x
- Tkinter (for GUI)
- pytest (for testing)

## Installation
To run the application, ensure you have Python 3.x installed. Then, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kelvinnseth/Quoting_app.git
   cd Quoting_app
   ```

2. **Install the required packages (if necessary):**
   If you haven't already, you can install `pytest` via pip:
   ```bash
   pip install pytest
   ```

## Usage
To run the Quoting Application, execute the following command in your terminal:
```bash
python app.py
```
This will open the GUI window where you can input the area dimensions and discount percentage.
1. Enter the length and width in meters.
2. Enter a discount percentage (optional).
3. Click the "Generate Quote" button to see the quote details.

## Running Tests
To ensure the application functions as expected, you can run the provided tests using pytest. Execute the following command in the terminal:
```bash
pytest tests/test_quote_app.py
```
This will run all unit tests and display the results in the terminal.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Project Structure
- `app.py`: Main application code
- `tests/test_quote_app.py`: Unit tests for the application
- `README.md`: Documentation
- `LICENSE`: (Optional) Include if you decide to add licensing information

## Summary of What You Need
1. **Project Structure:**
   - Ensure you have the main `app.py` file with your application code.
   - Create a `tests` directory with `test_quote_app.py` for unit tests.
   - Include this README.md file in your project root.
   - Optionally, add a LICENSE file if you decide to include licensing.

2. **Testing:**
   - Make sure to have the proper testing files in the `tests` directory as mentioned earlier.

If you need any further assistance or have questions about setting up your project, feel free to ask!
