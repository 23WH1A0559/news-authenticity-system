# News-Authenticity-Detection-System
📘 SOFTWARE REQUIREMENTS SPECIFICATION (SRS)
News Authenticity Detection System (Semi-Supervised Learning Based)
________________________________________
# 1. Introduction
# 1.1 Purpose
The purpose of this document is to describe the functional and non-functional requirements of the News Authenticity Detection System.
This system detects whether a news article is Real or Fake using a Semi-Supervised Machine Learning approach and provides analytical insights about news trends, prediction confidence, and model behavior.
Unlike traditional supervised systems, this application improves over time by learning from unlabeled real-world news data.
This document is intended for:
•	Project evaluators and faculty
•	Developers and testers
•	End users
________________________________________
# 1.2 Scope
The News Authenticity Detection System is a web-based application that:
•	Accepts news text as input
•	Predicts authenticity (Real/Fake)
•	Displays prediction confidence score
•	Learns from new unlabeled news articles
•	Provides interactive analytics dashboards
The system combines:
•	Natural Language Processing (NLP)
•	Semi-Supervised Learning
•	Data Analytics
•	Web-based deployment
The application is designed for educational, research, and real-world experimentation purposes.

________________________________________
# 1.3 Definitions, Acronyms, Abbreviations
•	ML – Machine Learning
•	NLP – Natural Language Processing
•	SSL – Semi-Supervised Learning
•	SRS – Software Requirements Specification
•	UI – User Interface
•	TF-IDF – Term Frequency–Inverse Document Frequency
•	API – Application Programming Interface
________________________________________
# 1.4 References
•	Kaggle Fake News Dataset
•	Scikit-learn Documentation
•	Pandas Documentation
•	FastAPI Documentation
________________________________________
# 2. Overall Description
2.1 Product Perspective
The system follows a modular architecture:
Dataset
→ Text Preprocessing
→ Semi-Supervised Model Training
→ Model Storage
→ Backend API
→ Frontend UI
→ Data Analytics Dashboard
→ Continuous Learning Module
The system is designed to simulate a real-world intelligent verification platform.
________________________________________
# 2.2 Product Functions
The system performs the following functions:
•	Accept news article text input
•	Preprocess text using NLP techniques
•	Predict authenticity using Semi-Supervised Learning
•	Display prediction result and confidence score
•	Store predictions for analytics
•	Continuously learn from high-confidence predictions
•	Provide visual data analytics dashboards
•	Allow admin monitoring of system performance
________________________________________
# 2.3 User Classes and Characteristics
User Type	Description
End User	Inputs news and views prediction results
Admin	Monitors analytics and system performance
Evaluator	Reviews system functionality
________________________________________
# 2.4 Operating Environment
•	Operating System: Windows / Linux
•	Backend: Python
•	ML Libraries: Scikit-learn, NumPy, Pandas
•	Frontend: HTML, CSS, JavaScript / React
•	Backend Framework: FastAPI or Flask
•	Database: MongoDB / SQLite
________________________________________
# 2.5 Design and Implementation Constraints
•	Availability of quality dataset
•	Model performance depends on data distribution
•	Requires periodic retraining
•	Internet required for optional API integration
________________________________________
# 3. System Features (Functional Requirements)
________________________________________
# 3.1 News Authenticity Prediction
Description:
Users enter a news article and receive a prediction.
Inputs:
•	News article text
Outputs:
•	Prediction label (Real / Fake)
•	Confidence score
•	Timestamp
________________________________________
# 3.2 Text Preprocessing Module
The system performs:
•	Lowercasing
•	Stopword removal
•	Tokenization
•	Special character removal
•	Vectorization using TF-IDF
Purpose:
Converts raw text into machine-readable format.
________________________________________
# 3.3 Semi-Supervised Learning Module (Core Feature)
Description:
The system uses a Semi-Supervised Learning approach instead of traditional supervised learning.
Algorithm Used:
Self-Training Classifier with Linear Support Vector Machine as base estimator.
Workflow:
1.	Train on small labeled dataset
2.	Use unlabeled news data
3.	Generate pseudo-labels for high-confidence predictions
4.	Retrain model using newly labeled data
5.	Deploy improved model
Benefits:
•	Learns from limited labeled data
•	Adapts to new patterns of fake news
•	Reduces manual labeling effort
•	More realistic real-world behavior
________________________________________
# 3.4 Continuous Learning Module (Unique Feature)
Description:
The system continuously improves by:
•	Storing user-submitted news
•	Identifying high-confidence predictions
•	Adding them to pseudo-labeled dataset
•	Periodically retraining the model
This simulates “learning from experience.”
________________________________________
# 3.5 Data Analytics Module
Description:
Provides analytical insights derived from dataset and user predictions.
Analytics Features:
•	Fake vs Real distribution
•	Category-wise analysis
•	Word frequency analysis
•	Confidence score distribution
•	Prediction trends over time
•	Model performance metrics
•	Confusion matrix visualization
Purpose:
•	Improves transparency
•	Helps understand dataset bias
•	Enhances decision-support capability
________________________________________
# 3.6 Dashboard Visualization
Interactive charts include:
•	Bar charts
•	Pie charts
•	Line graphs
•	Confusion matrix
Used for visual interpretation of system behavior.
________________________________________
# 4. External Interface Requirements
________________________________________
# 4.1 User Interface
•	Text input area
•	Submit button
•	Prediction result display
•	Confidence score display
•	Analytics dashboard page
________________________________________
# 4.2 Software Interfaces
•	Model stored as .pkl file
•	Backend API for prediction
•	Database for storing logs
•	Optional integration with fact-check APIs
________________________________________
# 5. Non-Functional Requirements
________________________________________
5.1 Performance Requirements
•	Prediction response time < 3 seconds
•	Supports multiple users
________________________________________
5.2 Accuracy Requirements
•	Target accuracy ≥ 90%
•	Improved performance after each retraining cycle
________________________________________
5.3 Security Requirements
•	Input validation
•	Secure API endpoints
•	Protection against injection attacks
________________________________________
5.4 Usability Requirements
•	Simple interface
•	Clear prediction display
•	Easy navigation
________________________________________
5.5 Scalability
•	Can integrate advanced models (e.g., BERT)
•	Can expand dataset
•	Can integrate real-time news APIs
________________________________________
# 6. System Architecture
High-Level Architecture:
User Interface
↓
Backend API (FastAPI/Flask)
↓
Semi-Supervised Learning Engine
↓
Prediction + Analytics Engine
↓
Database
↓
Continuous Learning Module
________________________________________
# 7. Future Enhancements
•	Integration with live news APIs
•	Deep learning models such as BERT
•	Multilingual fake news detection
•	Real-time streaming analysis
•	Hybrid ML + fact-check API verification
________________________________________
# 8. Conclusion
The News Authenticity Detection System combines Semi-Supervised Learning and Data Analytics to provide adaptive and intelligent news verification.
Unlike traditional supervised systems, this application improves over time by learning from unlabeled news articles, making it closer to real-world intelligent AI systems.
The inclusion of analytics enhances transparency, interpretability, and decision-making capability, making the system suitable for both academic and practical applications.


