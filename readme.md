
# Cleanup Script

This script organizes files in a specified directory based on predefined categories.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Configuration](#configuration)
- [Categories](#categories)
- [Log File](#log-file)

## Features

- Automatically organizes files into folders based on predefined categories.
- Logs details of the cleanup process.

## Usage

To use the script, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required Python libraries:

   ```bash
   pip install python-magic
   ```

3. Run the script using the following command:

   ```bash
   python cleanup_script.py
   ```

4. Optionally, you can customize the behavior by providing command-line arguments. See [Configuration](#configuration) for details.

## Configuration

The script can be configured using command-line arguments. Here are the available options:

- `--location`: Specify the directory to clean up. Default is the Downloads directory.
- `--log_file`: Specify the name of the log file. Default is a timestamped log file.

Example:

```bash
python cleanup_script.py --location "/path/to/your/directory" --log_file "custom_cleanup.log"
```

## Categories

The script organizes files into the following categories:

- Image
- Document
- Archive
- Executable
- Source

Each category corresponds to a specific folder where files of that type will be moved.

## Log File

The script generates a log file to record details of the cleanup process. The log file is named based on the timestamp when the script is executed.

Example log file name: `cleanup on {timestamp}.log`
