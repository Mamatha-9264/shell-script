latency_data=[12,34,56,10,89,23]
def calculate_average(data):
    return sum(data)/len(data)
def get_summary(data):
     summary={"min":min(data),"max":max(data),"average":calculate_average(data)}
     return summary
result=get_summary(latency_data)
print("Latency Summary:", result)