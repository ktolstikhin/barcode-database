# Product Barcode Database

This script is used to parse the [UhttBarcodeReference](https://github.com/papyrussolution/UhttBarcodeReference) repository of products' barcodes and create SQLite database from the parsed records.

## Install

```bash
pip3 install --user -r requirements.txt
```

## Usage

```bash
./makedb.py -c UhttBarcodeReference/DATA/*.csv -d barcodes.sqlite
```

