import requests

BASE_URL = 'https://toyokounqpeptides.s3-us-west-2.amazonaws.com/tripep/N{}-R{}.dmd.1.out'
#https://toyokounqpeptides.s3-us-west-2.amazonaws.com/tripep/NALAALACALA-R1.dmd.1.out

class Getfiles3pep():
    """
    Only for tripeptides
    """
    def __init__(self):
        pass
    
    def get(self, peptide):
        """
        get 5 replicas
        """
        results = []
        for replica in range(1,6):
            x = requests.get(BASE_URL.format(peptide, replica))
            results.append(x.text)
        return results





    

