# subdomain_enum.py

import dns.resolver
import concurrent.futures

def enumerate_subdomains(domain, subdomains, max_threads=10):
    found_subdomains = []

    def check_subdomain(subdomain):
        try:
            full_domain = f"{subdomain}.{domain}"
            answers = dns.resolver.resolve(full_domain, 'A')
            print(f"[+] Found: {full_domain}")
            return full_domain
        except dns.resolver.NXDOMAIN:
            return None

    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        results = executor.map(check_subdomain, subdomains)
    
    for result in results:
        if result:
            found_subdomains.append(result)
    
    return found_subdomains
