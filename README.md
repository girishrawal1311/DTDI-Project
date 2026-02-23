# 📊 DTDI Project - Stock Investment Advisor

A full-stack web application for analyzing and comparing stock investments with professional financial metrics and AI-powered recommendations.

**Live Demo**: https://dtdi-stock-advisor.herokuapp.com (Deploy here)

## ✨ Features

✅ **Company Analysis** - Analyze 30 stocks with comprehensive financial metrics
✅ **30 Companies** - Mix of global leaders (US) & Indian market stocks
✅ **Smart Recommendations** - STRONG BUY/BUY/HOLD/WEAK HOLD/SELL/AVOID based on Sharpe ratio & fundamentals
✅ **Risk & Return Metrics** - Annual return, volatility, Sharpe ratio, P/E ratio, Beta, dividend yield
✅ **Company Comparison** - Compare up to 5 companies side-by-side
✅ **Beautiful UI** - Modern, responsive interface with smooth animations
✅ **Real-time Analysis** - Instant calculations using professional financial formulas

## 📋 Companies Included

**US Companies (20):** Apple, Microsoft, Google, Amazon, Tesla, Meta, NVIDIA, JPMorgan, Berkshire Hathaway, Johnson & Johnson, Coca-Cola, Walmart, Visa, Mastercard, Adobe, Intel, AMD, Netflix, IBM, Oracle

**Indian Companies (10):** Reliance Industries, TCS, HDFC Bank, Infosys, State Bank of India, Hindustan Unilever, ITC Limited, Axis Bank, Bajaj Auto, Larsen & Toubro

## 🏗️ Tech Stack

- **Backend**: Python Flask 3.0.0, Pandas, NumPy
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Data**: CSV-based financial metrics
- **API**: RESTful with CORS support

## 🚀 Quick Start (Local)

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/DTDI-Project.git
cd DTDI-Project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start Backend (Terminal 1)
```bash
python backend/app.py
```
Runs on `http://localhost:5000`

### 4. Start Frontend (Terminal 2)
```bash
cd frontend
python -m http.server 8000
```
Open `http://localhost:8000` in browser

## 🌐 Deploy Online

### Option 1: Railway.app (Easiest - Free Tier Available)

1. **Push to GitHub** (see below)
2. Go to https://railway.app
3. Login with GitHub
4. Click "New Project" → "Deploy from GitHub repo"
5. Select DTDI-Project repository
6. Add `FLASK_ENV=production` as environment variable
7. Deploy! Railway will auto-detect your Python app

### Option 2: Render.com (Free Tier)

1. **Push to GitHub**
2. Go to https://render.com
3. Click "New+" → Web Service
4. Connect GitHub repo
5. Set Build command: `pip install -r requirements.txt`
6. Set Start command: `python backend/app.py`
7. Create `Procfile` in root:
```
web: gunicorn backend.app:app
```
8. Add to requirements.txt: `gunicorn==21.2.0`
9. Deploy!

### Option 3: Heroku (Paid - but works well)

1. **Push to GitHub**
2. Create `Procfile`:
```
web: gunicorn backend.app:app
```
3. Add to requirements.txt: `gunicorn==21.2.0`
4. Git push and Heroku auto-deploys

## 📤 Push to GitHub

```bash
cd "c:\Users\giris\OneDrive\Desktop\DTDI Project"
git remote add origin https://github.com/YOUR_USERNAME/DTDI-Project.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## 📁 Project Structure

```
DTDI-Project/
├── backend/
│   └── app.py              # Flask API
├── frontend/
│   └── index.html          # Web UI
├── data/
│   └── companies_data.csv  # 30 Companies
├── requirements.txt        # Dependencies
├── Procfile                # Deployment config
├── .gitignore              # Git ignore
└── README.md               # This file
```

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
