import psycopg2
from config import config
from imports import importRegions, importCompetitions, importParticipants
from exports import merger
from model import engine

# import data from csv files and create dataframes
regions = importRegions("data/regions.csv")
print(regions)

# soccerCompetitions = importCompetitions("data/competitions_soccer.csv")
# basketballCompetitions = importCompetitions("data/competitions_basketball.csv")
# tennisCompetitions = importCompetitions("data/competitions_tennis.csv")

# soccerParticipants = importParticipants("data/participants_soccer.csv")
# basketballParticipants = importParticipants("data/participants_basketball.csv")
# tennisParticipants = importParticipants("data/participants_tennis.csv")

# translate data and update the dataframes to include translations
greek = "Greek"
persian = "Persian"

""" Translations """
regionsGR = engine(regions, greek)
print(regionsGR)
# regionsPE = engine(regions, persian)

# soccerCompetitionsGR = engine(soccerCompetitions, greek)
# soccerCompetitionsPE = engine(soccerCompetitions, persian)

# basketballCompetitionsGR = engine(basketballCompetitions, greek)
# basketballCompetitionsPE = engine(basketballCompetitions, persian)

# tennisCompetitionsGR = engine(tennisCompetitions, greek)
# tennisCompetitionsPE = engine(tennisCompetitions, persian)

# soccerParticipantsGR = engine(soccerParticipants, greek)
# soccerParticipantsPE = engine(soccerParticipants, persian)

# basketballParticipantsGR = engine(basketballParticipants, greek)
# basketballParticipantsPE = engine(basketballParticipants, persian)

# tennisParticipantsGR = engine(tennisParticipants, greek)
# tennisParticipantsPE = engine(tennisParticipants, persian)

""" New CSV files """
merger(regions, regionsGR, 'data/regions_translated_GR.csv')