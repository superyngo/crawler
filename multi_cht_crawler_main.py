import importlib
import app.data.source_MSG_Reports
import app.data.source_contracts
import app.data.source_items
import ast
from app.config import *
from app.viewmodels.cht_crawlers import CsMultiCHTCrawler
from app.utils.common import fn_log
def convert_string_to_dict(input_string):
  result = {}
  current_key = ''
  in_brackets = False
  bracket_content = ''

  for char in input_string:
      if char == '{':
          in_brackets = True
          bracket_content = '{'
      elif char == '}':
          in_brackets = False
          bracket_content += '}'
          result[current_key.rstrip(':')] = ast.literal_eval(bracket_content)
          current_key = ''
      elif char == ',' and not in_brackets:
          if current_key and current_key.rstrip(':') not in result:
              result[current_key.rstrip(':')] = {}
          current_key = ''
      elif in_brackets:
          bracket_content += char
      else:
          current_key += char

  if current_key and current_key.rstrip(':') not in result:
      result[current_key.rstrip(':')] = {}

  return result


def main():
  cht_multi_crawler = CsMultiCHTCrawler()
  handle_stop = False
  while not handle_stop:
    importlib.reload(app.data.source_contracts)
    importlib.reload(app.data.source_items)
    importlib.reload(app.data.source_MSG_Reports)
    from app.data.source_contracts import lst_source_contracts
    from app.data.source_items import lst_items
    from app.data.source_MSG_Reports import lst_source_MSG_reports
    # test
    # lst_source_contracts = ["23S13A0041","23R13A0051"]
    # lst_items = ["02502735","21190613"]
    # lst_source_MSG_reports = [{'name' : 'RS4212RA4L','postfix' : '50502'}] # {'name' : 'RS5203A' , 'prefix' : '20240110'} 
    configs = {
    'EPIS_contract_batch' : {
      'source' : lst_source_contracts,
      'task' : 'EPIS_contract_batch',
      'threads' : 2
    },
    'EPIS_contract_info_items':{
      'source' : lst_source_contracts,
      'task' : 'EPIS_contract_info_items',
      'threads' : 3
    },
    'MASIS_barcode' : {
      'source' : {"23B12A2491":["1","2",3,4,5]},
      'task' : 'MASIS_barcode',
      'threads' : 2
    },
    'MASIS_item_detail' : {
      'source' : lst_items,
      'task' : 'MASIS_item_detail',
      'threads' : 4
    },
    'MSG' : {
      'source' : lst_source_MSG_reports,
      'task' : 'MSG',
      'threads' : 1
    },
    'MASIS_InvQry' : {
      'source' : ['50503', '59511', '59512', '59521', '59531'],
      'task' : 'MASIS_InvQry',
      'threads' : 2
  }}

    tasks = convert_string_to_dict(input(f"tasks:\n {"\n ".join(configs.keys())}\nor stop:"))
    print(f"input tasks: {set(tasks)}")
    # config = tasks['config'] if 'config' in 
    for task, config in tasks.items():
      match task:
        case 'stop':
          handle_stop = True
          break
        case 'debug':
          breakpoint()
          pass
        case None:
          pass
        case _:
          cht_multi_crawler.crawling_main(**(configs[task]|config))
  cht_multi_crawler.threads = 0
  fn_log("All jobs done!!")

if __name__ == "__main__":
    main()


# MSG:{'handle_check_online':False}