############################
# Import Libraries
############################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

############################
# Page Start
############################

imaage = Image.open('DNA.png')

st.image(imaage, use_column_width=True)

st.write("""
# DNA Nucleotide Count APP

This app counts the nucleotide composition of DNA.

***
""")

st.header('Enter Sequence')

sequence_input = ">DNA Q 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence inpput", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (DNA Nucleotide Count)')

st.subheader('1. Print dictionary')

def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d

X = DNA_nucleotide_count(sequence)
X

st.subheader('2. Print text')
st.write('There are ' + str(X['A'])  + ' adenine (A)')
st.write('There are ' + str(X['T'])  + ' thumine (T)')
st.write('There are ' + str(X['G'])  + ' guanine (G)')
st.write('There are ' + str(X['C'])  + ' cytosine (C)')

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)


st.subheader('4. Display Bar Chart')

p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)

)
st.write(p)