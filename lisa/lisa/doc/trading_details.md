# Lisa and cfd trading #

:Info: See <https://github.com/rockwolf/lisa> for the lisa code.  
:Author: Andy Nagels <no@email.given>  
:Date: $Date: 2013-02-26$  
:Revision: $Revision: 0001 $  
:Description: Extra documentation on cfd's for lisa.

## Notes ##

Table t_trade might need extra fields, this will be checked in detail in
this analysis.

## Margin ##

### Initial margin ###

Initial margin requires a margin percentage that can differ per cfd.
e.g.: For BE, it's usually 10%, but exceptions are possible.

### Maintenance margin ###

The maintenance margin is calculated on the realtime course.
It's not possible to keep this information in lisa.
The percentage is usually twice as high.

### Information ###

Though there are exceptions, it's still a good idea to keep that information
available. We can use it to make sure that our positions do not get
liquidated.
A good solution would be to look at the following page:
http://www.whselfinvest.com/nl/CFD_Market_Information_Sheets.php?sheet=1
and use these general values.

#### Margin info in database ####

We can conclude that we need to store these values from that link in the
database.
This gives us 3 things to implement:
- init script needs the values added in T_PARAMETER
- code needs to retrieve the correct value, based on market and country
- code needs to calculate the estimated maximum required margin:
  margin_estimated_max as both an absolute number and a percentage of the
  pool_at_start

#### T_TRADE ####

Add columns
margin_estimated_max
margin_estimated_max_percent

### Conclusion ###

We need to make sure that we have enough margin, but it's difficult to keep
how much exactly. Estimations will be built in.

## Overnight holding of cfd's  ##

### Overnight costs ###

When you hold a long cfd overnight, you get an additional cost:
    (overnight Libor + 3%)/360

Note: the 3% and 360% is a solid amount.

Problem: THe overnight Libor rate changes daily.
Solution: don't care about this too much, your total costs are commission +
tax, the difference will be the other costs.

### Information ###

Those other costs will have to be saved in the database?
Attention, when shorting, those costs will be negative!
TODO: check if the calculations

## Spread ##

### Important note ###

The spread is not a cost that goes off your account. It's an extra course
action you need to undergo in order to be profitable.

This can however affect the total cost!

### Conclusion ###

Add an extra field to t_trade and also t_investment with extra_costs, where
a potential difference is added. This should be 0 for all invades without
extra costs, but covers all extra expenses for trading and investing.

## Lisa structure for trading/investing ##

### Notes ###

General information regarding lisa and it's structure needs to be
documented, to ensure that the inner workings are well defined.

It's important tot know that as a trader, you can not make the calculations
too complex. Tax, commission, that should be known. Extra expenses are extra
costs.

## Currency ##

### Notes ###

All fields with currencies, should be in the currency from finance. If that
is USD, all will be in USD.
Next to all fields, a converted value will be added, which will be in the
base currency.

### Base currency ###

What is the base currency?
Add a field in T_PARAMETER that defines this.
It will be euro in this case.

## Interesting links ##

Margin per country/market, http://www.whselfinvest.com/nl/CFD_Market_Information_Sheets.php?sheet=1

Overnight libor rates, http://www.global-rates.com/interest-rates/libor/european-euro/eur-libor-interest-rate
