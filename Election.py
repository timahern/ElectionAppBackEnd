

class Election:
    def __init__(self, eID, name, date, description =None, candidates = None):
        self.eID = eID
        self.name = name
        self.date = date
        self.description = description
        self.candidates = candidates if candidates is not None else []
        
    def get_eID(self):
        return self.eID
    
    def get_date(self):
        return self.date
    
    def get_name(self):
        return self.name

    def update_description(self, new_desc):
        self.description = new_desc
    
    def get_description(self):
        if self.description:
            return self.description
        else:
            return None
    
    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def get_candidates(self):
        if len(self.candidates) == 0:
            return []
        else:
            return self.candidates
        
    
    def to_dict(self):
        #Convert to a dict for JSON serialization
        return {
            "eID": self.eID,
            "name": self.name,
            "date": self.date,
            "description": self.description,
            "candidates": self.candidates
        }