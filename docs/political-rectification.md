# Political Rectification

Political rectification refers to the process of adjusting the political
entities in the raw data to match the actual political entities in existence
over time.

Political rectification is made up of two stages. Data-source-wise political
rectification and inter-source political matching. The former manages the
merges and splits of political entities over time within the data from one
source and the latter matches the rectified entities from different data
sources.

## Rectification types and examples

Some different types and examples of political rectification from the Marchand
paper.

1. Name change: Ethiopia was renamed the Peoples Democratic Republic of
   Ethiopia from 1987 to 1991. So for the years 1986 to 1991 all trade to
   either entity was merged.

   In a name change rectification, a political entity simply changes its name
   and the rectifier keeps track of that fact.

   The names of the political entity prior to and after the name change must be
   given along with the year that the name change takes effect.

2. Simple merge: Ethiopia was renamed the Peoples Democratic Republic of
   Ethiopia from 1987 to 1991. So for the years 1986 to 1991 all trade to
   either entity was merged.

   For a simple merge, the time period must be specified. By default this is
   all years. The merging entities in the data source must be specified.

   If the time period is given, and the model years includes years outside of
   the time period, then a before political entity or an after political entity
   or both must be given so that the rectified entity can be matched with its
   predecessor and/or successor.

3. Simple split: In 1993 Eritrea emerged as a political node distinct from
   Ethiopia. Trade attributed to Eritrea prior to 1993 should be merged with
   Ethiopia.

   The parent political entity needs to be identified, as well as 
