import pandas as pd
class LoadCSV():
    '''Class for loading a CSV file into a Pandas Dataframe'''

    def __init__(self, data_path, encoding=None):
        '''
        Initialization Method
        :param data_path: local disk path where the data is located
        :param encoding: CSV encoding
        #Python standard encodings list. Source: https://docs.python.org/3/library/codecs.html#standard-encodings
        '''
        self.data_path = data_path
        self.encoding = encoding
        self.df = pd.DataFrame()
        super().__init__()

    def __call__(self):
        '''
        Perform data activity here
        :return: dataframe object
        '''
        applicable_encodings=[]
        if self.encoding is None:
            applicable_encodings=self.detect_encoding(file_name=self.data_path)
        else:
            applicable_encodings.append(self.encoding)

        for l,l_encoding in enumerate(applicable_encodings):
            try:
                self.df = pd.read_csv(self.data_path, encoding=l_encoding)
                #if encoding was sucessfuly read break from the applicable_encodings loop
                break
            except Exception as e:
                print(e)

        return self.df

    def detect_encoding(self,file_name):
        '''
        This function detects the Python standard encoding of an input file.
        :param file_name: Input file name in column format (.csv)
        :return: list of applicable encodings for this file
        '''

        #Python standard encodings list. Source: https://docs.python.org/3/library/codecs.html#standard-encodings
        encoding_list = ['utf-8', 'ISO-8859-1','utf_8_sig', 'ascii', 'latin-1', 'cp-424', 'big5', 'big5hkscs', 'cp037', 'cp273', 'cp424', 'cp437',
                        'cp500', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp856', 'cp857', 'cp858', 'cp860', 'cp861',
                        'cp862','cp863', 'cp864', 'cp865', 'cp866', 'cp869', 'cp874', 'cp875', 'cp932', 'cp949', 'cp950', 'cp1006',
                        'cp1026', 'cp1125', 'cp1140', 'cp1250', 'cp1251', 'cp1251', 'cp1252', 'cp1253', 'cp1254', 'cp1255', 'cp1256',
                        'cp1257', 'cp1257', 'cp65001', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213', 'euc_kr', 'gb2312', 'gbk',
                        'gb18030', 'hz', 'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004', 'iso2022_jp_3',
                        'iso2022_jp_ext', 'iso2022_kr', 'iso8859_2', 'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6',
                        'iso8859_7', 'iso8859_8', 'iso8859_9', 'iso8859_10', 'iso8859_11', 'iso8859_12', 'iso8859_13', 'iso8859_14',
                        'iso8859_15', 'iso8859_16', 'johab', 'koi8_r', 'koi8_t', 'koi8_u', 'kz1048', 'mac_cyrillic', 'mac_greek',
                        'mac_iceland', 'mac_latin2', 'mac_roman', 'mac_turkish', 'ptcp154', 'shift_jis', 'shift_jis_2004',
                        'shift_jisx0213', 'utf_32', 'utf_32_be', 'utf_32_le', 'utf_16', 'utf_16_be', 'utf_16_le', 'utf_7']

        valid_encodings=[]
        for i,l_encoding in enumerate(encoding_list):
            try:
                df = pd.read_csv(file_name, encoding=l_encoding)
                valid_encodings.append(l_encoding)
                break
            except Exception as e:
                print('detect_encoding(): Encoding '+l_encoding+' is not applicable')
        return valid_encodings