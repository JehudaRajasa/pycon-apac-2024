import pandas as pd
import yfinance as yf

country_names = {
    "au": "Australia",
    "ca": "Canada",
    "id": "Indonesia",
    "jp": "Japan",
    "kr": "South Korea",
    "my": "Malaysia",
    "nz": "New Zealand",
    "sg": "Singapore",
    "th": "Thailand",
    "us": "United States",
    "tw": "Taiwan",
    "hk": "Hong Kong",
    "cn": "China",
    "mx": "Mexico",
    "cl": "Chile",
    "in": "India",
}
# Map each Yahoo exchange code to the country of that exchange, e.g. "BSE" -> "India".
exchange_countries = {
    exchange: country_names[region]
    for region, exchanges in yf.EquityQuery("eq", ["region", "us"])
    .valid_values["exchange"]
    .items()
    if region in country_names
    for exchange in exchanges
}
exchange_countries["OID"] = (
    "United States"  # OTCID, a US OTC market missing from yfinance's list
)
asset_details = {}


def add_asset_details(ranking):
    for symbol in ranking.index:
        if symbol in asset_details:
            continue

        try:
            info = yf.Ticker(symbol).get_info() or {}
        except Exception as error:  # noqa: BLE001 - Optional metadata must not stop rankings.
            print(f"Metadata unavailable for {symbol}: {error}")
            info = {}

        asset_details[symbol] = {
            "Country": exchange_countries.get(info.get("exchange"), "Unavailable"),
            "Sector": "ETF"
            if info.get("quoteType") == "ETF"
            else info.get("sector") or "Unavailable",
        }

    details = pd.DataFrame.from_dict(asset_details, orient="index").reindex(
        index=ranking.index, columns=["Country", "Sector"]
    )

    return details.join(ranking)
