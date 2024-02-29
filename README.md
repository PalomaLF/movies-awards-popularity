<img width="1044" alt="Captura de pantalla 2024-02-02 a las 19 14 57" src="https://github.com/PalomaLF/movies-awards-popularity/assets/156684365/38684ff5-36c4-4852-991a-39ecf61e2609">

# Awarded Movies Popularity Review

## Description

This study focuses on the rating provided to Oscars/Golden Globes winning movies by viewers through TMDB. The project has been created as part of Ironhack's Data Analytics Bootcamp

The data used in this study provides from:
- [Kaggle](https://www.kaggle.com/), for data regarding nominations and awards for the Oscars until 2023 and Golden Globers until 2020
- [Golden Globes website](https://goldenglobes.com/winners-nominees/) for Golden Globes nominations and winners for the years 2020-2023
- [The Movie Database (TMDb)](https://www.themoviedb.org/) free API for the scoring of each of the films in the study

In this hypothetical scenario, a global video on demand streaming platform is trying to optimize their IP purchase strategy as means to reduce their churn rate, which has been alarmingly increasing during the past 6 months. As awarded movies tend to have a higher acquisition fee for distribution, our goal is to determine whether our potential users apreciate the quality of these movies or not, and re-evaluate our strategy based on data.

The study focuses mainly on American movies and awards due to their international recognition.

## Step by step
All the code and process is available for review in this repository, in the "Notebooks" folder. Processed data after each cleaning step is avaliable in the "Data" folder.
All data has been cleaned and formated to follow Oscars denominations for films, and Golden Globes awards have been reduced to those focusing on films. Due to historical changes in the industry, the awards themselves have evolved over time, including different categories for black-and-white and color films in their early years. For this reason, the study focuses on the years 1967-2023

## Results

**Differences in nominee selection**
On average, only 26% of the films in this study have been nominated to both awards, showing a strong difference in the selection criteria. This difference persists on some specific categories, such as Best Picture (28%), althoug we can see an increase if we only select the main categories(40%). For this reason, the study has differentiated between Oscars and Golden Globes in the rating analysis.

**Rating Analysis**
Analysis shows a similar appreciation of awarded movies, with only 1.2% higher ratings in the case of Golden Globes for all slected films. However, this differnce increases if we focus on main categories, with an average of 2.4% higher ratings going for Oscar awarded movies. In general, ratings improve significantly when focusing on main categories, either nominees or award winners, which should be the focus moving forward.

As next steps, it would be interesting to continue the study the platfomr's own data, specially number of visualization, and extend the analysis to awards relevant outside the US.




