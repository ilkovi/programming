#!/usr/bin/python

# Open a file
fo = open("foot.txt", "wb")

print "Name of the file: ", fo.name

# Here it does nothing, but yo ucan call it whti read opertion.
fo.flush()


# Close opend file
fo.close()
