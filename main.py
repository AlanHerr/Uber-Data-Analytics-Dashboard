from Extract.Uber_Data_Analytics_Dashboard_Extract import uberExtractor



extractor = uberExtractor("ncr_ride_bookings.csv")



extractor.queries()



print(extractor.response())