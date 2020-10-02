# code to check domaini availablity using python

# pip install python-whois
import whois
import sys

try:
    domain = whois.whois("")
    if domain.domain_name = None:
        sys.exit(1)
except:
    print("This Domain is available")   
    else:
        print("Oops! this domain is already purchased")
