SpellbookRando

A randomiser for the Dominions 5 default spellbook, with various options:

Randomise primary paths: whether to affect spells' primary paths
Randomise secondary paths: whether to affect spells' secondary paths, but only for spells that normally have them
Randomise research schools: whether to shuffle research schools
Gems per slave: how many gems to adjust spell costs/fatigue by when converting to or from blood magic. Note that spells that originally cost a gem will always cost a gem regardless of this setting
Paired communions: the master and slave spells for communion/sabbath/chorus sets will always end up together in the same research school, and with the same path requirement
Skip communions: do not randomise communion/sabbath/chorus spells
Skip magic duel: do not randomise magic duel
Force blood in blood: All spells with a blood magic path requirement will end up in blood, and no others will be allowed in there.
Construction rate: The probability of accepting a spell into construction. This is to make construction get less spells to prevent it getting forging options on top of a full complement of random spells
Name: The name of the output file, probably set this to the name of your game (or it will take the seed instead)
Seed: force seed for the PRNG

Some options are redundant (it will still ask if you want to keep communions together if you're leaving them alone).

Updates to the spells.csv file should be obtained from the dom5inspector github repo (which is also under the included GPL v3) and is available at https://github.com/larzm42/dom5inspector - (specifically, check the gamedata folder)

The spells.csv included in this version is for Dominions 5.48.