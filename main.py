from Extract.Uber_Data_Analytics_Dashboard_Extract import uberExtractor



extractor = uberExtractor("qualifying_results.csv")



extractor.queries()



print(extractor.response())