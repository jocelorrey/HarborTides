from bs4 import BeautifulSoup

class TableParser:

  def _set_table(self, table):
    if table is None:
      self._valid_input = False
    else:
      self._valid_input = True
    self._table = table
  
  def __init__(self, table):
    self._set_table(table)
    self._key_index = None
    self._value_indices = None

  def _set_output_key_val_indices(self, key_index, value_indices):
    self._key_index = key_index
    self._value_indices = value_indices
  
  def _parse_to_dict(self, **kwargs):
    table = kwargs.get('table', self._table)
    output = {}
    rows = table.find_all('tr')

    for r in rows:
      table_data = r.find_all('td')
      row = [i.text for i in table_data]

      if len(row) != 0:
        try:
          key = row[self._key_index]
          values = []
          for i in self._value_indices:
            values.append(row[i])
          
          output[key] = values
        
        except IndexError:
          pass
    
    return output