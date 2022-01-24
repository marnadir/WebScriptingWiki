
# Get Contenet Wikipedia

The script creates xlsx files from decompressed file obtainted by the script WikiExtractor.py.

Remaind the WikiExtractor.py get as input a Wikipedia dump file and generetes a set of decompressed file.

Each file will contain several documents in the format:

	<doc id="" url="" title="">
	    --Information about the "title" word
	    </doc>
      
The script ExtractContent.py decrompresses such document and generates a set of xlsx files.

Each file will have as fields: title and description.
	   
       
