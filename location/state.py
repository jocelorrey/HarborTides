class State:
  ocean_states = {'alabama': 'al', 'alaska': 'ak', 'california': 'ca',
  'connecticut': 'ct', 'delaware': 'de', 'florida': 'fl', 'georgia': 'ga',
  'hawaii': 'hi', 'louisiana': 'la', 'maine': 'me', 'maryland': 'md',
  'massachusetts': 'ma', 'mississippi': 'ms', 'new hampshire': 'nh',
  'new jersey': 'nj', 'new york': 'ny', 'north carolina': 'nc',
  'oregon': 'or', 'rhode island': 'ri', 'south carolina': 'sc',
  'texas': 'tx','vermont': 'vt', 'virginia': 'va', 'washington': 'wa'}

  def is_valid_abbrev(self, name):
    return (len(name) == 2 and name in self.ocean_states.values())

  def is_valid_full_name(self, name):
    return (len(name) > 2 and name in self.ocean_states.keys())

  def is_ocean_state(self, state):
    return (state in self.ocean_states.keys() or
            state in self.ocean_states.values())

  def __init__(self, input_name):
      name = input_name.lower().strip(' ')
      if self.is_valid_abbrev(name):
        self.abbrev = name
      elif self.is_valid_full_name(name):
        self.abbrev = self.ocean_states[name]
      else:
        self.abbrev = None