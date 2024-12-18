import importlib
import app.data.source_contracts
import app.data.source_items
import app.data.source_MSG_Reports
import ast
from app.viewmodels.cht_crawlers import CsCHTCrawler
from app.config import *
from app.utils.common import fn_log


def convert_string_to_dict(input_string):
    result = {}
    current_key = ""
    in_brackets = False
    bracket_content = ""

    for char in input_string:
        if char in "{[":
            in_brackets = True
            bracket_content = char
        elif char in "]}":
            in_brackets = False
            bracket_content += char
            result[current_key.rstrip(":").strip()] = ast.literal_eval(bracket_content)
            current_key = ""
        elif char == "," and not in_brackets:
            if current_key and current_key.rstrip(":").strip() not in result:
                result[current_key.rstrip(":").strip()] = None
            current_key = ""
        elif in_brackets:
            bracket_content += char
        else:
            current_key += char

    if current_key and current_key.rstrip(":").strip() not in result:
        result[current_key.rstrip(":").strip()] = None

    return result


def main():
    cht_crawler = CsCHTCrawler()

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
            "EPIS_contract_batch": lst_source_contracts,
            "EPIS_contract_info_items": lst_source_contracts,
            "MASIS_barcode": {
                "23F13A1391": [
                    "007",
                    "010",
                    "023",
                    "024",
                    "060",
                    "077",
                    "080",
                    "081",
                    "081",
                    "095",
                ],
                "23V13A0301": ["048", "049"],
            },
            "MASIS_item_detail": lst_items,
            "MSG": lst_source_MSG_reports,
            "MASIS_InvQry": ["50503", "59511", "59512", "59521", "59531"],
        }
        tasks = ""
        tasks = convert_string_to_dict(
            input(f"tasks:\n {"\n ".join(configs.keys())}\nor stop:")
        )
        print(f"input tasks: {set(tasks)}")
        # config = tasks['config'] if 'config' in
        for task, source in tasks.items():
            match task:
                case "stop":
                    handle_stop = True
                    break
                case "debug":
                    breakpoint()
                    pass
                case None:
                    pass
                case _:
                    if task not in cht_crawler._loaded_components:
                        cht_crawler.load_components(task)
                    getattr(cht_crawler, task + "_handler")(
                        source if source else configs.get(task)
                    )
    fn_log("Jobs done!!")
    cht_crawler.close()
    cht_crawler.quit()


if __name__ == "__main__":
    main()


# cht_crawler.load_components('MSG')
# cht_crawler.MSG_handler(source=[{'name' : 'RS4107RA4L'}], handle_check_online=False)
