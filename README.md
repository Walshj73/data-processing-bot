# Advancements in Imaging Sensors and AI for Plant Stress Detection: A Systematic Literature Review

The Data Processing Bot is a Python script designed to automate data processing tasks using the PyAutoGUI and Pyperclip libraries. It interacts with various applications to extract, process, and manage data in specific workflows.

For this bot to succeed the user needs to customise the script to their own system. This script and all experiments were performed on a Ubuntu machine. However, the script should run on any OS as long as the user has installed the required python libraries.

## Features

- Automate data processing tasks.
- Extract data from one application and paste it into another.
- Dynamically handle row and column interactions based on specific coordinates.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/<username>/data-processing-bot.git
   ```
   
2. Install the required dependencies using pip:

   ```python
   python install.py
   ```

## Running the Bots

It is very easy to run the bot. As the bot is simply a python script you only need to execute the following command in your terminal:

   ```python
   python bot.py
   ```

## Usage

1. Before running the bot, make sure all required applications (e.g., LibreOffice, Excel, Chrome) are open, and the correct sheets are active.

2. Ensure that you have customised the script so that the screen locations (pixel coordinates) have been updated to reflect your monitors resolution. If using another journal database other than OneSearch the script will need to be redesigned to work with this database. However, the fundamental concept will remain the same along with the bots checkpointing abilities.
   
3. Launch the bot by executing the provided script according to your operating system.

4. The bot will process the data according to the predefined automation logic, interacting with different applications as needed.

5. The bot may require manual interaction or specific setups in certain steps, depending on the use case.

## Configuration

The bot script contains various parameters that can be adjusted to fit specific use cases. These parameters include:

+ bot.PAUSE: Set the delay between GUI actions (in seconds). This can be useful for handling delays when webpages are slow to load or to handle slow download speeds.
+ bot.FAILSAFE: Set whether the fail-safe feature is enabled (True/False).

## Contributions

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Disclaimer

The use of this bot script is subject to the end-user's responsibility. Be cautious while running automated scripts and ensure that you have proper authorization and permissions for the target applications and data.
