# 📊 Student Performance Analyzer

A comprehensive Streamlit application designed to analyze student academic performance across multiple subjects and generate detailed PDF reports with AI-powered recommendations.

## ✨ Features

- **CSV Data Upload**: Easy file upload interface for student performance data
- **Interactive Data Visualization**:
  - Overall performance bar chart for all students
  - Subject-specific performance trend lines
  - Dynamic chart selection for different subjects
- **Individual Student Analysis**: Select specific students for detailed review
- **AI-Powered Feedback**: Automated performance assessment and recommendations
- **PDF Report Generation**: Download comprehensive student reports
- **Multi-Subject Support**: Covers English, History, ICT, Math, and Science

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/student-performance-analyzer.git
cd student-performance-analyzer
```

2. Install the required dependencies:
```bash
pip install streamlit pandas fpdf2
```

### Running the Application

1. Navigate to the project directory
2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your web browser and go to `http://localhost:8501`

## 📁 CSV Data Format

Your CSV file should include the following columns:

| Column Name | Description | Data Type | Required |
|-------------|-------------|-----------|----------|
| Name        | Student name | String    | Yes      |
| Student ID  | Unique identifier | String/Number | Optional |
| English     | English score (0-100) | Number | Yes |
| History     | History score (0-100) | Number | Yes |
| ICT         | ICT score (0-100) | Number | Yes |
| Math        | Math score (0-100) | Number | Yes |
| Science     | Science score (0-100) | Number | Yes |

### Sample CSV Data
```csv
Name,Student ID,English,History,ICT,Math,Science
John Smith,S001,85,78,92,76,88
Jane Doe,S002,92,85,78,94,90
Mike Johnson,S003,67,72,85,68,75
Sarah Wilson,S004,78,88,76,82,79
```

## 📱 Usage

### 1. Upload Data
- Click "📂 Upload a CSV file"
- Select your CSV file containing student performance data
- View the uploaded data in the interactive table

### 2. Analyze Overall Performance
- View the overall bar chart showing all students' performance across subjects
- Compare students visually across different subjects

### 3. Subject-Specific Analysis
- Select from 5 subjects: English, History, ICT, Math, Science
- View trend lines for the selected subject
- Analyze performance patterns across students

### 4. Generate Individual Reports
- Select a specific student from the dropdown
- View AI-generated performance feedback
- Download a comprehensive PDF report

## 🤖 AI Feedback System

The application provides automated feedback based on score ranges:

- **80-100**: "Excellent in [Subject]"
- **50-79**: "Average in [Subject], could improve"
- **0-49**: "Needs improvement in [Subject]"

## 📄 PDF Report Features

Each generated PDF report includes:
- Student name and ID
- Complete score breakdown for all subjects
- AI-generated recommendations
- Professional formatting
- Downloadable format for record-keeping

## 🛠️ Technical Details

- **Framework**: Streamlit
- **Data Processing**: Pandas
- **PDF Generation**: FPDF2
- **File Handling**: Python tempfile
- **Visualization**: Streamlit's built-in charting

## 📊 Supported Visualizations

1. **Overall Bar Chart**: Comparative view of all students across subjects
2. **Subject Line Charts**: Individual subject performance trends
3. **Interactive Selection**: Dynamic chart updates based on user selection

## 🔧 File Structure

```
student-performance-analyzer/
│
├── app.py              # Main Streamlit application
├── README.md          # This file
├── requirements.txt   # Python dependencies
├── sample_data.csv    # Sample CSV file (optional)
└── reports/           # Generated PDF reports (auto-created)
```
## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 Future Enhancements

- [ ] Add grade calculation (A, B, C, D, F)
- [ ] Implement class average comparisons
- [ ] Add more sophisticated AI recommendations
- [ ] Include trend analysis over time
- [ ] Support for custom subject additions
- [ ] Batch PDF report generation
- [ ] Data export to Excel format
- [ ] Student ranking system
- [ ] Performance prediction models
- [ ] Integration with school management systems

## 📋 Requirements

Create a `requirements.txt` file with:
```
streamlit>=1.28.0
pandas>=2.0.0
fpdf2>=2.7.0
```

## ⚠️ Important Notes

- Ensure CSV files follow the exact column naming convention
- Scores should be numeric values between 0-100
- PDF reports are temporarily stored and automatically cleaned up
- Application supports unlimited number of students

## 🎯 Use Cases

- **Teachers**: Analyze class performance and generate student reports
- **Schools**: Track academic progress across subjects
- **Parents**: Understand child's academic standing
- **Students**: Self-assessment and progress tracking
- **Educational Consultants**: Performance analysis and recommendations

## 📞 Support

If you encounter any issues or have questions:
1. Check the sample CSV format
2. Ensure all required columns are present
3. Verify numeric data types for scores
4. Create an issue in the GitHub repository

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Built with ❤️ using Streamlit | Perfect for educators and academic institutions
