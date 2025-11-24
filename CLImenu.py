def ip_reachability():
    ip=input("Enter an IP address")
    print(f"pinging{ip}...")
    print("IP reachability test completed(dummy output)")
          
def calculate_average(data):
    return sum(data)/len(data)
def get_summary(data):
        return{"min":min(data),"max":max(data),"average":calculate_average(data)}
while True:
     print("\n=== MENU ===")
     print("1. Test IP Reachability")
     print("2. Compute latency summary")
     print("3. Exit")
     choice = input("Enter your choics")
     if choice == "1":
          ip_reachability()
     elif choice == "2":
          raw_values = input("Enter comma-separated latency values: ")
          data =[float(x) for x in raw_values.split(",")]
          summary=get_summary(data) 
          print("Latency Summary:", summary)    
     elif choice == "3":
          print("Exciting the program.")
          break
     else:
          print("Invalid choice! please choose 1,2 or 3.")

