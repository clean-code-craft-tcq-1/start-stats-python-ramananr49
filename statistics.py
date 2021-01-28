
def calculateStats(numbers):
  Max_number = Min_number = avg_number = float('nan')
  
  if len(numbers) != 0;
    Max_number = max(numbers)
    Min_number = min(numbers)
    avg_number = sum(numbers)/len(numbers)
    
  return {"avg": avg_number, "min": Min_number, "Max" : Max_number}

class StatsAlerter:
  def_init_(self, max_threshold, stats_alerters):
    self.max_threshold = max_threshold
    self.stats_alerters = stats_alerters
    
  def checkAndAlert(self, values):
    for value in values
      if value >= self.max_threshold:
        for alerter in self.stats_alerters:
          alerter.alert()
