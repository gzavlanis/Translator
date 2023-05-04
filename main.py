import psycopg2
from config import config
from imports import importRegions, importCompetitions, importParticipants
from exports import generator
from model import translator

""" Import CSV files """
# regions = importRegions("data/regions.csv")

# soccerCompetitions = importCompetitions("data/competitions_soccer.csv")
# basketballCompetitions = importCompetitions("data/competitions_basketball.csv")
tennisCompetitions = importCompetitions("data/competitions_tennis.csv")

# soccerParticipants = importParticipants("data/participants_soccer.csv")
# basketballParticipants = importParticipants("data/participants_basketball.csv")
# tennisParticipants = importParticipants("data/participants_tennis.csv")

""" Languages to translate to """
greek = "Greek"
persian = "Persian"

""" Translations """
# regionsGR = translator(regions, greek)
# regionsPE = translator(regions, persian)

# soccerCompetitionsGR = translator(soccerCompetitions, greek)
# soccerCompetitionsPE = translator(soccerCompetitions, persian)

# basketballCompetitionsGR = translator(basketballCompetitions, greek)
# basketballCompetitionsPE = translator(basketballCompetitions, persian)

tennisCompetitionsGR = translator(tennisCompetitions, greek)
tennisCompetitionsPE = translator(tennisCompetitions, persian)

# soccerParticipantsGR = engine(soccerParticipants, greek)
# soccerParticipantsPE = engine(soccerParticipants, persian)

# basketballParticipantsGR = engine(basketballParticipants, greek)
# basketballParticipantsPE = engine(basketballParticipants, persian)

# tennisParticipantsGR = engine(tennisParticipants, greek)
# tennisParticipantsPE = engine(tennisParticipants, persian)

""" New CSV files """
# generator(regions, regionsGR, regionsPE, 'data/regions_translated.csv')

# generator(soccerCompetitions, soccerCompetitionsGR, soccerCompetitionsPE, 'data/competitions_soccer_translated.csv')

# generator(basketballCompetitions, basketballCompetitionsGR, basketballCompetitionsPE, 'data/competitions_basketball_translated.csv')

generator(tennisCompetitions, tennisCompetitionsGR, tennisCompetitionsPE, 'data/competitions_tennis_translated.csv')

# generator(soccerParticipants, soccerParticipantsGR, soccerParticipantsPE, 'data/participants_soccer_translated.csv')

# generator(basketballParticipants, basketballParticipantsGR, basketballParticipantsPE, 'data/participants_basketball_translated.csv')

# generator(soccerParticipants, soccerParticipantsGR, soccerParticipantsPE, 'data/participants_soccer_translated.csv')