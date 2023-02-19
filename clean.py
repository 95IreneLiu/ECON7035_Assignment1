import pandas as pd


def clean(input_file):
    df1 = pd.read_csv("respondent_contact.csv")
    df2 = pd.read_csv("respondent_other.csv")
    df = df2.rename(columns=({"id": "respondent_id"}), inplace=True)
    df = pd.merge(df1, df2, on="respondent_id", how="outer")
    df = df.dropna()
    df.loc[df["job"].str.contains("insurance", case=False)]
    df = df.drop([12, 181])
    return df


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='contact_info_file (CSV)')
    parser.add_argument('input', help='other_info_file (CSV)')
    parser.add_argument('output', help='output_file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input)
    cleaned.to_csv(args.output, index=False)
    output_file = pd.read_csv(args.output)
    print(output_file.shape)

