from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import os
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the financial data
data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'companies_data.csv')
df = pd.read_csv(data_file)

# Create a dictionary for quick lookup
companies_dict = {}
for _, row in df.iterrows():
    companies_dict[row['company_name'].lower()] = row.to_dict()

# Calculate Sharpe ratio and other metrics
RISK_FREE_RATE = 0.045  # 4.5% risk-free rate

def calculate_metrics(company_data):
    """Calculate all necessary metrics for analysis"""
    annual_return = company_data['annual_return'] / 100
    volatility = company_data['volatility'] / 100
    
    # Sharpe Ratio = (Return - Risk-Free Rate) / Volatility
    sharpe_ratio = (annual_return - RISK_FREE_RATE) / volatility if volatility > 0 else 0
    
    # Coefficient of Variation = Volatility / Return (Risk per unit of return)
    coeff_variation = volatility / annual_return if annual_return > 0 else 0
    
    return {
        'annual_return': company_data['annual_return'],
        'volatility': company_data['volatility'],
        'sharpe_ratio': round(sharpe_ratio, 4),
        'coefficient_of_variation': round(coeff_variation, 4),
        'beta': company_data['beta'],
        'pe_ratio': company_data['pe_ratio'],
        'dividend_yield': company_data['dividend_yield'],
        'current_price': company_data['current_price']
    }

def generate_recommendation(company_data, metrics):
    """Generate investment recommendation based on analysis"""
    score = 0
    reasons = []
    
    annual_return = metrics['annual_return']
    volatility = metrics['volatility']
    sharpe_ratio = metrics['sharpe_ratio']
    pe_ratio = metrics['pe_ratio']
    
    # Score based on Sharpe Ratio (higher is better)
    if sharpe_ratio > 0.5:
        score += 3
        reasons.append("Good risk-adjusted returns (Sharpe Ratio > 0.5)")
    elif sharpe_ratio > 0:
        score += 1
        reasons.append("Moderate risk-adjusted returns")
    else:
        score -= 2
        reasons.append("Poor risk-adjusted returns")
    
    # Score based on Return
    if annual_return > 25:
        score += 3
        reasons.append("Strong annual returns (> 25%)")
    elif annual_return > 15:
        score += 2
        reasons.append("Good annual returns (15-25%)")
    elif annual_return > 10:
        score += 1
        reasons.append("Moderate annual returns (10-15%)")
    else:
        score -= 1
        reasons.append("Low annual returns (< 10%)")
    
    # Score based on Volatility (lower is better)
    if volatility < 20:
        score += 2
        reasons.append("Low volatility (< 20%) - Stable investment")
    elif volatility < 30:
        score += 1
        reasons.append("Moderate volatility (20-30%)")
    else:
        score -= 1
        reasons.append("High volatility (> 30%) - Higher risk")
    
    # Score based on P/E Ratio
    if pe_ratio < 20:
        score += 1
        reasons.append("Favorable P/E ratio (< 20) - Potentially undervalued")
    elif pe_ratio > 50:
        score -= 1
        reasons.append("High P/E ratio (> 50) - Potentially overvalued")
    
    # Score based on Dividend Yield
    if company_data['dividend_yield'] > 2:
        score += 1
        reasons.append(f"Good dividend yield ({company_data['dividend_yield']}%)")
    
    # Generate recommendation
    if score >= 6:
        recommendation = "STRONG BUY"
        description = "Excellent risk-return profile with strong fundamentals."
    elif score >= 4:
        recommendation = "BUY"
        description = "Good investment opportunity with favorable metrics."
    elif score >= 2:
        recommendation = "HOLD"
        description = "Moderate investment with mixed signals. Requires careful monitoring."
    elif score >= 0:
        recommendation = "WEAK HOLD"
        description = "Weak fundamentals. Consider alternatives."
    else:
        recommendation = "SELL/AVOID"
        description = "Poor risk-return profile. Avoid this investment."
    
    return {
        'recommendation': recommendation,
        'description': description,
        'score': score,
        'reasons': reasons
    }

@app.route('/api/companies', methods=['GET'])
def get_all_companies():
    """Get list of all available companies"""
    company_names = df['company_name'].tolist()
    return jsonify({
        'status': 'success',
        'companies': company_names,
        'total': len(company_names)
    })

@app.route('/api/analyze/<company_name>', methods=['GET'])
def analyze_company(company_name):
    """Analyze a specific company"""
    company_key = company_name.lower()
    
    if company_key not in companies_dict:
        return jsonify({
            'status': 'error',
            'message': f'Company "{company_name}" not found. Available companies: {", ".join(df["company_name"].tolist())}'
        }), 404
    
    company_data = companies_dict[company_key]
    metrics = calculate_metrics(company_data)
    recommendation = generate_recommendation(company_data, metrics)
    
    return jsonify({
        'status': 'success',
        'company': company_data['company_name'],
        'metrics': metrics,
        'recommendation': recommendation
    })

@app.route('/api/compare', methods=['POST'])
def compare_companies():
    """Compare multiple companies"""
    data = request.json
    company_names = data.get('companies', [])
    
    if not company_names:
        return jsonify({
            'status': 'error',
            'message': 'No companies provided for comparison'
        }), 400
    
    results = []
    for company_name in company_names:
        company_key = company_name.lower()
        if company_key in companies_dict:
            company_data = companies_dict[company_key]
            metrics = calculate_metrics(company_data)
            results.append({
                'company': company_data['company_name'],
                'metrics': metrics
            })
    
    if not results:
        return jsonify({
            'status': 'error',
            'message': 'None of the provided companies were found'
        }), 404
    
    return jsonify({
        'status': 'success',
        'comparison': results,
        'total': len(results)
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'Risk and Return Analysis API is running'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
