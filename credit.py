# -*- coding: utf-8 -*-
"""
-- ===============================================================================================
-- Description...:  Given credit card number and then by using Luhn’s Algorithm, 
                    print whether it is a valid American Express, MasterCard, or Visa card number.	
-- Input.........:  Credit Card Number, w-out hyphens.
-- Output........:  AMEX|MASTERCARD|VISA|INVALID      
--  
-- Rules.........:  AMEX.......: length: 15-digit; starts-with: {34, 37}
                    MASTERCARD.: length: 16-digit; starts-with: {51, 52, 53, 54, or 55}
                    VISA.......: length: 13-digit OR 16-digit; starts-with: 4
--
-- Arcenio Brito, 2020-06-20: start-time: 13:30 hrs; end-time: 16:00 hrs
-- ===============================================================================================
"""

import os
import sys
import math

DEBUG = False
AMEX = 'AMEX'
VISA = 'VISA'
INVALID = 'INVALID'
MASTERCARD = 'MASTERCARD'

def validate_luhns_algorithm (string_number) :
    string_number_rev = string_number[::-1]
    
    index1 = 1
    odd_number_list = []   #impar
    even_number_list = []  #par

    #!! [1: doubling even-numbers]
    for x in string_number_rev :
        number = int(x)
        if index1 % 2 == 0: 
            number = number * 2
            if number > 9:
                number_list = [int(t) for t in str(number)] 
                number = number_list[0] + number_list[1]
            even_number_list.append(number)
        else: 
            odd_number_list.append(number)
        index1 = index1 + 1
    #endfor

    #!! [2: sum of odd an even mumbers]
    luhns_list = odd_number_list + even_number_list
    sum_all = sum(luhns_list)

    #!! [3: checks modulus 10]
    result = (sum_all % 10 == 0)
    
    if DEBUG : print ('odd:{} even:{}'.format( odd_number_list[::-1], even_number_list[::-1]))
    if DEBUG : print ('sum:{} result:{}'.format(sum_all, result))

    return result 

def get_credit_card_type (string_number) :
    result = INVALID
    if validate_luhns_algorithm(string_number) :
        firstdigit = string_number[0]
        first2digit = string_number[0:2]
        length = len(string_number)
        
        if DEBUG : print ('firstdigit:{} first2digit:{} len:{}'.format(firstdigit, first2digit, length))
        if first2digit in ['34', '37'] and length == 15 : 
            result = AMEX
        elif first2digit in ['51', '52', '53', '54', '55'] and length == 16 : 
            result = MASTERCARD
        elif firstdigit in ['4'] and (length == 13 or length == 16) : 
            result = VISA
        else :
            result = INVALID
        #endif
    #endif
    return result

def validate_credit_card (string_number) :
    string_number = str(string_number)
    result = get_credit_card_type(string_number)
    print (result)
    return    


def execute_paypalpage_test() :
    lst1 = [378282246310005, 371449635398431, 378734493671000, 30569309025904, 6011111111111117]
    lst2 = [6011000990139424, 3530111333300000, 3566002020360505, 2221000000000009, 2223000048400011]
    lst3 = [2223016768739313, 5555555555554444, 5105105105105100, 4111111111111111, 4012888888881881, 4222222222222]
    lst_n = lst1 + lst2 + lst3 
    [validate_credit_card(t) for t in lst_n]
    return

########
### main
########
if __name__ == '__main__' :
    args = sys.argv
    if len(args) > 1 :
        for x in args[1:] :
            validate_credit_card(x)
    else :
        execute_paypalpage_test()
    #endif
    print("")
#endif

