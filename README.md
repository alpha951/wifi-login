# Auto Wifi Login script for LNMIIT portal

## Requirements

    1. Selenium
    2. Chrome Webdriver
    3. pyinstaller (fot creating executable file)

## Usage

1. Clone the repository
2. update your login credentials in `wifi.py`
3. Run the script using `python wifi.py`

## Creating executable and set as Satrtup program

1. Run `pyinstaller wifi.py`
2. create shortcut of the executable file in `dist` folder
3. Using `Win+R` open `shell:startup` and paste the shortcut file there.
4. Test by restarting your system.
5. The script will run automatically after startup and login to the wifi portal.
6. Cheers! :beers:
