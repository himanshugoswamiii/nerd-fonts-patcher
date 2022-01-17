#   For Regular
#import fontforge
#
## Here we telling which font we want to change
#name="RecMonoCasual-Regular" 
#file_name="./{}.ttf".format(name)
#
## Open the file
#delugia=fontforge.open(file_name)              
#
## Rename the file
#delugia.fontname=name
#delugia.familyname=name
#delugia.fullname=name
#delugia.copyright=""
#
## Save
#delugia.generate(file_name)

# ------- For Bold after Patching
import fontforge

# Here we telling which font we want to change
name="RecMonoCasual-Bold Nerd Font Complete" 
file_name="./{}.ttf".format(name)

# Open the file
delugia=fontforge.open(file_name)              

# Rename the file
delugia.fontname=name
delugia.familyname=name
delugia.fullname=name
delugia.copyright=""

# Save
delugia.generate(file_name)
