##Transcribing DNA into RNA
##Skip input data validation

seq = "GATGGAACTTGACTACGTAAATT"

def transcribe(seq):
    return seq.replace("T","U")


print(transcribe(seq))