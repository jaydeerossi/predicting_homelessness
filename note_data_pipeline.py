import pandas as pd
import html2text


def note_data_pipeline():
    src_df = load_data()
    clean_df = data_quality_filter(src_df)
    return convert_html_to_clean_text(clean_df)


def data_quality_filter(df):
    return df.loc[~df['NOTE_HTML'].isna(),]


def convert_html_to_clean_text(df):
    clean = []
    html_transformer = html2text.HTML2Text()
    for index, row in df.iterrows():
        # convert to unicode to avioid UnicodeDecodeError
        html = unicode(row['NOTE_HTML'], errors='ignore')
        text = html_transformer.handle(html)
        clean.append(text)
    df['NOTE_TEXT'] = clean
    return df


def load_data():
    filename = 'S:\dcore-prj0107-SHARED\homelessness notes.csv'
    src_df = pd.read_csv(filename, header=None)
    src_df.columns = ['PAT_ID', 'DATE', 'OTHER_1', 'OTHER_2', 'OTHER_3', 'NOTE_TYPE', 'NOTE_HTML']
    return src_df


def test_note_data_pipeline(notes_df):
    print notes_df.sample()['NOTE_TEXT'].values[0]
    