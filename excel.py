import os
import pandas as pd

# 分批 读取 excel 数据
HERE = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = HERE


def make_df_from_excel(file_name, nrows):
    """Read from an Excel file in chunks and make a single DataFrame.

    Parameters
    ----------
    file_name : str
    nrows : int
        Number of rows to read at a time. These Excel files are too big,
        so we can't read all rows in one go.
    """
    file_path = os.path.abspath(os.path.join(DATA_DIR, file_name))
    # xl = pd.ExcelFile(file_path)

    # In this case, there was only a single Worksheet in the Workbook.
    # sheetname = xl.sheet_names[0]

    # Read the header outside of the loop, so all chunk reads are
    # consistent across all loop iterations.
    df_header = pd.read_excel(file_path, sheet_name='Sheet1', nrows=1)
    print(f"Excel file: {file_name} (worksheet: {'Sheet1'})")

    chunks = []
    i_chunk = 0
    # The first row is the header. We have already read it, so we skip it.
    skiprows = 1
    while True:
        df_chunk = pd.read_excel(
            file_path, sheet_name='Sheet1',
            nrows=nrows, skiprows=skiprows, header=None)
        skiprows += nrows
        # When there is no data, we know we can break out of the loop.
        if not df_chunk.shape[0]:
            break
        else:
            print(f"  - chunk {i_chunk} ({df_chunk.shape[0]} rows)")
            chunks.append(df_chunk)
        i_chunk += 1

    df_chunks = pd.concat(chunks)
    # Rename the columns to concatenate the chunks with the header.
    columns = {i: col for i, col in enumerate(df_header.columns.tolist())}
    df_chunks.rename(columns=columns, inplace=True)
    df = pd.concat([df_header, df_chunks])
    return df


if __name__ == '__main__':
    df = make_df_from_excel('果蔬干_0.xlsx', nrows=10000)