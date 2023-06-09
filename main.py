import psycopg2
from config import config
from imports import importRegions, importCompetitions, importParticipants
from exports import generator
from model import regions_translator, competitions_translator, participants_translator

""" Import CSV files """
# regions = importRegions("data/regions.csv")

# soccerCompetitions = importCompetitions("data/competitions_soccer.csv")
# basketballCompetitions = importCompetitions("data/competitions_basketball.csv")
# tennisCompetitions = importCompetitions("data/competitions_tennis.csv")

# soccerParticipants = importParticipants("data/participants_soccer.csv")
# basketballParticipants = importParticipants("data/participants_basketball.csv")
tennisParticipants = importParticipants("data/participants_tennis.csv")

""" Languages to translate to """
greek = "Greek"
persian = "Persian"

""" Translations """
# regionsGR = regions_translator(regions, greek)
# regionsPE = regions_translator(regions, persian)

# soccerCompetitionsGR = competitions_translator(soccerCompetitions, greek)
# soccerCompetitionsPE = competitions_translator(soccerCompetitions, persian)

# basketballCompetitionsGR = competitions_translator(basketballCompetitions, greek)
# basketballCompetitionsPE = competitions_translator(basketballCompetitions, persian)

# tennisCompetitionsGR = competitions_translator(tennisCompetitions, greek)
# tennisCompetitionsPE = competitions_translator(tennisCompetitions, persian)

# soccerParticipantsGR = participants_translator(soccerParticipants, greek)
# soccerParticipantsPE = participants_translator(soccerParticipants, persian)

# basketballParticipantsGR = participants_translator(basketballParticipants, greek)
# basketballParticipantsPE = participants_translator(basketballParticipants, persian)

tennisParticipantsGR = participants_translator(tennisParticipants, greek)
tennisParticipantsPE = participants_translator(tennisParticipants, persian)

""" New CSV files """
# generator(regions, regionsGR, regionsPE, 'data/regions_translated.csv')

# generator(soccerCompetitions, soccerCompetitionsGR, soccerCompetitionsPE, 'data/competitions_soccer_translated.csv')

# generator(basketballCompetitions, basketballCompetitionsGR, basketballCompetitionsPE, 'data/competitions_basketball_translated.csv')

# generator(tennisCompetitions, tennisCompetitionsGR, tennisCompetitionsPE, 'data/competitions_tennis_translated.csv')

# generator(soccerParticipants, soccerParticipantsGR, soccerParticipantsPE, 'data/participants_soccer_translated.csv')

# generator(basketballParticipants, basketballParticipantsGR, basketballParticipantsPE, 'data/participants_basketball_translated.csv')

generator(tennisParticipants, tennisParticipantsGR, tennisParticipantsPE, 'data/participants_tennis_translated.csv')