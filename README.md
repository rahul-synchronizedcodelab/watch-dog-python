# Watchdog

Watchdog is a Python project designed to monitor files dynamically created in a file system, and automatically upload them to an S3 bucket. This is achieved through a Python script that watches for changes in specified directories and performs the upload to an S3 bucket.

## Key Features

- Monitors the file system for changes in specified directories.
- Automatically uploads modified or newly created files to an S3 bucket.

## Getting Started

Follow these steps to set up and run the Watchdog project on your local machine.

### Prerequisites

- Python 3.10+
- [AWS CLI](https://aws.amazon.com/cli/) configured with the necessary S3 bucket access credentials.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/rahul-synchronizedcodelab/watch-dog-python.git
    cd watchdog
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Watchdog script with arguments:

    ```bash
    python script.py adv_number filepath
    ```

   - `adv_number`: The advertisement number associated with the file.
   - `filepath`: The path to the file or directory to be watched.

## Usage

Provide additional details on how users can interact with and customize the Watchdog script for their specific use cases.

## Contributing

If you would like to contribute to this project, please follow these guidelines. Contributions can include bug reports, feature requests, or code contributions.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add your feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## License

This project is licensed under the [License] - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements

- Mention any third-party libraries or tools used in the development of Watchdog.
- Give credit to any external resources or inspiration.