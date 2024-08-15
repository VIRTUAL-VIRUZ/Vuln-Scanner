# xss_scanner.py

import requests
from bs4 import BeautifulSoup
import csv
import random

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"
    ]
    return random.choice(user_agents)

def generate_payloads(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    payloads = []
    
    # Example: Generate payloads based on input fields
    inputs = soup.find_all('input')
    for input_tag in inputs:
        name = input_tag.get('name')
        if name:
            payloads.append(f"{name}\"><script>alert(1)</script>")
            payloads.append(f"{name}=\"><img src=x onerror=alert(1)>")
    
    # Add default payloads as well
    payloads.extend([
        "<script>alert(1)</script>",
        "\"><script>alert(1)</script>",
        "'\"><img src=x onerror=alert(1)>"
    ])
    
    return payloads

def dynamic_xss_scan(url):
    headers = {'User-Agent': get_random_user_agent()}
    try:
        r = requests.get(url, headers=headers)
        payloads = generate_payloads(r.text)
        
        for payload in payloads:
            r = requests.get(url, params={"q": payload}, headers=headers)
            if payload in r.text:
                print(f"[!] XSS Vulnerability found with payload '{payload}' at {url}")
                return True
    except requests.RequestException as e:
        print(f"[!] Error scanning {url}: {str(e)}")
    print(f"[+] No XSS Vulnerability at {url}")
    return False

def store_results(vulnerabilities, output_file='results.csv'):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['URL', 'Vulnerability', 'Payload']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for vuln in vulnerabilities:
            writer.writerow(vuln)

    print(f"[+] Results saved to {output_file}")
