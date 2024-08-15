# cli.py

import argparse
from subdomain_enum import enumerate_subdomains
from utils import sanitize_url
from xss_scanner import dynamic_xss_scan, store_results

def main():
    parser = argparse.ArgumentParser(description="Advanced Vulnerability Assessment Tool")
    parser.add_argument("--url", required=True, help="Target domain for vulnerability assessment")
    parser.add_argument("--subdomains", required=True, help="File containing a list of common subdomains")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads to use for scanning")
    parser.add_argument("--output", default="results.csv", help="File to save the scan results")

    args = parser.parse_args()
    
    domain = sanitize_url(args.url)
    
    with open(args.subdomains, 'r') as f:
        subdomains = f.read().splitlines()
    
    print(f"[*] Enumerating subdomains for {domain}...")
    found_subdomains = enumerate_subdomains(domain, subdomains, max_threads=args.threads)
    
    print(f"[*] Scanning for XSS vulnerabilities...")
    vulnerabilities = []
    for subdomain in found_subdomains:
        if dynamic_xss_scan(f"http://{subdomain}"):
            vulnerabilities.append({
                'URL': f"http://{subdomain}",
                'Vulnerability': 'XSS',
                'Payload': 'Payload details here'
            })
    
    store_results(vulnerabilities, output_file=args.output)
    
if __name__ == "__main__":
    main()
