# 🎱 Korean Lottery (Lotto) Auto-Purchase Bot

This bot automates the process of purchasing lottery tickets from the Korean lottery website (동행복권). It uses Selenium WebDriver to automate browser interactions.

## 💡 Project Motivation
I created this project to eliminate the need for physical visits to lottery retailers. Instead of making trips to purchase lottery tickets, this bot allows me to buy tickets. This project can be further extended to asking other willing users to be on the platform where one person will be managing multiple accounts. A further extension would be add frontend UI allowing users to get insights about their lottery status i.e. spending, profit, number of tickets bought etc.

- Purchase lottery tickets online automatically
- Save time and effort by automating the entire purchase process
- Avoid the hassle of visiting physical lottery retailers
- Maintain consistent participation with minimal effort

## 🚀 Features

- Automated login to the lottery website
- Automatic number generation and ticket purchase
- Headless browser operation (runs in background)
- Configurable number of tickets to purchase

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7 or higher
- Google Chrome browser

## 🛠️ Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/lotto.git
cd lotto
```

2. Install required packages:
```bash
pip install selenium python-dotenv chromedriver-autoinstaller
```

## ⚙️ Configuration

1. Create a `.env` file in the project root directory:
```bash
touch .env
```

2. Add your lottery website credentials to the `.env` file:
```
USER_ID=your_username
USER_PW=your_password
```

## 🎮 Usage

1. Adjust the number of tickets to purchase by modifying the `COUNT` variable in `buy_lotto.py`

2. Run the bot:
```bash
python buy_lotto.py
```

## ⏰ Scheduling Automatic Runs (Mac/Unix Systems)

For Mac and other Unix-based systems, you can use crontab to schedule the bot:

1. Open your crontab file:
```bash
crontab -e
```

2. Add a line to run the script weekly (e.g., every Monday at 9 AM):
```bash
0 9 * * 1 cd /path/to/lotto && /usr/bin/python buy_lotto.py
```

Note: This scheduling method uses the Unix crontab system and works on macOS and other Unix-based operating systems.

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your login credentials secure
- Use this bot responsibly and in accordance with the lottery website's terms of service

## ⚠️ Disclaimer

This bot is for educational purposes only. Use at your own risk. The authors are not responsible for any misuse or consequences of using this bot.
