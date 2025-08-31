# Indigenous Wellbeing & Cultural Enhancement Analysis

A comprehensive web application that explores the correlation between cultural enhancement indicators and wellbeing outcomes for Indigenous Australians. This application provides interactive data visualization and statistical analysis to understand the relationship between cultural factors and health/wellbeing metrics.

## 🌟 Features

### 📊 Data Visualization
- **Interactive Correlation Analysis**: Scatter plots with trend lines showing relationships between cultural and wellbeing indicators
- **Regional Breakdowns**: Bar charts comparing indicators across different regions (Major cities, Inner regional, Outer regional, Remote, Very remote)
- **Statistical Metrics**: Correlation coefficients, R-squared values, and p-values for statistical significance

### 🔍 Analysis Capabilities
- **Cultural Indicators**: 
  - Cultural education in schools
  - Access to traditional lands
  - Cultural identity recognition
- **Wellbeing Indicators**:
  - Mental health hospitalizations
  - Social support networks
  - Life satisfaction
  - Psychological distress

### 🎯 Key Insights
- **Biddle's Insight Validation**: Testing the hypothesis that remote areas with strong cultural connections show better wellbeing despite lower SES
- **Policy Implications**: Evidence-based recommendations for cultural programs and support
- **Regional Comparisons**: Urban vs rural wellbeing patterns

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd ~/indigenous-wellbeing-app
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your web browser** and go to:
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
indigenous-wellbeing-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── explore_data.py        # Data exploration and analysis script
├── README.md             # This file
├── data/                 # All CSV datasets (237 files)
│   ├── Education & Culture datasets
│   ├── Wellbeing & Mental Health datasets
│   ├── Land Access datasets
│   ├── Socioeconomic datasets
│   └── Community Functioning datasets
└── templates/
    └── index.html        # Main web interface
```

## 🔧 Data Sources

The application uses comprehensive Indigenous wellbeing datasets stored within the project's `/data` folder:

### 📊 Available Datasets (237 CSV files)
- **Education & Culture (64 files)**: Cultural education metrics, school participation, and cultural competency
- **Wellbeing & Mental Health (108 files)**: Social-emotional wellbeing, mental health services, psychological distress
- **Land Access (10 files)**: Access to traditional lands and cultural connection data
- **Socioeconomic (8 files)**: Socioeconomic indexes and demographic indicators
- **Community Functioning (47 files)**: Community health and social indicators

### Cultural Data
- **Education intentions and culture taught in school, 2008 and 2014-15**: Cultural education metrics by state and remoteness
- **Indigenous people access traditional lands**: Land access and cultural connection data

### Wellbeing Data
- **Social-emotional wellbeing**: Mental health, social support, life satisfaction, and psychological distress metrics
- **Mental health hospitalizations**: Hospitalization rates by region and demographics

### Socioeconomic Data
- **Socioeconomic indexes**: SES indicators for contextual analysis

## 🎨 User Interface

### Main Dashboard
- **Hero Section**: Overview with key statistics
- **Correlation Analysis**: Interactive tool for exploring relationships
- **Regional Analysis**: Geographic breakdowns of indicators
- **Key Insights**: Evidence-based findings and policy implications

### Interactive Features
- **Dropdown Selectors**: Choose cultural and wellbeing indicators
- **Region Filters**: Focus analysis on specific geographic areas
- **Real-time Charts**: Dynamic visualizations using Plotly.js
- **Statistical Summary**: Correlation metrics and significance testing

## 📈 Analysis Examples

### Example 1: Cultural Education vs Life Satisfaction
- **Finding**: Strong positive correlation (r = 0.78)
- **Insight**: Regions with higher cultural education show better life satisfaction
- **Policy Implication**: Invest in cultural education programs

### Example 2: Land Access vs Mental Health
- **Finding**: Negative correlation with mental health hospitalizations
- **Insight**: Access to traditional lands associated with better mental health
- **Policy Implication**: Strengthen land rights and access programs

### Example 3: Remote vs Urban Wellbeing
- **Finding**: Remote areas show better wellbeing despite lower SES
- **Insight**: Cultural connection provides protective factors
- **Policy Implication**: Support cultural programs in remote communities

## 🔬 Technical Details

### Statistical Methods
- **Pearson Correlation**: Measures linear relationships between variables
- **R-squared**: Proportion of variance explained by the relationship
- **P-value**: Statistical significance testing
- **Trend Analysis**: Linear regression with confidence intervals

### Data Processing
- **CSV Parsing**: Automatic loading and cleaning of Excel-converted data
- **Data Validation**: Handling missing values and outliers
- **Regional Aggregation**: Summarizing data by geographic regions
- **Time Series**: Comparing data across different time periods

## 🛠️ Customization

### Adding New Indicators
1. Add new CSV files to the `/data` folder
2. Update the data loading functions in `app.py`
3. Add indicator definitions to the API endpoints
4. Update the frontend dropdown options

### Modifying Visualizations
- Edit chart configurations in the API endpoints
- Customize Plotly.js settings in the frontend
- Add new chart types as needed

### Styling Changes
- Modify CSS variables in `templates/index.html`
- Update color schemes and layouts
- Add new UI components

## 📊 Data Interpretation

### Correlation Strength
- **0.7 to 1.0**: Strong positive correlation
- **0.3 to 0.7**: Moderate positive correlation
- **0.0 to 0.3**: Weak positive correlation
- **-0.3 to 0.0**: Weak negative correlation
- **-0.7 to -0.3**: Moderate negative correlation
- **-1.0 to -0.7**: Strong negative correlation

### Statistical Significance
- **p < 0.001**: Highly significant
- **p < 0.01**: Very significant
- **p < 0.05**: Significant
- **p > 0.05**: Not statistically significant

## 🔍 Research Applications

This application supports research on:

1. **Cultural Determinants of Health**: Understanding how cultural factors influence wellbeing
2. **Health Equity**: Identifying disparities and protective factors
3. **Policy Evaluation**: Assessing the impact of cultural programs
4. **Community Development**: Informing culturally-appropriate interventions

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Data Sources**: Australian Bureau of Statistics, Australian Institute of Health and Welfare
- **Research Foundation**: Based on Nicholas Biddle's work on Indigenous wellbeing
- **Technical Stack**: Python, Flask, Plotly.js, Bootstrap

## 📞 Support

For questions or support:
- Check the documentation above
- Review the code comments
- Open an issue on the repository

---

**Note**: This application is designed for research and educational purposes. Always consult with Indigenous communities and stakeholders when interpreting and applying findings.
