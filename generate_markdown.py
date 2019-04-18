#! /usr/bin/python

import channellist_pb2 #protobuf storage of channels
import sys #to get script arguments

PATH='./'
FILENAME = 'README.md'
FILEPATH = PATH + FILENAME


file_contents = """"""

file_header = """
# List of Educational YouTube channels
### Mathematics and Computing Science
###### Inspiring and Insightful
"""

file_footer = """
### How to contribute?
>SEE INSTRUCTIONS.md
>THIS README file is generated using python script (generate_markdown.py).
>DO NOT EDIT README.md manually. Changes will be overwritten by generate_markdown.py
***
### Footnotes
>channels listed here do not rely heavily on advertisements and expect to see very less sponsered content in them.

***
"""

# Iterates though all people in the ChannelList and adds to a list.
def GenerateMarkdownTable(channel_list):
  
  channel_content = """"""
  channels_data = []
  serial = 0
  for channel in channel_list.channel:
    serial = serial + 1
    channel_name = channel.c_name
    if channel.HasField('c_link'):
      channel_link = channel.c_link
    else:
      channel_link = ''
    if channel.HasField('c_desc'):
      channel_desc1 = channel.c_desc.c_desc_1
      channel_desc2 = channel.c_desc.c_desc_2
    
    entry = """|%s.| [%s](%s)|<ul> <li>%s<br><br> <li>%s|
"""%(serial,channel_name,channel_link,channel_desc1,channel_desc2)      
  
    channel_content = channel_content + entry

  return channel_content

def GenerateMarkdownFile(channel_table):
  
  channel_table_header = """|S.No.|           Channel            |          Short Description            |
|----|------------------------------|---------------------------------------|
"""
  channel_table = channel_table_header + channel_table
  file_contents = file_header + channel_table + file_footer
  with open(FILEPATH, 'wt') as file:
    file.write(file_contents)

# Main procedure:  Reads the entire channel list from a file and generate a markdown file.
CHANNEL_LIST_FILE = "CHANNEL_LIST"

if len(sys.argv) != 2:
  print("Using default channellist file:", CHANNEL_LIST_FILE)
else:
  CHANNEL_LIST_FILE = sys.argv[1]

channel_list = channellist_pb2.ChannelList()

# Read the existing channel list.
f = open(CHANNEL_LIST_FILE, "rb")
channel_list.ParseFromString(f.read())
f.close()

# Get channel content in markdown table
channel_table = GenerateMarkdownTable(channel_list)

# Generate final markdown file from markdown table
GenerateMarkdownFile(channel_table)


