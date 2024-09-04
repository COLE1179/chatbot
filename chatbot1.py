import streamlit as st
import difflib
def user_input(user_info):
    commands = ['how old is kobe bryant', 'how old is he', 'whats his age', 'how old', 'his age', 'how old',
                'whats his name', 'name', 'whats name', 'what does he go by',
                'what his is position', 'his position', 'where does he play',
                'what is kobe bryant full name', 'what his name', 'what is his name', 'please tell me his name', 'full name',
                'which league did he play in', 'league',
                'what is his nickname', 'what does he go by on the court', 'nickname',
                'how did he die', 'how he died', 'the cause of his death', 'death',
                'how many children does he has', 'how many children', 'number of children', 'children',
                'how many championship did he win', 'how many rings did he win', 'how many cups does he have',
                'how many followers does he have on instagram', 'how many people follow him on instagram', 'followers', 'how many active followers does he have',
                'job', 'what does he do', 'what does he do for a living', 'career',
                'date of birth', 'which year was he born',  'when was he born', 'birth',
                'which state was he born in', 'state', 'area he was born', 'where was he given birth to',
                'siblings', 'how many siblings does he has']
    close = difflib.get_close_matches(user_info.lower(), commands, n=1, cutoff=0.5)

    if close:
        close_matches = close[0]
    if close_matches in ['how old is kobe bryant', 'how old is he', 'whats his age', 'how old', 'his age', 'how old']:
        return "He is dead"
    elif close_matches in ['whats his name', 'name', 'whats name', 'what does he go by']:
        return "Kobe Bryant"
    elif close_matches in ['what his is position', 'his position', 'where does he play']:
        return " He is a Shooting Guard"
    elif close_matches in ['what is kobe bryant full name', 'what his name', 'what is his name', 'please tell me his name', 'full name']:
        return "Kobe Bean Bryant"
    elif close_matches in ['what is his nickname', 'what does he go by on the court', 'nickname']:
        return "Black Mamba"
    elif close_matches in ['which league did he play in', 'league']:
        return " National Basket-ball Association"
    elif close_matches in ['when did he die', 'when he died', 'he died when', ]:
        return " he died 2020"
    elif close_matches in ['which team does he play for', 'team']:
        return "Los Angeles Lakers"
    elif close_matches in ['how did he die', 'how he died', 'the cause of his death', 'death']:
        return " he died in a plane crash"
    elif close_matches in ['how many children does he has', 'how many children', 'number of children', 'children']:
        return "He has five children"
    elif close_matches in ['whats his wife name', 'whats his partner name', 'wife name', 'baby mama', 'wife']:
        return "Vanessa Bryant"
    elif close_matches in ['how many championship did he win', 'how many rings did he win', 'how many cups does he have']:
        return "He won five championship"
    elif close_matches in ['how many followers does he have on instagram', 'how many people follow him on instagram', 'followers', 'how many active followers does he have']:
        return "He has 21 million followers"
    elif close_matches in ['job', 'what does he do', 'what does he do for a living', 'career']:
        return "He is a basket-baller"
    elif close_matches in ['date of birth', 'which year was he born', 'when was he born', 'birth']:
        return "23 August 1978"
    elif close_matches in ['which state was he born in', 'state', 'area he was born', 'where was he given birth to']:
        return "Philadelphia, pennsylvania, United States"
    elif close_matches in ['siblings', 'how many siblings does he has']:
        return "He has two siblings which are sharia and shaya Bryant"
    else:
        return "Sorry the information is not available"


st.header('Kobe Bryant')
c = st.text_input('Cole: ')
st.sidebar.header('Questionnaire about Kobe Bryant')
st.sidebar.image('Kobe_Bryant.jpeg')

if c:
  response = user_input(c)
  st.write(f'chatbot:{response}')



