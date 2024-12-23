## Company Data

# Apple Data
a_mcap = 896473
a_pref = 0
a_ltdebt = 97128
a_cltdebt = 17472
a_mint = 0
a_cash = 70970
a_q3_17 = 17067
a_q4_17 = 30509
a_q1_18 = 19699
a_q2_18 = 16795

# Microsoft Data
m_mcap = 757029
m_pref = 0
m_ltdebt = 72242
m_cltdebt = 3998
m_mint = 0
m_cash = 133768
m_q3_17 = 11155
m_q4_17 = 12403
m_q1_18 = 12042
m_q2_18 = 13868


## Enterprise Value Calculation

a_ev = a_mcap \
         + a_pref \
         + a_ltdebt \
         + a_cltdebt \
         + a_mint \
         - a_cash

m_ev = m_mcap \
         + m_pref \
         + m_ltdebt \
         + m_cltdebt \
         + m_mint \
         - m_cash


## EBITDA Calculation

a_ltm_ebitda = a_q3_17 \
              + a_q4_17 \
              + a_q1_18 \
              + a_q2_18

m_ltm_ebitda = m_q3_17 \
              + m_q4_17 \
              + m_q1_18 \
              + m_q2_18


## Enterprise Multiple / EV-to-EBITDA Multiple Calculation

a_em = a_ev / a_ltm_ebitda
m_em = m_ev / m_ltm_ebitda


## Output

print( "AAPL EV = {}".format(a_ev))
print ( "AAPL LTM EBITDA = {}".format(a_ltm_ebitda))
print ( "AAPL EV / EBITDA = {}".format(round(a_em, ndigits=2)))
print ( "-" )
print( "MSFT EV = {}".format(m_ev))
print ( "MSFT LTM EBITDA = {}".format(m_ltm_ebitda))
print ( "MSFT EV / EBITDA = {}".format(round(m_em, ndigits=2)))
print ( "-" )
print ("AAPL's ratio is greater than MSFT's: {}".format( a_em > m_em ))