import whois  # pip install whois
import sys

try:
    domain = whois.whois("copyassignment.com")
    if domain.domain_name is None:
        sys.exit(1)
except:
    print("This domain is available")
else:
    print("Oops! this domain alrady purchased")
