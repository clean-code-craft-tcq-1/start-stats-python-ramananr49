
def calculateStats(numbers):
  Max_number = Min_number = avg_number = float('nan')
  
  if len(numbers) != 0;
    Max_number = max(numbers)
    Min_number = min(numbers)
    avg_number = sum(numbers)/len(numbers)
    
  return {"avg": avg_number, "min": Min_number, "Max" : Max_number}
