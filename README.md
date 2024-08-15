VulnScanner

VulnScanner is a lightweight CLI tool designed to scan web applications for common vulnerabilities like SQL injection, XSS, and CSRF. The tool also allows for subdomain enumeration and advanced XSS detection across those subdomains.

Features

- Subdomain Enumeration: Enumerates subdomains for a given domain.
- XSS Vulnerability Scanning: Scans for XSS vulnerabilities in the discovered subdomains.
- Dynamic Payload Generation: Generates payloads dynamically based on the content of web pages.
- Multithreading: Speeds up subdomain enumeration and scanning using multithreading.
- User Agent Spoofing: Option to spoof user agents to avoid detection.
- Results Storage: Stores scan results in a CSV file for further analysis.

Installation

1. Clone the repository:

    git clone https://github.com/VIRTUAL-VIRUZ
    cd vulnscanner

2. Install dependencies:

    pip install -r requirements.txt

Usage

    python cli.py --url example.com --subdomains subdomains.txt --threads 20 --output scan_results.csv

- --url: Target domain for vulnerability assessment.
- --subdomains: File containing a list of common subdomains.
- --threads: Number of threads to use for scanning (default: 10).
- --output: File to save the scan results (default: results.csv).

Example

    python cli.py --url example.com --subdomains subdomains.txt --threads 20 --output scan_results.csv

This command will enumerate subdomains for example.com, scan each subdomain for XSS vulnerabilities, and save the results to scan_results.csv.

Requirements

- Python 3.x
- Libraries listed in requirements.txt

License

This project is licensed under the MIT License - see the LICENSE file for details.

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

Contact

- Author: Muhammed Farhan
- Email: farhanfarhan1003@gmail.com
