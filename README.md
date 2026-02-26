# 🏛️ The Architect's Log

> A time logging and analytics tool designed around an architect's workflow.

---

## What Is It?

Have you ever wondered how long your project's Design Development phase actually took? How many hours are you spending on Construction Documents per project?

**The Architect's Log** lets you log your work by project and phase, building out your own personal analytics over time — so you can finally understand how your time really breaks down.

Whether you're billing a client, estimating a future project, or just satisfying your own curiosity, the Architect's Log gives you the data-backed clarity you'll need to properly handle your workflow.

---

## Features

- **On-screen timer** - Log time live as you work, or add entries after the fact on your own schedule
- **Project & phase organization** - Categorize every log by project and phase
- **Beautiful analytics** - Visualize how your time is distributed across projects and phases
- **Invoice generation** - Group logs into invoices and export them as PDFs
- **Easy-to-use interface** - Minimal learning curve, maximum insight

---

## Download

Pre-built standalone desktop applications are available for all major platforms:

| Platform | Download |
|----------|----------|
| macOS | [Download for Mac](https://github.com/CanMatthewCode/ArchitectsLog/releases/download/v1.0.1/ArchitectsLog-mac.zip) |
| Windows | [Download for PC](https://github.com/CanMatthewCode/ArchitectsLog/releases/download/v1.0.1/ArchitectsLog.exe) |
| Linux | [Download for Linux](https://github.com/CanMatthewCode/ArchitectsLog/releases/download/v1.0.1/ArchitectsLog-Linux) |

When you first run the program you may encounter an OS warning due to system securities and the lack of a developer certificate. 

To move past this:

- **Mac** -	   	After unzipping the file and double-clicking the app you will get a system warning. Click 'Done'.  
			   	Then go to 'System Settings' -> 'Privacy & Security' -> scroll down to 'Security' where it says:
			   	"ArchitectsLog.app" was blocked to protect your Mac.  Click 'Open Anyway' and enter your password.
			   	The program will now run normally.

- **Windows** - After double-clicking the app you will get a 'Windows protected your PC' popup against 
				potentially unsafe software. Click 'More Info' followed by 'Run Anyway' to open the application.
				The program will now run normally.

- **Linux** -	Right-click the program and select 'Properties' -> 'Permissions' and check 'Run as Program'.
				If that is not an option, open a terminal, cd to where the program exists and run:
```
chmod +x ArchitectsLog-Linux
./ArchitectsLog-Linux
```

---

## Run From Source

Prefer to run it directly? Clone the repository and launch it from the command line:

```bash
git clone https://github.com/CanMatthewCode/ArchitectsLog.git
cd ArchitectsLog/src
python architectsLog_main.py
```

**Requirements:**
- Python 3.x
- Dependencies listed in `requirements.txt` (run `pip install -r requirements.txt`)

---

## Contributing

Found a bug or have a feature request? Open an issue or submit a pull request — contributions are welcome.

---

## License

This project is licensed under the [MIT License](LICENSE).
