import os
import pandas as pd
from src import constants
from src.constants import Phone
from src.data_manager import date_builder
from src.data_manager import data_constants

     
def show_archive(data_folder = data_constants.DATA_FOLDER):
    archive = []
    current_date = date_builder.get_current_date()
    for file in os.listdir(data_folder):
        try:
            date = date_builder.get_file_date_name(file)
            if (current_date - date).days<=data_constants.MAX_ARCHIVE_DAYS:
                 archive.append(file)
        except ValueError:
            continue
    return archive


def compare_data(text, data_folder = data_constants.DATA_FOLDER):
    arguments = text.split(" ")[1:]
    message = check_arguments(arguments, data_folder)
    if not message:
        dfs = [pd.read_excel(data_folder+file +'.xlsx') for file in arguments]
        datasets = analyze_datasets(dfs[0],dfs[1])
        buffer = create_xlsx(datasets,data_constants.COMPARE_RESULT_NAME)
        return buffer
    return message


def check_arguments(arguments, data_folder):
    if len(arguments)!=2:
        return (constants.INVALID_ARGUMENT_MESSAGE % (" ".join(arguments)))
    if not all(file +'.xlsx' in os.listdir(data_folder) for file in arguments):
        return constants.UNABLE_MESSAGE


def analyze_datasets(df1, df2):
    old_phones = df1.loc[df1.index.difference(df2.index)]
    new_phones = df2.loc[df2.index.difference(df1.index)]
    same_phones = pd.merge(df1,df2[Phone.PRICE].to_frame(name = Phone.PRICE_AFTER), left_index=True, right_index=True)
    price_changed_phones = same_phones[same_phones[Phone.PRICE]!=same_phones[Phone.PRICE_AFTER]]
    price_changed_phones = price_changed_phones[[Phone.TITLE, Phone.PRICE,Phone.PRICE_AFTER, Phone.SHOP]]
    return [old_phones, new_phones, price_changed_phones]


def create_xlsx(datatasets, filename):
    writer = pd.ExcelWriter(filename)
    datatasets[0].to_excel(writer, sheet_name = "Out of stock")
    datatasets[1].to_excel(writer, sheet_name = "New phones")
    datatasets[2].to_excel(writer, sheet_name = "Price changed")
    writer.save()
    buffer = open(filename, 'rb')
    return buffer