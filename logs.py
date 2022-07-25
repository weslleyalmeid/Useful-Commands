# https://docs.python.org/3/library/logging.html

import os.path                                      # lib para obter diretorios
import glob                                         # lib de pegar todos os arquivos de pasta especifica
import pandas as pd
import ipdb                                         # lib de debug
import io                                           
import logging
from logging import basicConfig                     # configuracao do logging
from logging import DEBUG, INFO                     # levels
from logging import FileHandler, StreamHandler      # Mostrar log no terminal e pode salver em N arquivos
from logging import Formatter, Filter               # Personalizar levels no handler

# format_file_handler = Formatter(
#     '%(levelname)s:%(asctime)s:%(lineno)d:%(message)s'
# )

# file_handler = FileHandler('check_types_log.txt', 'a'),   # escreve no arquivo
# file_handler.setlevel('ERROR')
# file_handler.setFormatter(format_file_handler)

format_stream_handler = Formatter(
    '%(levelname)s:%(asctime)s:linha %(lineno)d:%(message)s'
)

stream_handler = StreamHandler()
stream_handler.setLevel('ERROR')
stream_handler.setFormatter(format_stream_handler)

basicConfig(
    level=DEBUG,
    format='%(levelname)s:%(asctime)s:%(message)s',
    handlers=[
        FileHandler('logs/check_types_log.txt', 'a', 'utf-8'),   # escreve no arquivo
        stream_handler,                                          # escreve no terminal personalizado
        StreamHandler()
    ]
)


# utilizado em outras arquivos, para obter os logs ajustados
log = logging.getLogger(__name__)

def step_line(name_file, title=None):

    if title:
        with open(name_file, 'a') as f:
            f.write(f'### {title} \n')
    else:
        with open(name_file, 'a') as f:
            f.write('\n')
            f.write('\n')

def write_file_info(df):
    try:
        buffer = io.StringIO()
        df.info(buf=buffer)
        information = buffer.getvalue()

        with open('output/info.txt', 'a', newline='', encoding='utf-8') as f:
            f.write(information)
            f.write('\n')
    except Exception as e:
        logging.error('Erro no write_file_info', exc_info=e)

def write_file_dtypes(name_col, df):
    try:
        df = df.dtypes.rename(name_col)
        name_file = 'output/dtypes.md'
        step_line(name_file, title=name_col)
        df.to_markdown(name_file, mode='a')
        step_line(name_file)
    except Exception as e:
        logging.error('Erro no write_file_dtypes', exc_info=e)

def write_file(name_col, df):
    try:
        dict_data = {
            'COLUMNS': df.dtypes.index,
            'TYPES': df.dtypes.values,
            'NULL': df.isnull().sum().values
        }
        
        df = pd.DataFrame(data=dict_data)
        
        name_file = 'output/info_dtypes.md'
        step_line(name_file, title=name_col)
        df.to_markdown(name_file, mode='a', index=False)
        step_line(name_file)
    except Exception as e:
        logging.error('Erro no write_file', exc_info=e)

def init_export(name_file, df):
    try:
        # ipdb.set_trace()

        write_file_info(df)
        write_file_dtypes(name_file, df)
        write_file(name_file, df)

        # ipdb.set_trace()

    except Exception as e:
        logging.error('Erro no init_export', exc_info=e)

def main():
    
    DIR_ROOT = os.path.abspath('.')   
    DIR_BASE = os.path.join(DIR_ROOT, 'ABACATE')
    

    logging.debug('Diretorio ajustado')

    names_file = [os.path.basename(x) for x in glob.glob(f"{DIR_BASE}/*.xlsx") if '~' not in x]

    logging.debug('Diretorio ajustado')

    logging.info(names_file)

    route_read = {
        'sheet_off':[
                        'ABACATE',
                        'LARANJA'
                    ],
        'sheet_on':{ 
                        'LARANJA': ['ABACATE', 'LARANJA'],
                    }
    }

    for file in names_file:
        logging.info(file.upper())
        data = os.path.join(DIR_BASE, file)
        # name_file = file.partition('-')[0].strip()
        name_file = file.split('.')[0].strip()

        # ipdb.set_trace()

        if name_file in route_read['sheet_off']:
            try:
                
                # ipdb.set_trace()

                df = pd.read_excel(data)

                # ipdb.set_trace()

                init_export(name_file, df)

                # ipdb.set_trace()
                logging.info(f'ESCRITO COM SUCESSO:{name_file}')


            except Exception as e:
                logging.error(f'Erro no sheet_off {name_file}', exc_info=e)
        else:
            try:
                # ipdb.set_trace()
                sheets = route_read['sheet_on'].get(name_file)
                # ipdb.set_trace()

                for sheet in sheets:
                    # ipdb.set_trace()
                    logging.info(f'Nome arquivo:{name_file} e Sheet:{sheet} ')
                    df = pd.read_excel(data, sheet_name=sheet)
                    # ipdb.set_trace()
                    name_sheet = f'{name_file} - {sheet}'
                    init_export(name_sheet, df)
                    logging.info(f'ESCRITO COM SUCESSO:{name_file} - {sheet} ')
                    # ipdb.set_trace()
            except Exception as e:
                logging.error(f'Erro no sheet_on {name_file}', exc_info=e)

if __name__ == "__main__":
    main()