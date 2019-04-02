import json
from urllib import parse


class Nation:
  def __init__(self, path, path_out):
    self.datafile = open(path, encoding='utf8')
    self.file_out = open(path_out, 'w', encoding='utf8')
    self.json_data = json.load(self.datafile)
    self.start = 0
    self.end = len(self.json_data) - 1

  def __iter__(self):
    return self

  def __next__(self):
    if self.start < self.end:
      country = self.json_data[self.start]['name']['common']
      wikiurl = "https://ru.wikipedia.org/w/index.php?"
      value = {'search': country}
      mydata = parse.urlencode(value)
      myurl = wikiurl + mydata
      output_line = country + ':' + '\n' + myurl + '\n'

      self.start += 1
      return self.file_out.write(output_line)

    else:
      raise StopIteration

def main():
  if __name__ == '__main__':
    for item in Nation('countries.json', 'output.txt'):
      pass
main()
