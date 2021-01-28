
def calculateStats(numbers):
  Max_number = Min_number = avg_number = float('nan')
  
  if len(numbers) != 0:
    Max_number = max(numbers)
    Min_number = min(numbers)
    avg_number = sum(numbers)/len(numbers)
    
  return {"avg": avg_number, "min": Min_number, "Max" : Max_number}

class EmailAlert:
  def _init_ (self):
    self.emailSent = False
    
  def alert(self):
    self.emailSent = True
    
    
class LEDAlert:
  def _init_ (self):
    self.ledGlows = False
    
  def alert(self):
    self.ledGlows = Ture
    
class StatsAlerter:
  def checkAndAlert(self, values):
    for value in values:
      for alerter in self.stats_alerters:
        alerter.alert()
          

