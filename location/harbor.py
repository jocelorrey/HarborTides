class Harbor:
  # formats it like xxx-harbor
  def __init__(self, input_name):
    name = input_name.lower().strip(' ')
    if ' harbor' in name:
      self.name = name.replace(' ', '-')
    else:
      self.name = name + '-harbor'