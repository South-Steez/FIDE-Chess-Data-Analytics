🏆 FIDE Chess Data Analytics

📖 Overview
This project explores historical FIDE (World Chess Federation) player ratings using Python.
It performs data cleaning, transformation, and visualization to reveal rating trends for famous chess players such as Magnus Carlsen, Wesley So, Vladimir Kramnik, and Garry Kasparov.
The analysis highlights player performance over time, compares top competitors, and studies how ratings evolved across different years.

📊 Key Features
Import and clean real-world FIDE rating data from a CSV file
Filter and analyze player performance by name and date
Visualize FIDE rating progress using Seaborn and Matplotlib
Compare top players on a single chart
Compute average world rating vs. Magnus Carlsen’s performance
Explore data trends post-2007 excluding Carlsen

🧠 Concepts Covered
Data wrangling with Pandas
Data visualization with Seaborn and Matplotlib
Time series analysis and date handling
Comparative analytics

⚙️ Installation
1️⃣ Clone this repository
git clone https://github.com/South-Steez/FIDE-Chess-Data-Analytics.git
2️⃣ Navigate into the folder
cd FIDE-Chess-Data-Analytics
3️⃣ Install dependencies
Make sure you have Python 3.x installed, then run:
pip install pandas seaborn matplotlib numpy
▶️ How to Run the Script
Place the dataset file (e.g. fide_historical.csv) in the same directory as the script.
Run the Python file:
python fide_analysis.py

The program will:
Display dataset summaries
Plot rating progress for specific players
Show visual comparisons across multiple players

📈 Example Outputs
Line plots showing Magnus Carlsen’s rating rise
Comparisons between Carlsen vs. Kasparov
“Rest of the world” rating average vs. top player performance
Ratings of all players post-2007 (excluding Carlsen)

👨‍💻 Author
South-Steez
📍 Data analytics and visualization enthusiast

📜 License
This project is for educational and analytical purposes only.
You may modify and share it freely with credit to the author.
