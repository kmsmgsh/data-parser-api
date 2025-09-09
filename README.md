# Data Parser API

A simple FastAPI server to serve documents from a data folder via REST endpoints.

## Features

- 🚀 FastAPI-based REST API
- 📁 Serve files from `/data/` directory
- 🔒 Path traversal protection
- 📋 File listing endpoint
- 🌐 Network accessible (configurable)

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Server

```bash
python main.py
```

The server will start on `http://0.0.0.0:8005`

### 3. Access Your Files

- **List all files**: `GET http://localhost:8005/data/`
- **Download a file**: `GET http://localhost:8005/data/{filename}`
- **API status**: `GET http://localhost:8005/`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API status message |
| GET | `/data/` | List all files in data directory |
| GET | `/data/{filename}` | Download specific file |

## Example Usage

```bash
# Check API status
curl http://localhost:8005/

# List available files
curl http://localhost:8005/data/

# Download iris.csv
curl http://localhost:8005/data/iris.csv
```

## Adding Your Own Files

Simply place any files in the `/data/` directory and they'll be accessible via the API:

```
data/
├── iris.csv          # → /data/iris.csv
├── report.pdf        # → /data/report.pdf
└── dataset.json      # → /data/dataset.json
```

## Security Features

- Path traversal attack prevention
- File existence validation
- Directory boundary enforcement
- No execution of uploaded files

## Configuration

To change the port or host, edit `main.py`:

```python
uvicorn.run(app, host="0.0.0.0", port=8005)
```

- `host="127.0.0.1"` - localhost only
- `host="0.0.0.0"` - accessible from network
- `port=8005` - change port number

## Project Structure

```
data_parser_source/
├── main.py           # FastAPI application
├── requirements.txt  # Python dependencies
├── data/            # Files to serve
│   └── iris.csv     # Sample dataset
└── README.md        # This file
```

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## License

MIT License