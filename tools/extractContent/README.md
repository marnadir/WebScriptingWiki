
# Get Contenet Wikipedia

The script creates xlsx files from decompressed file obtainted by the script WikiExtractor.py.


## Usage

### Wikiextractor
The script is invoked with set of folders which itself contains set of compressed files:

    python WikiExtraxtContent.py <path the set of folder>


Remaind the WikiExtractor.py get as input a Wikipedia dump file and generetes a set of folders which itself contains set of compressed files.

Each file will contain several documents in the format:

	<doc id="" url="" title="">
	    --Information about the "title" word
	    </doc>
      
The script WikiExtractContent.py decrompresses such document and generates a set of xlsx files.

Each file will have as fields: title and description.
	   
       
