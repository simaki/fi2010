import pandas


def fetch_fi2010(normalization=None) -> pandas.DataFrame:
    """
    Load the FI2010 dataset with no auction.

    Benchmark Dataset for Mid-Price Forecasting of Limit Order Book Data with Machine
    Learning Methods. A Ntakaris, M Magris, J Kanniainen, M Gabbouj, A Iosifidis.
    arXiv:1705.03233 [cs.CE].  https://arxiv.org/abs/1705.03233

    Parameters
    ----------
    normalization : {"zscore", None}
        Normalization method.
    """
    if normalization is None:
        url = "https://raw.githubusercontent.com/simaki/fi2010/main/data/data.csv"
        return pandas.read_csv(url, index_col=0)
    if normalization == "zscore":
        url1 = "https://raw.githubusercontent.com/simaki/fi2010/main/data/data_zscore1.csv"
        url2 = "https://raw.githubusercontent.com/simaki/fi2010/main/data/data_zscore2.csv"
        return pandas.concat([pandas.read_csv(url1, index_col=0), pandas.read_csv(url2, index_col=0)])

