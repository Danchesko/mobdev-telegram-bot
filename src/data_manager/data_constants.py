from src.parsers import (kivano_parser, mistore_parser, myphone_parser, 
ostore_parser, softech_parser, svetofor_parser, beeshop_parser, mostovoy_parser)

MAX_ARCHIVE_DAYS = 31
COMPARE_RESULT_NAME = "result.xlsx"
DATA_FOLDER = "../../data/"
PARSERS = {
    "kivano.kg": kivano_parser,
    "mistore.kg": mistore_parser,
    "myphone.kg": myphone_parser,
    "ostore.kg": ostore_parser,
    "softech.kg": softech_parser,
    "svetofor.kg": svetofor_parser,
    "beeshop.kg": beeshop_parser,
    "mostovoy.kg": mostovoy_parser
    }
