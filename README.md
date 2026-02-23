# Risk & Return Analysis - Stock Investment Advisor

A full-stack web application for analyzing stock risk and return profiles with AI-powered investment recommendations.

## Features

✅ **Company Analysis** - Enter any company name to get instant financial analysis
✅ **Risk & Return Metrics** - View annual returns, volatility, Sharpe ratio, P/E ratio, Beta, and more
✅ **Smart Recommendations** - Get BUY/SELL/HOLD recommendations based on risk-return analysis
✅ **Company Comparison** - Compare up to 5 companies side-by-side
✅ **Pre-loaded Data** - 20 major companies with real financial metrics
✅ **Beautiful UI** - Modern, responsive interface with smooth animations
✅ **Real-time Analysis** - Instant calculations using professional financial formulas

## Project Structure

```
DTDI Project/
├── backend/
│   └── app.py              # Flask API server
├── frontend/
│   └── index.html          # Web interface
├── data/
│   └── companies_data.csv  # Pre-loaded company financial data
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Technologies Used

- **Backend**: Python Flask, Pandas, NumPy
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Data**: CSV-based financial metrics
- **API**: RESTful Flask API with CORS support

## Quick Start

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Backend Server

```bash
python backend/app.py
```

The server will run on `http://localhost:5000`

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 3. Open the Frontend

Open the `frontend/index.html` file in your web browser, or serve it using Python:

```bash
python -m http.server 8000 --directory frontend
```

Then visit: `http://localhost:8000`

## How to Use

### Analyze a Single Company

1. **Enter company name** in the search box (e.g., "Apple", "Microsoft", "Google")
2. **Click "Analyze"** button
3. **View results**:
   - Investment recommendation (STRONG BUY / BUY / HOLD / WEAK HOLD / SELL)
   - Key financial metrics
   - Risk vs Return analysis
   - Key factors affecting the recommendation

### Compare Multiple Companies

1. **Select up to 5 companies** from the checkboxes in the "Compare" section
2. **Click "Compare Selected Companies"**
3. **View side-by-side comparison** in the table

### Available Companies

- Apple
- Microsoft
- Google
- Amazon
- Tesla
- Meta
- NVIDIA
- JPMorgan
- Berkshire Hathaway
- Johnson & Johnson
- Coca-Cola
- Walmart
- Visa
- Mastercard
- Adobe
- Intel
- AMD
- Netflix
- IBM
- Oracle

## Key Metrics Explained

### Annual Return (%)
Expected return on investment per year based on historical performance

### Volatility (%)
Standard deviation of returns; higher volatility = higher risk

### Sharpe Ratio
Risk-adjusted return metric. Formula: (Annual Return - Risk-Free Rate) / Volatility
- > 0.5: Good
- 0.3-0.5: Fair
- < 0.3: Poor

### Beta
Measures stock volatility relative to the market
- Beta = 1: Moves with market
- Beta > 1: More volatile than market
- Beta < 1: Less volatile than market

### P/E Ratio
Price-to-Earnings ratio
- Low P/E: Potentially undervalued
- High P/E: Potentially overvalued

### Coefficient of Variation
Risk per unit of return. Lower is better.

### Dividend Yield (%)
Annual dividend payment as percentage of stock price

## Recommendation Algorithm

The AI recommendation system scores companies based on:

1. **Sharpe Ratio** (Risk-Adjusted Returns)
   - Score +3: Sharpe > 0.5
   - Score +1: Sharpe > 0 and ≤ 0.5
   - Score -2: Sharpe ≤ 0

2. **Annual Return**
   - Score +3: Return > 25%
   - Score +2: Return 15-25%
   - Score +1: Return 10-15%
   - Score -1: Return < 10%

3. **Volatility** (Risk)
   - Score +2: Volatility < 20%
   - Score +1: Volatility 20-30%
   - Score -1: Volatility > 30%

4. **P/E Ratio** (Valuation)
   - Score +1: P/E < 20 (undervalued)
   - Score -1: P/E > 50 (overvalued)

5. **Dividend Yield**
   - Score +1: Yield > 2%

**Final Scoring**:
- Score ≥ 6: **STRONG BUY**
- Score 4-5: **BUY**
- Score 2-3: **HOLD**
- Score 0-1: **WEAK HOLD**
- Score < 0: **SELL/AVOID**

## API Endpoints

### 1. Get All Companies
```
GET /api/companies
Response: { status, companies: [...], total }
```

### 2. Analyze Company
```
GET /api/analyze/<company_name>
Response: { status, company, metrics, recommendation }
```

### 3. Compare Companies
```
POST /api/compare
Body: { companies: ["Company1", "Company2", ...] }
Response: { status, comparison: [...], total }
```

### 4. Health Check
```
GET /api/health
Response: { status, message }
```

## Adding New Companies

To add new companies to the analysis:

1. Open `data/companies_data.csv`
2. Add a new row with the following columns:
   - company_name
   - annual_return (%)
   - volatility (%)
   - mean_return
   - std_deviation
   - beta
   - current_price ($)
   - pe_ratio
   - dividend_yield (%)

Example:
```
Tesla,45.0,38.2,0.450,0.382,1.6,250.00,60.0,0.0
```

3. Restart the backend server

## Troubleshooting

### Error: "Failed to connect to server"
- Ensure the Flask backend is running on port 5000
- Check firewall settings
- Verify `http://localhost:5000/api/health` returns success

### Error: "Company not found"
- Check company name spelling
- Use exact names from the available companies list
- Company names are case-insensitive

### CORS Errors
- The backend includes CORS headers for frontend communication
- Ensure Flask-CORS is properly installed

## Future Enhancements

- Real-time stock data integration (Alpha Vantage, Yahoo Finance)
- Historical price charts
- Portfolio optimization
- Risk-free rate and market data customization
- User authentication and saved portfolios
- Machine learning-based predictions
- Mobile app version
- Export analysis to PDF

## Dependencies

- Flask 3.0.0
- Flask-CORS 4.0.0
- pandas 2.0.0
- numpy 1.24.0

## License

This project is free to use and modify for educational purposes.

## Support

For issues or questions:
1. Check that both backend and frontend are running
2. Verify company names are correct
3. Check console for detailed error messages
4. Ensure all dependencies are installed

---

**Created**: February 2026
**Version**: 1.0
