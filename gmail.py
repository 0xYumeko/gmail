import requests

def check_email(email):
    """Check if an email is disposable or not."""
    url = f'https://gmailcheck.pythonanywhere.com/?gmail={email}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["check"]

def read_emails_from_file(file_name):
    """Read emails from a file and return them as a list."""
    with open(file_name, 'r') as file:
        emails = [line.strip() for line in file]
    return emails

def main():
    """Main function to run the script."""
    file_name = input("[+] Enter List :")
    print("[!] Start Check Emails Just Wait... [!]")
    emails = read_emails_from_file(file_name)

    for email in emails:
        is_disposable = check_email(email)
        print(f"{email} : {is_disposable}")

if __name__ == "__main__":
    main()