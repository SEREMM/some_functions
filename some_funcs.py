import pandas as pd

def read_gsheet_shared(sheet_id, sheet_name):
  '''
  Easy and fast read gsheet.
  Receives:
    sheet_id (string): Example "2y1kdVoBif48Kq8s7aUeBEQ4Omzvo3y1aqi495LOZVme"
    sheet_name (string): Name of sheet, example "abril"
  Returns:
    A dataframe of the csv in the gsheet.
  '''
  id = sheet_id
  name = sheet_name
  gsheet_url = 'https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}'.format(id, name)
  df = pd.read_csv(gsheet_url)
  return df
