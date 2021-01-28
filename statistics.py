def calculateStats(numbers):
    maximum_number = minimum_number = avg_number = float('nan')

    if len(numbers) != 0:
        maximum_number = max(numbers)
        minimum_number = min(numbers)
        avg_number = sum(numbers) / len(numbers)

    return {"avg": avg_number, "min": minimum_number, "max": maximum_number}


class EmailAlert:
    def __init__(self):
        self.emailSent = False

    def alert(self):
        self.emailSent = True


class LEDAlert:
    def __init__(self):
        self.ledGlows = False

    def alert(self):
        self.ledGlows = True


class StatsAlerter:
    def __init__(self, max_threshold, stats_alerters):
        self.max_threshold = max_threshold
        self.stats_alerters = stats_alerters

    def checkAndAlert(self, values):
        for value in values:
            if value >= self.max_threshold:
                for alerter in self.stats_alerters:
                    alerter.alert()
