# Finding the Most Profitable Investment in APAC Using Python

This repo is an updated companion to the [PyCon APAC 2024 lecture](https://www.youtube.com/watch?v=6e53cVVjlTw).

> **Disclaimer: This analysis is educational and is not investment advice.**

## Run the notebook

1. Install the dependencies with `uv sync` (Python 3.14 or newer).
2. Open [the notebook](lecture.ipynb) in your editor and select the project's `.venv` kernel.
3. Run its cells in order. By default, it uses the saved [lecture ticker list](lecture_tickers.json). Set `use_lecture_snapshot = False` in the notebook to collect current symbols instead.

The price download is large and Yahoo Finance may rate-limit it. Completed batches are saved in `asset_metrics_cache/`, so rerunning the calculation cell resumes from the remaining batches. Download caches and `yfinance_download.log` are ignored by Git. Current price data and calculations may produce different results from the 2024 lecture.

The [lecture slides](lecture.pdf) are included for reference. The notebook presents rankings calculated from available Yahoo Finance data and their known limitations.
